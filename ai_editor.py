from .utils import log_action
try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    Image = None

def edit_image(image_path, instructions, code_block=None):
    """
    Executes edits. If code_block is provided (from the agent), it executes that.
    Otherwise, it mocks the edit.
    """
    log_action("AI Editor", "Editing Image", f"Path: {image_path}, Instructions: {instructions}")
    
    if code_block:
        log_action("AI Editor", "Executing Custom Code", "Running provided Python code...")
        try:
            # Dangerous in prod, typical for "Code Interpreter" style agents locally
            exec(code_block)
            return f"Edited image using custom code."
        except Exception as e:
            return f"Error executing code: {e}"
            
    return f"Simulated edit on {image_path} based on: {instructions}"
