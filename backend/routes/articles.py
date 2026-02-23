from flask import Blueprint, request, json, current_app
from models import Article
from app import db
import os
from werkzeug.utils import secure_filename

articles_bp = Blueprint("aryicles", __name__)

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

# CREATE
@articles_bp.route("/articles", methods=["POST"])
def create_article():
    title = request.form.get("title")
    content = request.form.get("content")
    file = request.files.get("thumbnail")
    
    if not title or not content:
        return jsonify({"error": "Judul dan konten wajib diisi"}), 400
    
    thumbnail_filename = None
    if file and allowed_file(file.filename):
        file.save(os.path.join(current_app.config["UPLOAD_FOLDER"], filename))
        thumbnail_filename = filename