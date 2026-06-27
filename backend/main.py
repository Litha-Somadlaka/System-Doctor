import sys
import json
import time
import threading
import argparse
from core.system_monitor import SystemMonitor
from core.process_manager import ProcessManager

# Global flag for shutdown
running = True

def stat_loop(monitor: SystemMonitor, interval: float = 2.0):
    """
    Background thread that pushes stats to stdout periodically.
    """
    global running
    while running:
        try:
            stats = monitor.get_health_stats()
            # Construct the update message
            msg = {
                "type": "stats_update",
                "data": stats
            }
            # Write to stdout using flush to ensure immediate sending
            print(json.dumps(msg))
            sys.stdout.flush()
            time.sleep(interval)
        except Exception as e:
            # Log to stderr so it doesn't break the JSON stream
            print(f"Error in stat loop: {e}", file=sys.stderr)
            time.sleep(interval)

def main():
    global running
    parser = argparse.ArgumentParser(description="System Doctor Backend")
    parser.add_argument("--mode", type=str, default="interactive", help="Run mode: interactive (IPC) or oneshot")
    args = parser.parse_args()

    monitor = SystemMonitor()
    proc_mgr = ProcessManager()

    if args.mode == "oneshot":
        props = monitor.get_health_stats()
        print(json.dumps(props, indent=2))
        return

    # --- Interactive/Sidecar Mode ---
    
    # 1. Start the Stat Pushing Thread
    t = threading.Thread(target=stat_loop, args=(monitor, 2.0), daemon=True)
    t.start()

    # 2. Main Loop: Listen for Commands via STDIN
    # Tauri (or any parent process) sends commands as JSON lines
    try:
        for line in sys.stdin:
            if not line:
                break
            try:
                cmd = json.loads(line)
                action = cmd.get("action")
                
                response = {"type": "command_response", "action": action, "status": "ok"}
                
                if action == "boost":
                    # Run cleanup
                    result = monitor.run_cleanup()
                    response["result"] = result
                elif action == "get_processes":
                    limit = cmd.get("limit", 5)
                    procs = proc_mgr.get_top_processes(limit)
                    response["processes"] = procs
                elif action == "exit":
                    running = False
                    break
                else:
                    response["status"] = "error"
                    response["message"] = f"Unknown command: {action}"
                
                print(json.dumps(response))
                sys.stdout.flush()
                
            except json.JSONDecodeError:
                print(json.dumps({"type": "error", "message": "Invalid JSON"}), file=sys.stderr)
    except KeyboardInterrupt:
        pass
    finally:
        running = False
        print("Backend stopping...", file=sys.stderr)

if __name__ == "__main__":
    main()
