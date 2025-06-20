from flask import Blueprint, request, jsonify
from app.services.embedder import get_relevant_chunks
from app.services.bedrock_client import ask_bedrock

query_bp = Blueprint('query', __name__)

@query_bp.route('/ask', methods=['POST'])
def ask_question():
    data = request.get_json()
    question = data.get("question")
    doc_id = data.get("doc_id")

    if not question or not doc_id:
        return jsonify({'error': 'Question and doc_id required'}), 400

    chunks = get_relevant_chunks(question, doc_id)
    if not chunks:
        return jsonify({'error': 'No relevant chunks found'}), 404

    prompt = build_prompt(chunks, question)
    answer = ask_bedrock(prompt)

    return jsonify({'answer': answer})

def build_prompt(chunks, question):
    context = "\n\n".join([f"- {chunk['metadata']['text']}" for chunk in chunks])
    return f"""Answer the following question using only the context below:

Context:
{context}

Question: {question}

Answer:"""