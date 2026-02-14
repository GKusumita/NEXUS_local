import re
from execution.utils import load_directive, log_action
from execution import (
    ghost_writer_tool, 
    academic_tutor, 
    visual_generator, 
    ai_editor, 
    social_manager, 
    scheduler
)

class Orchestrator:
    def __init__(self):
        log_action("Orchestrator", "Startup", "Initializing System...")
        
    def determine_intent(self, user_input):
        """
        Simple keyword-based routing for demonstration. 
        In production, this would use an LLM call.
        """
        u = user_input.lower()
        if "formula" in u or "solve" in u or "study" in u:
            return "ACADEMIC"
        elif "write" in u or "essay" in u or "draft" in u:
            return "CREATIVE_WRITING"
        elif "image" in u or "generate" in u or "visual" in u:
            return "VISUAL_GEN"
        elif "edit" in u and "image" in u:
            return "EDITING"
        elif "linkedin" in u:
            return "SOCIAL_LINKEDIN"
        elif "instagram" in u or "stitch" in u:
            return "SOCIAL_INSTAGRAM"
        else:
            return "GENERAL"

    def handle_request(self, user_input):
        intent = self.determine_intent(user_input)
        log_action("Orchestrator", "Routing", f"Input: '{user_input}' -> Intent: {intent}")
        
        response = "I'm not sure how to handle that."
        
        if intent == "ACADEMIC":
            if "solve" in user_input.lower():
                # Extract math roughly
                expression = re.sub(r'[a-zA-Z\s]', '', user_input)
                response = academic_tutor.solve_math(expression)
            else:
                response = academic_tutor.explain_concept(user_input)
                
        elif intent == "CREATIVE_WRITING":
            response = ghost_writer_tool.generate_content("User Query", user_input)
            
        elif intent == "VISUAL_GEN":
            response = visual_generator.generate_image(user_input)
            
        elif intent == "EDITING":
            # Mocking an image path for the example
            response = ai_editor.edit_image("sample.png", user_input)
            
        elif intent == "SOCIAL_LINKEDIN":
            # Chained workflow example
            draft = ghost_writer_tool.generate_content("LinkedIn Topic", user_input)
            post = social_manager.create_linkedin_post(draft)
            response = scheduler.schedule_post(post, "NOW")
            
        elif intent == "SOCIAL_INSTAGRAM":
            prompt = f"Photo for {user_input}"
            img_path = visual_generator.generate_image(prompt)
            post = social_manager.create_instagram_post(user_input, img_path)
            response = scheduler.schedule_post(post, "Schedule")
            
        elif intent == "GENERAL":
            response = "I am the Central Brain. I can help you with Academic, Creative, Visual, and Social Tasks."

        return response
