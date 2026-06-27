// Prevents additional console window on Windows in release, DO NOT REMOVE!!
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

use tauri::{Emitter, Listener};
use tauri_plugin_shell::ShellExt;
use tauri_plugin_shell::process::CommandEvent;
use std::sync::{Arc, Mutex};

fn main() {
    tauri::Builder::default()
        .plugin(tauri_plugin_shell::init())
        .plugin(tauri_plugin_log::Builder::default().build())
        .setup(|app| {
            let window = app.get_webview_window("main").unwrap();
            
            // Spawn Python Sidecar (expecting 'python' in path or bundled)
            // Note: In development we often use absolute path or relative to CWD
            // For MVP on this machine, we assume 'python' is in PATH.
            // Using a simple shell command for flexibility in dev.
            let sidecar_command = app.shell().sidecar("python").unwrap_or_else(|_| {
                 // Fallback to calling python directly if sidecar bundling isn't set up yet
                 app.shell().command("python")
            });

            // Arguments to run the backend
            let (mut rx, mut child) = sidecar_command
                .args(["backend/main.py"]) 
                .spawn()
                .expect("Failed to spawn python backend");

            let window_clone = window.clone();
            
            // Async Reader Thread for Python STDOUT
            tauri::async_runtime::spawn(async move {
                while let Some(event) = rx.recv().await {
                    if let CommandEvent::Stdout(line_bytes) = event {
                        let line = String::from_utf8_lossy(&line_bytes);
                        // Forward JSON directly to UI as an event
                        // SystemMonitor emits {"type": "stats_update", ...}
                        // We emit "backend-message" payload
                        if let Ok(json) = serde_json::from_str::<serde_json::Value>(&line) {
                             window_clone.emit("backend-message", json).unwrap(); 
                        }
                    }
                }
            });

            Ok(())
        })
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
