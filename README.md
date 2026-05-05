# DSA Chatbot using Gemini API 🤖

An intelligent chatbot that answers **Data Structures and Algorithms (DSA)** questions using Google’s Gemini Large Language Model (LLM).

This project demonstrates my practical understanding of Generative AI, prompt engineering, and clean Python application development.

## ✨ Features

- Structured responses with **Explanation + Python Code Example + Time & Space Complexity**
- Maintains short conversation context (memory)
- Strong System Prompt for consistent, high-quality answers
- Good error handling and input validation
- Two Interfaces:
  - Command Line Interface (CLI)
  - Web Interface using **Streamlit**
- Clean and modular code structure

## 🛠 Tech Stack

- **Python 3.10+**
- **Google Gemini API** (Generative AI)
- **Streamlit** - For Web UI
- **python-dotenv** - For managing API keys securely

## 🚀 How to Run

1. Clone the repository:
   
   -git clone <repository url>
   -cd dsa-chatbot

2. Install required packages:
    -pip install -r requirements.txt
   
4. Get your Gemini API Key from Google AI Studio

5. Create environment file:
    -cp .env.example .envOpen .env file and paste your actual Gemini API key.
   
6. Run CLI(main) Version:
    -python main.py

7. Run the Application:
    -streamlit run app.py


What I Learned : 

  - Integrating LLM (Gemini) into Python applications
  - Prompt Engineering and System Instructions
  - Managing conversation history in chatbots
  - Building modular and scalable code structure
  - Creating both CLI and Web-based interfaces
  - Secure API key management using environment variables
