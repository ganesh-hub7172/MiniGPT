import streamlit as st
import requests

# Page configuration
st.set_page_config(
    page_title="MiniGPT",
    page_icon="🤖",
    layout="centered"
)

OLLAMA_URL = "http://localhost:11434/api/chat"
DEFAULT_MODEL = "llama3.2"

# App title
st.title("🤖 MiniGPT")
st.caption("Your Personal AI Chatbot powered by Ollama")

# Session state for chat memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")

    model = st.text_input(
        "Ollama Model",
        value=DEFAULT_MODEL
    )

    st.info("Make sure Ollama is running on your computer.")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
prompt = st.chat_input("Ask MiniGPT anything...")

if prompt:
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""

        try:
            payload = {
                "model": model,
                "messages": st.session_state.messages,
                "stream": True
            }

            response = requests.post(
                OLLAMA_URL,
                json=payload,
                stream=True,
                timeout=(10, 300)
            )

            response.raise_for_status()

            for line in response.iter_lines():
                if line:
                    import json
                    data = json.loads(line)

                    content = data.get("message", {}).get("content", "")
                    full_response += content

                    response_placeholder.markdown(
                        full_response + "▌"
                    )

            response_placeholder.markdown(full_response)

            st.session_state.messages.append({
                "role": "assistant",
                "content": full_response
            })

        except requests.exceptions.ConnectionError:
            st.error(
                "Cannot connect to Ollama. "
                "Please start Ollama on your computer."
            )

        except requests.exceptions.RequestException as error:
            st.error(f"Ollama API error: {error}")

        except Exception as error:
            st.error(f"Unexpected error: {error}")
