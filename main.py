from dsa_chatbot import DSAChatbot
import sys

def main():
    print("🤖 DSA Chatbot (Powered by Gemini)\n")
    print("Commands: 'exit', 'quit', 'clear'\n")
    
    try:
        chatbot = DSAChatbot()
        print("✅ Chatbot is ready!\n")
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

    while True:
        try:
            user_input = input("You: ").strip()
            
            if user_input.lower() in ['exit', 'quit', 'bye']:
                print("👋 Thank you! Happy Learning DSA!")
                break
                
            elif user_input.lower() == 'clear':
                print(chatbot.reset_conversation())
                continue
                
            if not user_input:
                continue
                
            print("\nThinking...\n")
            response = chatbot.get_response(user_input)
            print(f"Bot:\n{response}\n")
            
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()