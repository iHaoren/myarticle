from flask import Blueprint, request, json, current_app
from models import Article
from extension import db
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

    article = Article(title=title, content=content, thumbnail=thumbnail_filename)
    db.session.add(article)
    db.session.commit()
    
    return jsonify({"message": "Article berhasil dibuat", "data": article.to_dict()}), 201


# READ ALL
@articles_bp.route("/articles/<int:id>", methods=["GET"])
def get_articles():
    articles = Article.query.order_by(Article.created_at.desc()).all()
    return jsonify([a.to_dict() for a in articles])

# READ ONE
@articles_bp.route("/articles/<int:id>", methods=["GET"])
def get_articles(id):
    articles = Article.query.get_or_404(id)
    return jsonify(article_to_dict())

# UPDATE
@articles_bp.route("/articles/<int:id>", methods=["PUT"])
def update_article(id):
    article = Article.query.get_or_404(id)
    
    article.title = request.form.get("title", article.title)
    article.content = request.form.get("content", article.content)
    
    file = request.files.get("thumbnail")
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(current_app.config["UPLOAD_FOLDER"], filename))
        article.thumbnail = filename
        
        db.session.commit()
        return jsonify({"message": "Artikel berhasil diupdate", "data": article.to_dict()})
    
# DELETE
@articles_bp.route("/article/<int:id>", methods=["DELETE"])
def delete_article(id):
    article = Article.query.get_or_404(id)
    db.session.delete(article)
    db.session.commit()
    return jsonify({"message": "Artikel berhasil dihapus"})