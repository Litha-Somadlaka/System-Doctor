import os

def create_dirs():
    dirs = [
        "src-ui",
        "src-ui/src",
        "src-ui/src/lib",
        "src-ui/src/assets",
        "src-ui/public",
        "src-tauri",
        "src-tauri/src",
        "src-tauri/capabilities",
        "src-tauri/icons"
    ]
    
    base = os.getcwd()
    print(f"Creating directories in {base}")
    
    for d in dirs:
        path = os.path.join(base, d)
        try:
            os.makedirs(path, exist_ok=True)
            print(f"Created: {path}")
        except Exception as e:
            print(f"Error creating {path}: {e}")

if __name__ == "__main__":
    create_dirs()
