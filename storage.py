import os
import json
from encryption import encrypt_text, decrypt_text

NOTES_DIR = "notes"

if not os.path.exists(NOTES_DIR):
    os.makedirs(NOTES_DIR)

def save_note(title, content):
    encrypted_content = encrypt_text(content)
    with open(f"{NOTES_DIR}/{title}.json", "w") as file:
        json.dump({"content": encrypted_content}, file)

def load_note(title):
    try:
        with open(f"{NOTES_DIR}/{title}.json", "r") as file:
            data = json.load(file)
            return decrypt_text(data["content"])
    except FileNotFoundError:
        return None

def list_notes():
    return [f.replace(".json", "") for f in os.listdir(NOTES_DIR) if f.endswith(".json")]
