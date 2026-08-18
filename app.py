import streamlit as st
import requests

st.set_page_config(page_title="Zeno AI", page_icon="⚡", layout="centered")

# Key یہاں سے خود اٹھے گی - آپ کو یہاں لکھنے کی ضرورت نہیں
HF_TOKEN = st.secrets["HF_TOKEN"]

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

st.title("⚡ Zeno AI")
st.caption("Duniya Ka Sabse Taiz AI")

user_input = st.text_area("آپ کیا پوچھنا چاہتے ہیں؟", height=100)

if st.button("Send 🚀"):
    if user_input:
        with st.spinner('Zeno سوچ رہا ہے...'):
            output = query({"inputs": f"<s>[INST] {user_input} [/INST]"})
            if isinstance(output, list) and 'generated_text' in output[0]:
                st.success(output[0]['generated_text'])
            elif 'error' in output:
                st.error(f"Error: {output['error']}")
            else:
                st.error("کچھ مسئلہ آ گیا۔ دوبارہ کوش کریں")
    else:
        st.warning("پہلے کوئی سوال لکھیں")
