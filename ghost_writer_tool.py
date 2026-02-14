from .utils import log_action

def generate_content(context, topic, tone="neutral"):
    """
    Simulates content generation (mocking LLM call for now).
    In a real scenario, this would call OpenAI/Gemini.
    """
    log_action("Ghost Writer", "Generating Content", f"Topic: {topic}, Tone: {tone}")
    
    # Mock response based on the 'Context' idea
    draft = f"""
    [Draft Content for: {topic}]
    
    (Using tone: {tone})
    
    Here is a sample draft reflecting the requested style. 
    It avoids AI jargon and focuses on the core message.
    
    Reference: As seen in the context provided ({context[:20]}...).
    """
    return draft.strip()
