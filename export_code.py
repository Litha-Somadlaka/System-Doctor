import os
import datetime

# List of files to export
files = [
    "backend/adapters/base.py",
    "backend/adapters/windows.py",
    "backend/core/system_monitor.py",
    "backend/core/process_manager.py",
    "backend/main.py",
    "src-ui/src/app.css",
    "src-ui/src/App.svelte",
    "src-ui/src/components/Card.svelte",
    "src-ui/src/components/Gauge.svelte",
    "src-ui/src/components/Avatar.svelte",
    "src-ui/package.json",
    "src-ui/vite.config.js",
    "src-tauri/src/main.rs",
    "src-tauri/tauri.conf.json",
    "src-tauri/Cargo.toml",
    "README.md"
]

print(f"Current Working Directory: {os.getcwd()}")
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
output_file = f"all_project_code_{timestamp}.txt"

with open(output_file, "w", encoding="utf-8") as out:
    out.write("SYSTEM DOCTOR - COMPLETE SOURCE CODE EXPORT\n")
    out.write("===========================================\n\n")
    
    for f in files:
        if os.path.exists(f):
            print(f"Found: {f}")
            out.write(f"\n{'='*80}\n")
            out.write(f"FILE: {f}\n")
            out.write(f"{'='*80}\n\n")
            try:
                with open(f, "r", encoding="utf-8") as infile:
                    out.write(infile.read())
            except Exception as e:
                out.write(f"\n[ERROR READING FILE: {e}]\n")
        else:
            print(f"MISSING: {f}")
            out.write(f"\n{'='*80}\n")
            out.write(f"FILE: {f} (NOT FOUND)\n")
            out.write(f"{'='*80}\n")

print(f"Exported code to: {os.path.abspath(output_file)}")
