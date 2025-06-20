from flask import Flask
from flask_cors import CORS
from app.routes.upload import upload_bp
from app.routes.query import query_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(upload_bp, url_prefix="/api")
app.register_blueprint(query_bp, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)
