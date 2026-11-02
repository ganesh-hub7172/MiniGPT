# 🤖 MiniGPT – Personal AI Chatbot

MiniGPT is a simple AI-powered chatbot built using Python, Streamlit, and Ollama. It allows users to interact with a locally running Large Language Model (LLM) through a clean web interface.

## 🚀 Features

- Interactive chatbot interface
- Local AI model integration using Ollama
- Chat history and conversation memory during the session
- Streaming AI responses
- Clear chat option
- Custom Ollama model selection
- No OpenAI or Gemini API key required

## 🛠️ Technologies Used

- Python
- Streamlit
- Ollama
- REST API
- Llama 3.2

## 📁 Project Structure

```text
MiniGPT/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/ganesh-hub7172/MiniGPT.git
cd MiniGPT
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Install Ollama

Download Ollama:

https://ollama.com/

### 6. Download the AI model

```bash
ollama pull llama3.2
```

### 7. Run the application

```bash
python -m streamlit run app.py
```

Open:

http://localhost:8501

## 🔐 Privacy

MiniGPT communicates with Ollama running locally on your computer. No external OpenAI or Gemini API key is required.

## 🔮 Future Improvements

- Persistent chat history
- PDF document chat
- Multiple model support
- Conversation export
- Improved error handling

## 👨‍💻 Author

Ganesh Musham

GitHub: https://github.com/ganesh-hub7172

LinkedIn: https://www.linkedin.com/in/ganesh-musham-14946b333/

---

⭐ If you find this project useful, consider giving it a star!
