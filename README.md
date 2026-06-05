# SaveRoot

Built this because paying for youtube premium just to download videos offline is a financial crime 

SaveRoot is a full stack web application built step by step to rescue media from the cloud and trap it safely on your local hard drive where it belongs. Built with a fast Python backend and a modern React frontend, it’s designed to survive the impending digital apocalypse.

---

##  The Stack (How the sausage is made)

* **Backend:** FastAPI (Async Python, because waiting is for losers)
* **The Engine:** `yt-dlp` + `FFmpeg` (Ripping audio and video streams and stitching them back together)
* **Frontend:** React + Vite (A clean, state-driven UI to hide the chaos underneath)

---

##  Features (Planned & Current)

- [x] **The Trap:** A React-controlled input field that aggressively hoards the URL you paste.
- [x] **The Handshake:** A FastAPI server with CORS wide open, begging the frontend to talk to it.
- [ ] **The Interrogation:** Fetching video thumbnails, titles, and format sizes so you know what you're stealing.
- [ ] **The Extraction:** Downloading up to 4K video or ripping pure MP3 audio.
- [ ] **The Lie:** A smooth progress bar to keep you calm while the backend does all the heavy lifting.

---

##  Local Deployment (For when the internet collapses)

If you want to run this local pirate ship on your own machine:

### 1. The Back Alley (Backend Setup)
```powershell
cd backend
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

### 2. The Face Layer (Frontend Setup)

```powershell
cd frontend
npm install
npm run dev
```

---

##  Local Deployment (For when the internet collapses)

This project is strictly for educational purposes. If Google’s legal team is reading this, it's just a complex computer science assignment on streaming protocols and async architecture. Please don't sue me, I have a net worth of about $12 and a pet cat to feed
