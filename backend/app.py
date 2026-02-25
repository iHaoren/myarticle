from flask import Flask, send_from_directory
from flask_cors import CORS
from config import Config
from extension import db
import os


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # inisialisasi extension
    db.init_app(app)
    CORS(app)  # mengizinkan react untuk akses backend

    # Daftarkan routes
    @app.route("/uploads/<filename>")
    def uploaded_file(filename):
        return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

    # buat tabel database otomatis
    with app.app_context():
        db.create_all()

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
