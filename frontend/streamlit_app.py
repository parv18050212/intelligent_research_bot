import streamlit as st
import requests

API_URL = "http://localhost:5000/api"

st.set_page_config(page_title="🧠 Research Assistant", layout="wide")
st.title("📚 Intelligent Research Assistant")

# Upload PDF
st.header("📤 Upload a PDF")
uploaded_file = st.file_uploader("Upload your research paper or document", type="pdf")

if uploaded_file:
    with st.spinner("📄 Uploading and processing your file..."):
        files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "application/pdf")}
        response = requests.post(f"{API_URL}/upload", files=files)

    if response.status_code == 200:
        result = response.json()
        doc_id = result.get("doc_id")
        st.success("✅ File processed successfully!")
        st.code(f"Your doc_id: {doc_id}", language="text")
        st.session_state["doc_id"] = doc_id
    else:
        st.error("❌ Upload failed: " + response.text)

# Ask Question
st.header("🤖 Ask a Question")
doc_id_input = st.text_input("Enter your doc_id (auto-filled after upload):", value=st.session_state.get("doc_id", ""))
question = st.text_area("Your Question", placeholder="e.g., What are the main takeaways?")

if st.button("Ask"):
    if not question or not doc_id_input:
        st.warning("Please provide both question and doc_id.")
    else:
        with st.spinner("🤔 Claude is thinking..."):
            payload = {"question": question, "doc_id": doc_id_input}
            res = requests.post(f"{API_URL}/ask", json=payload)

        if res.status_code == 200:
            answer = res.json().get("answer")
            st.success("🧠 Claude says:")
            st.write(answer)
        else:
            st.error("❌ Error from API: " + res.text)