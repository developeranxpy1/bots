import os
import base64
import requests
import json

# Configuration
CONFIG_PATH = r"C:/Users/rgb/Desktop/alphaseoand marketing/forbidden/config.json"
TRANSCRIPT_PATH = r"C:\Users\rgb\.openclaw\agents\main\sessions\6c5a7018-c194-48b7-9f82-7f3219ddc93b.jsonl"
MNEMONIC = "younger-fuzzy-ensign-smog-eating-wife-picked-eight-alley-cucumber-whale-nudged-wife"
REPO_FILE_PATH = f"transcripts/{MNEMONIC}.jsonl"

with open(CONFIG_PATH, "r") as f:
    config = json.load(f)

TOKEN = config["GITHUB_TOKEN"]
OWNER = config["REPO_OWNER"]
REPO = config["REPO_NAME"]
BRANCH = config.get("BRANCH", "main")

# GitHub API
API_URL = f"https://api.github.com/repos/{OWNER}/{REPO}/contents/{REPO_FILE_PATH}"

def upload():
    with open(TRANSCRIPT_PATH, "r", encoding="utf-8", errors="ignore") as f:
        content_text = f.read()

    # Scrub potential secrets
    import re
    content_text = re.sub(r'ghp_[a-zA-Z0-9]{36}', 'SCRUBBED_TOKEN', content_text)
    content_text = re.sub(r'gsk_[a-zA-Z0-9]{36}', 'SCRUBBED_TOKEN', content_text)
    
    content = base64.b64encode(content_text.encode("utf-8")).decode("utf-8")

    # Get SHA if exists
    resp = requests.get(API_URL, headers={"Authorization": f"token {TOKEN}"}, params={"ref": BRANCH})
    sha = None
    if resp.status_code == 200:
        sha = resp.json().get("sha")

    data = {
        "message": f"Upload session transcript: {MNEMONIC}",
        "content": content,
        "branch": BRANCH
    }
    if sha:
        data["sha"] = sha

    resp = requests.put(API_URL, headers={"Authorization": f"token {TOKEN}"}, json=data)
    if resp.status_code in [200, 201]:
        print(f"Successfully uploaded to {OWNER}/{REPO}/{REPO_FILE_PATH}")
    else:
        print(f"Failed to upload: {resp.status_code} - {resp.text}")

if __name__ == "__main__":
    upload()
