# tv-remote
Own ADB interface for home TV

[🇷🇺 Читать на русском языке](README_RU.md)

# 📺 Tv Remote: Vibecoding vs. Crappy Software

<img src="https://raw.githubusercontent.com/martimaxi/tv-remote/main/ScreenShot.png" width="250" align="right" style="margin-left: 20px; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.5);">

### A small project to "fine-tune" a specific TV
(and save the owner's nerve cells) from the strange decisions of marketing departments.

This is not just a remote control, but a neat example of **vibecoding**: when instead of weeks of planning, a solution is put together in one evening that simply works — and does it no worse than commercial alternatives.

---

### 💡 Why was this created?

The big button on the third (!) remote in a row couldn't withstand impatient children's hands and began to die quietly. Look for a compatible remote on marketplaces again? Ugh...

We go to the App Store, search for *TV Remote* — and see dozens of apps with a paid subscription (around $5-10/mo) just for the ability to press the **OK** button over Wi-Fi. At the same time, the app weighs hundreds of megabytes, is overloaded with ads, and sometimes lags as if the signal is going through Pluto.

Paying for sending ADB commands is a weird idea. So a simple alternative appeared:
**$0, minimum code, full control, and the ability to customize everything for yourself.**

---

### 🚀 Idea and Tech Stack

A lightweight Docker container that turns your phone into a fast web remote.

- **Backend:** Python (Flask) + ADB. Commands are sent instantly via `subprocess.Popen` without waiting for the TV's response.
- **Frontend:** Pure HTML5/JS + Bootstrap 5 — no heavy frameworks.
- **Vibe:** FontAwesome 6, dark theme, and nothing extra.
- **Stats:** Real-time display of RAM/Swap load right on the control buttons.

---

#### 🛠 TV Preparation (Important)

To make everything work:

1. Go to **Settings → About Device**.
2. Find **Build Number** and tap it until you see the message "You are now a developer."
3. In the **Developer Options** menu, enable:
    - **USB Debugging**
    - **Network Debugging** (if available)
4. Find out the TV's IP in the network settings and specify it in `docker-compose.yaml` (variable `TV_IP`).

> **Note:** If there is no "Network Debugging" item in the menu, try connecting the TV via USB once and running `adb tcpip 5555`.

---

### 📦 Quick Start

`docker compose up -d --build`

After launching, open the page `http://<your-ip>:5000` on your smartphone and add it to the Home Screen (**Add to Home Screen**) so the remote works as a full-fledged PWA without browser frames.

---

### 💡 Lifehack

Memory in budget TVs is always scarce. The stock launcher often takes a long time to load and pulls unnecessary services with it.

Since you now have ADB access — use it. You can disable unnecessary software (e.g., `adb shell pm disable-user com.google.android.youtube.tv`) to free up resources for things that actually matter.

---

### 👥 Authors & Credits

`@martimaxi` — Idea, field testing, macro architecture, and debugging on real hardware.

`Gemini (Google AI)` — Bulk of the code, implementation of "fast" ADB, frontend, and infinite patience for UI tweaks like "let's make the icons even larger."

---

**Have ideas for improvement?** Don't like the buttons? Need others? Or want to add voice control?

Take this project, call an AI for help, make it how you want and what you want. And be sure to share the result with others.

License: MIT

<br clear="right"/>
