from .utils import log_action

def solve_math(expression):
    """
    Evaluates a mathematical expression safely.
    """
    log_action("Academic Tutor", "Solving Math", expression)
    try:
        # Restricting scope for safety, though eval is generally risky in prod
        result = eval(expression, {"__builtins__": None}, {})
        return result
    except Exception as e:
        return f"Error solving math: {e}"

def explain_concept(concept):
    """
    Simulates a Socratic explanation.
    """
    log_action("Academic Tutor", "Explaining Concept", concept)
    return f"To understand {concept}, let's start with what you already know. How would you define the basic principles of it?"
