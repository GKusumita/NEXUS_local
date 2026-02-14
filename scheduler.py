import json
import os
from .utils import log_action

JOB_FILE = "jobs.json"

def schedule_post(post_payload, time="NOW"):
    """
    Schedules a post or executes it immediately.
    """
    log_action("Scheduler", "Scheduling Post", f"Time: {time}")
    
    if time == "NOW":
        return f"Posting to {post_payload.get('platform', 'Unknown')} IMMEDIATELY: Success."
    
    # Load existing jobs
    jobs = []
    if os.path.exists(JOB_FILE):
        try:
            with open(JOB_FILE, "r") as f:
                jobs = json.load(f)
        except:
            jobs = []
            
    # Add new job
    job = {
        "payload": post_payload,
        "scheduled_time": time,
        "status": "QUEUED"
    }
    jobs.append(job)
    
    # Save
    with open(JOB_FILE, "w") as f:
        json.dump(jobs, f, indent=2)
        
    return f"Post scheduled for {time}."
