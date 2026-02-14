from flask import Flask, request, jsonify, make_response
import os
import subprocess
import re

app = Flask(__name__)
TV_IP = os.getenv('TV_IP', '192.168.0.140:5555')

def adb_raw(args):
    """Быстрый запуск команды без ожидания вывода"""
    full_cmd = ["adb", "-s", TV_IP] + args
    subprocess.Popen(full_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def check_conn():
    """Проверка и восстановление коннекта"""
    state = subprocess.getoutput(f"adb -s {TV_IP} get-state")
    if "device" not in state:
        subprocess.run(["adb", "connect", TV_IP], timeout=2)

@app.route('/')
def index():
    # Читаем файл при каждом запросе (для разработки)
    with open('index.html', 'r', encoding='utf-8') as f:
        response = make_response(f.read())
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    return response

@app.route('/adb')
def adb():
    cmd = request.args.get('cmd', '')
    if cmd:
        # Разбиваем строку команды в список для Popen
        adb_raw(cmd.split())
    return "OK"

@app.route('/stats')
def stats():
    try:
        # Статистику ждем, но недолго
        out = subprocess.check_output(["adb", "-s", TV_IP, "shell", "free", "-m"], timeout=1.5).decode()
        lines = out.splitlines()
        ram = re.findall(r'\d+', lines[1])
        swp = re.findall(r'\d+', [l for l in lines if "Swap" in l][0])
        return jsonify({
            "ram_p": round((int(ram[1]) / int(ram[0])) * 100),
            "swap_p": round((int(swp[1]) / int(swp[0])) * 100) if int(swp[0]) > 0 else 0
        })
    except:
        check_conn() # Если упало, пробуем переподключиться
        return jsonify({"ram_p": 0, "swap_p": 0, "error": True})

if __name__ == '__main__':
    subprocess.run(["adb", "start-server"])
    check_conn()
    app.run(host='0.0.0.0', port=5000, threaded=True)