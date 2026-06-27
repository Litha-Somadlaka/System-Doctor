# Create Project Structure in the current directory (project root)
$root = "."

# Create directories
New-Item -Path "$root/src-ui/src/components" -ItemType Directory -Force
New-Item -Path "$root/src-ui/src/routes" -ItemType Directory -Force
New-Item -Path "$root/src-ui/public" -ItemType Directory -Force

New-Item -Path "$root/src-tauri/src" -ItemType Directory -Force
New-Item -Path "$root/src-tauri/capabilities" -ItemType Directory -Force

New-Item -Path "$root/backend/core" -ItemType Directory -Force
New-Item -Path "$root/backend/adapters" -ItemType Directory -Force
New-Item -Path "$root/backend/utils" -ItemType Directory -Force

New-Item -Path "$root/scripts" -ItemType Directory -Force

# Create placeholder files
New-Item -Path "$root/backend/main.py" -ItemType File -Force
New-Item -Path "$root/backend/requirements.txt" -ItemType File -Force
Set-Content -Path "$root/backend/requirements.txt" -Value "psutil`nrequests"

New-Item -Path "$root/backend/adapters/__init__.py" -ItemType File -Force
New-Item -Path "$root/backend/adapters/base.py" -ItemType File -Force
New-Item -Path "$root/backend/adapters/windows.py" -ItemType File -Force
New-Item -Path "$root/backend/adapters/macos.py" -ItemType File -Force
New-Item -Path "$root/backend/adapters/linux.py" -ItemType File -Force

Write-Host "Folder structure created at $PWD"
