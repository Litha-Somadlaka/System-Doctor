$files = @(
    "backend/adapters/base.py",
    "backend/adapters/windows.py",
    "backend/core/system_monitor.py",
    "backend/core/process_manager.py",
    "backend/main.py",
    "src-ui/src/App.svelte",
    "src-ui/package.json",
    "src-ui/vite.config.js",
    "src-tauri/src/main.rs",
    "src-tauri/tauri.conf.json",
    "src-tauri/Cargo.toml",
    "README.md"
)

$output = "all_project_code.txt"
Set-Content -Path $output -Value "SYSTEM DOCTOR - COMPLETE SOURCE CODE EXPORT`nGenerated on $(Get-Date)`n"

foreach ($f in $files) {
    if (Test-Path $f) {
        Add-Content -Path $output -Value "`n=============================================================================="
        Add-Content -Path $output -Value "FILE: $f"
        Add-Content -Path $output -Value "==============================================================================`n"
        Get-Content $f | Add-Content -Path $output
    } else {
        Add-Content -Path $output -Value "`n[MISSING FILE: $f]`n"
    }
}

Write-Host "Code export complete: $output"
