from .utils import log_action

def create_linkedin_post(text, image_path=None):
    """
    Formats and prepares a LinkedIn post.
    """
    log_action("LinkedIn Agent", "Creating Draft", f"Text len: {len(text)}")
    
    post = {
        "platform": "LinkedIn",
        "text": text,
        "image": image_path,
        "status": "DRAFT"
    }
    return post

def create_instagram_post(caption, image_path):
    """
    Formats and prepares an Instagram post.
    """
    log_action("Instagram Agent", "Creating Draft", f"Caption: {caption}")
    
    post = {
        "platform": "Instagram",
        "caption": caption,
        "image": image_path,
        "status": "DRAFT"
    }
    return post
