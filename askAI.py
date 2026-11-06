
import streamlit as st
import requests

API_KEY = st.secrets["OPENROUTER_API_KEY"]

url = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

payload = {
    "model": "nvidia/nemotron-3-ultra-550b-a55b:free",
    "messages": [
        {
            "role": "user",
            "content": "Reply with exactly one word: Hello"
        }
    ]
}

try:
    response = requests.post(
        url,
        headers=headers,
        json=payload,
        timeout=120
    )

    response.raise_for_status()

    answer = response.json()["choices"][0]["message"]["content"]

    st.success("Nemotron connection successful!")
    st.write(answer)

except requests.exceptions.RequestException as e:
    st.error(f"Connection failed: {e}")
