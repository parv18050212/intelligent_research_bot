# 🧠 Intelligent Research Bot

An intelligent research assistant that allows users to upload PDFs, query them using natural language, and receive context-aware answers. Powered by **AWS Bedrock**, **Pinecone**, **Flask**, and **Streamlit**.

---
## 🚀 Live Demo

👉 [Click here to try the app](http://54.147.246.159:8501/) 👈

## 🚀 Features

* 📄 PDF Upload and Text Chunking
* 🦮 Embedding with Amazon Titan (via AWS Bedrock)
* 📆 Vector storage and retrieval using Pinecone
* 🤖 Natural language Q\&A using context-based prompt generation
* 🔥 Simple UI built with Streamlit
* 🧪 Flask REST API backend

---

## 🛠️ Tech Stack

| Layer      | Tool/Service                 |
| ---------- | ---------------------------- |
| Frontend   | Streamlit                    |
| Backend    | Flask                        |
| Embeddings | Amazon Titan via AWS Bedrock |
| Vector DB  | Pinecone (Serverless)        |
| Hosting    | AWS EC2                      |

---

## 📁 Project Structure

```
intelligent_research_bot/
├── backend/
│   ├── app/
│   │   ├── routes/
│   │   ├── services/
│   │   └── __init__.py
│   ├── main.py
│   └── .env
├── frontend/
│   └── streamlit_app.py
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/intelligent_research_bot.git
cd intelligent_research_bot
```

### 2. Setup Environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Configure `.env`

```env
AWS_REGION=us-east-1
AWS_ACCESS_KEY_ID=YOUR_KEY
AWS_SECRET_ACCESS_KEY=YOUR_SECRET
BEDROCK_MODEL=amazon.titan-embed-text-v1
PINECONE_API_KEY=your-pinecone-key
PINECONE_ENV=us-east-1-aws
PINECONE_INDEX_NAME=researchbot-index
```

### 4. Run Backend (Flask)

```bash
cd backend
export FLASK_APP=main
flask run --host=0.0.0.0 --port=8000
```

### 5. Run Frontend (Streamlit)

```bash
cd frontend
streamlit run streamlit_app.py --server.port=8501 --server.address=0.0.0.0
```

---

## 🥪 Example Usage

1. Upload a PDF document.
2. Ask a question related to the content.
3. Get a smart, contextually aware response based on the document.

---

## 💡 Future Improvements

* Add user authentication
* Support for multiple document types
* Chat history and memory
* Fine-tuned model options

---

## 🛡️ License

MIT License

---

## 🤝 Contributing

PRs are welcome! Please fork the repo and open a pull request with your changes.

---

## 📬 Contact

Made by Parv Agarwal – feel free to connect!
