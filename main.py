import sys
from orchestrator import Orchestrator

def main():
    bot = Orchestrator()
    print("Welcome to NEXUS (Local Execution Mode)")
    print("Type 'exit' to quit.\n")
    
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit"]:
                break
            
            response = bot.handle_request(user_input)
            print(f"NEXUS: {response}\n")
            
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
