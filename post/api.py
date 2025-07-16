from ninja import Router
from post.schemas import PostSchema, PostCreateSchema
from post.models import Post
from ninja.pagination import paginate

router = Router()

@router.get("/", response=list[PostSchema])
@paginate
def get_posts(request):
    return Post.objects.all()

@router.post("/")
def create_post(request, post: PostCreateSchema):
    return Post.objects.create(**post.dict())