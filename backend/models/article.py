from extension import db
from datetime import datetime

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False) # Judul artikel
    content = db.Column(db.Text, nullable=False) # Isi artikel
    thumbnail = db.Column(db.String(300), nullable=True) # Nama file gambar
    created_at = db.Column(db.DateTime, default=datetime.utcnow) # Waktu dibuat
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "thumbnail": self.thumbnail,
            "created_at": self.created_at.strftime("%d %B %Y")
        }