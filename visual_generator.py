from .utils import log_action

def generate_image(prompt, aspect_ratio="1:1"):
    """
    Simulates calling an external Image Gen API (DALL-E 3 / Stability).
    """
    log_action("Visual Generator", "Generating Image", f"Prompt: {prompt}, AR: {aspect_ratio}")
    
    # Mock return path
    filename = f"image_{prompt[:10].replace(' ', '_')}.png"
    return f"/path/to/generated/{filename}"
