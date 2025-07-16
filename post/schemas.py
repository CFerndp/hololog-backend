from datetime import datetime
from ninja import Field, Schema
from typing import Dict, Any

class PostSchema(Schema):
    id: int
    title: str
    content: str
    created_at: datetime
    updated_at: datetime
    
class PostCreateSchema(Schema):
    title: str
    content: Dict[str, Any] = Field (
        description="Any valid JSON content. Can be used with rich text editors like Draft.js",
        example={
            "blocks": [
                {
                    "key": "foo",
                    "text": "Example content",
                    "type": "unstyled"
                }
            ]
        }
    )
    