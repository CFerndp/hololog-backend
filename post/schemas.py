from datetime import datetime
from ninja import Schema

class PostSchema(Schema):
    id: int
    title: str
    content: str
    created_at: datetime
    updated_at: datetime