"""
Simple AssemblyAI transcription pipeline for Romanian audio files.

Usage:
    export ASSEMBLYAI_API_KEY="your_key_here"
    python3 transcribe.py

Get a free API key at: https://www.assemblyai.com
Free tier: $50 in credits (~333 hours of audio).

Pricing (paid):
    Universal-2:     $0.15/hr  →  4 hours ≈ $0.60
    Universal-3 Pro: $0.21/hr  →  4 hours ≈ $0.84
"""

import os
import time
import httpx

API_KEY = os.environ.get("ASSEMBLYAI_API_KEY", "")
if not API_KEY:
    raise SystemExit("Set your API key: export ASSEMBLYAI_API_KEY='your_key_here'")

BASE = "https://api.assemblyai.com"
HEADERS = {"authorization": API_KEY}

AUDIO_FILES = [
    "other documents/New Recording 47.m4a",
    "other documents/New Recording 48.m4a",
    "other documents/New Recording 49.m4a",
]


def upload(path: str) -> str:
    print(f"  Uploading {path} ...")
    with open(path, "rb") as f:
        r = httpx.post(f"{BASE}/v2/upload", headers=HEADERS, content=f, timeout=300)
    r.raise_for_status()
    return r.json()["upload_url"]


def transcribe(upload_url: str) -> str:
    r = httpx.post(
        f"{BASE}/v2/transcript",
        headers=HEADERS,
        json={
            "audio_url": upload_url,
            "language_code": "ro",
            "speech_model": "universal",
            "speaker_labels": True,
        },
        timeout=30,
    )
    r.raise_for_status()
    return r.json()["id"]


def poll(transcript_id: str) -> dict:
    print("  Waiting for transcription", end="", flush=True)
    while True:
        r = httpx.get(f"{BASE}/v2/transcript/{transcript_id}", headers=HEADERS, timeout=30)
        r.raise_for_status()
        data = r.json()
        if data["status"] == "completed":
            print(" done.")
            return data
        if data["status"] == "error":
            raise RuntimeError(data.get("error", "unknown error"))
        print(".", end="", flush=True)
        time.sleep(10)


for audio_path in AUDIO_FILES:
    print(f"\nTranscribing: {audio_path}")
    try:
        url = upload(audio_path)
        tid = transcribe(url)
        data = poll(tid)

        output_path = audio_path.replace(".m4a", ".txt")
        with open(output_path, "w", encoding="utf-8") as f:
            utterances = data.get("utterances") or []
            if utterances:
                for u in utterances:
                    f.write(f"[Speaker {u['speaker']}] {u['text']}\n")
            else:
                f.write(data.get("text", ""))

        print(f"  Saved: {output_path}")
    except Exception as e:
        print(f"  ERROR: {e}")
