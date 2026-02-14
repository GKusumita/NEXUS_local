import os
import json
from datetime import datetime

def log_action(agent_name, action, details):
    """Logs actions to a file."""
    timestamp = datetime.now().isoformat()
    entry = {
        "timestamp": timestamp,
        "agent": agent_name,
        "action": action,
        "details": details
    }
    
    log_file = "system.log"
    with open(log_file, "a") as f:
        f.write(json.dumps(entry) + "\n")
    print(f"[{agent_name}] {action}: {details}")

def load_directive(directive_name):
    """Loads a directive from the directives directory."""
    path = os.path.join("directives", directive_name)
    if os.path.exists(path):
        with open(path, "r") as f:
            return f.read()
    return f"Directive {directive_name} not found."
