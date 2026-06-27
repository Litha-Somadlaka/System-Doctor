# System Doctor - Prototype Setup

## Prerequisites
- Node.js (v18+)
- Rust (latest stable)
- Python 3.11+

## Quick Start Hooks
1. **Install Frontend Dependencies:**
   ```bash
   cd src-ui
   npm install
   ```
2. **Setup Backend:**
   Ensure `psutil` is installed:
   ```bash
   pip install psutil
   ```
3. **Run Application:**
   From the root directory (or `src-ui` depending on setup preference, but Tauri usually runs from root or where `src-tauri` is visible if configured):
   
   Actually, with the current structure where `src-tauri` and `src-ui` are siblings in root:
   ```bash
   cd src-ui
   npm run tauri dev
   ```

   *Note: On first run, Rust keys and dependencies will be downloaded. This may take a few minutes.*

## Architecture
- **Backend:** `backend/` (Python)
- **Frontend:** `src-ui/` (Svelte + Vite)
- **Tauri Core:** `src-tauri/` (Rust)
