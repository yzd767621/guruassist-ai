from pathlib import Path
import os
from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse

app = FastAPI(title="GuruAssist — Autonomous PBD Agent (DEMO / SAMPLE)")
BASE_DIR = Path(__file__).resolve().parent


@app.get("/")
async def index():
    return FileResponse(BASE_DIR / "index.html")


@app.get("/api/health")
async def health():
    return JSONResponse({"status": "ok", "app": "GuruAssist", "watermark": "DEMO / SAMPLE"})


if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
