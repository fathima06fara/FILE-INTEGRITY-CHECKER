import hashlib

import os

import json



# === CONFIGURATION ===

# Path to the directory you want to monitor

MONITOR_DIR = "files_to_monitor"

# File to store the hash values

HASH_RECORD_FILE = "file_hashes.json"



# === FUNCTION TO CALCULATE HASH ===

def calculate_file_hash(file_path, algo='sha256'):

    hash_func = hashlib.new(algo)

    with open(file_path, 'rb') as f:

        while chunk := f.read(8192):

            hash_func.update(chunk)

    return hash_func.hexdigest()



# === LOAD EXISTING HASHES FROM RECORD FILE ===

def load_hashes():

    if os.path.exists(HASH_RECORD_FILE):

        with open(HASH_RECORD_FILE, 'r') as f:

            return json.load(f)

    return {}



# === SAVE HASHES TO FILE ===

def save_hashes(hashes):

    with open(HASH_RECORD_FILE, 'w') as f:

        json.dump(hashes, f, indent=4)



# === SCAN DIRECTORY AND GET HASHES ===

def scan_directory(directory):

    file_hashes = {}

    for root, dirs, files in os.walk(directory):

        for filename in files:

            full_path = os.path.join(root, filename)

            file_hashes[full_path] = calculate_file_hash(full_path)

    return file_hashes



# === MAIN FUNCTION TO CHECK FOR CHANGES ===

def check_file_integrity():

    print("🔍 Checking file integrity...")

    old_hashes = load_hashes()

    new_hashes = scan_directory(MONITOR_DIR)



    added = []

    removed = []

    modified = []



    for path in new_hashes:

        if path not in old_hashes:

            added.append(path)

        elif new_hashes[path] != old_hashes[path]:

            modified.append(path)



    for path in old_hashes:

        if path not in new_hashes:

            removed.append(path)



    # Print summary

    if added:

        print("\n📁 Added Files:")

        for f in added:

            print(f"  + {f}")

    if modified:

        print("\n✏ Modified Files:")

        for f in modified:

            print(f"  ~ {f}")

    if removed:

        print("\n❌ Removed Files:")

        for f in removed:

            print(f"  - {f}")

    if not (added or removed or modified):

        print("\n✅ No changes detected. All files are intact.")



    # Save current hash state

    save_hashes(new_hashes)



# === RUN SCRIPT ===

if __name__ == "__main__":


    os.makedirs(MONITOR_DIR, exist_ok=True)

    check_file_integrity()
