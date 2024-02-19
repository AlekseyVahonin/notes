from datetime import datetime


class Note:
    current_id = 1

    def __init__(self, title, body):
        self.id = Note.current_id
        self.title = title
        self.body = body
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        Note.current_id += 1

    def update(self, title, body):
        if not title:
            self.title = self.title
        else:
            self.title = title
        if not body:
            self.body = self.body
        else:
            self.body = body
        self.updated_at = datetime.now()

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "body": self.body,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
