import os

class Config:
    # Database SQLite
    SQLALCHEMY_DATABASE_URI = "sqlite:///ashuraarticle.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # For save image
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), "uploads")
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024 # Max 16 MB