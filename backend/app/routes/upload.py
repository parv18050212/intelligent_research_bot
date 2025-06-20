from flask import Blueprint, request, jsonify
import os
import uuid
from app.services.pdf_parser import extract_text_from_pdf
from app.services.chunker import split_text
from app.services.embedder import embed_chunks

upload_bp = Blueprint('upload', __name__)

@upload_bp.route('/upload', methods=['POST'])
def upload_pdf():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    filename = file.filename
    path = os.path.join("temp", filename)
    os.makedirs("temp", exist_ok=True)
    file.save(path)

    text = extract_text_from_pdf(path)
    chunks = split_text(text)
    doc_id = str(uuid.uuid4())
    count = embed_chunks(chunks, doc_id)

    return jsonify({
        'message': f"{count} chunks indexed successfully.",
        'doc_id': doc_id
    })