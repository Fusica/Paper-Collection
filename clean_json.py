import json
import os

# Files to clean
files = [
    'docs/cv-arxiv-daily.json',
    'docs/cv-arxiv-daily-web.json',
    'docs/cv-arxiv-daily-wechat.json'
]

# Keys to keep (from user's new config)
keys_to_keep = ["6D Pose"]

for filename in files:
    if not os.path.exists(filename):
        print(f"File not found: {filename}")
        continue
        
    print(f"Cleaning {filename}...")
    with open(filename, 'r') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            print(f"Error decoding JSON in {filename}")
            continue
            
    # Find keys to remove
    keys_to_remove = [k for k in data.keys() if k not in keys_to_keep]
    
    if not keys_to_remove:
        print(f"  No keys to remove in {filename}")
        continue
        
    # Remove keys
    for k in keys_to_remove:
        del data[k]
        print(f"  Removed: {k}")
        
    # Save back
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"  Saved {filename}")

print("Cleanup complete.")
