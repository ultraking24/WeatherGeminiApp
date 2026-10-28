
import time
import streamlit as st
from google import genai
from google.genai import types

st.title("Gemini Connection Test")

if st.button("Test Gemini"):
    try:
        client = genai.Client(
            api_key=st.secrets["GEMINI_API_KEY"],
            http_options=types.HttpOptions(timeout=120000),
        )

        start = time.time()

        with st.spinner("Contacting Gemini..."):
            response = client.models.generate_content(
                model="gemini-3.8-flash",
                contents="Reply with only: Hello!",
            )

        elapsed = time.time() - start
        st.success(f"Response received in {elapsed:.1f} seconds")
        st.write(response.text)

    except Exception as e:
        st.error(f"{type(e).__name__}: {e}")
        st.exception(e)


