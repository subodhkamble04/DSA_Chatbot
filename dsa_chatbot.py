import google.generativeai as genai
from config import SYSTEM_PROMPT, GEMINI_MODEL
import os

class DSAChatbot:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not found. Please check your .env file.")
        
        genai.configure(api_key=self.api_key)
        
        self.model = genai.GenerativeModel(
            model_name=GEMINI_MODEL,
            system_instruction=SYSTEM_PROMPT
        )
        
        self.chat = self.model.start_chat(history=[])
        self.history_length = 0
        self.max_history = 8

    def get_response(self, user_message: str) -> str:
        try:
            response = self.chat.send_message(user_message)
            self.history_length += 2
            
            if self.history_length > self.max_history:
                self.chat.history = self.chat.history[-self.max_history:]
                self.history_length = self.max_history
                
            return response.text
            
        except Exception as e:
            return f"❌ Sorry, an error occurred: {str(e)}\nPlease check your API key and internet connection."

    def reset_conversation(self):
        self.chat = self.model.start_chat(history=[])
        self.history_length = 0
        return "✅ Conversation history has been cleared."