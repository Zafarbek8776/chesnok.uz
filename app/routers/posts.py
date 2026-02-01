from time import time

from fastapi import APIRouter, HTTPException, UploadFile, File, Request, BackgroundTasks
from sqlalchemy import select, delete

from app.models import Post, post_tag_m2_table, Tag, Comment
from app.database import db_dep
from app.schemas import PostListResponse, PostCreateRequest, PostUpdateRequest
from app.utils import generate_slug


router = APIRouter(prefix="/posts", tags=["Posts"])


@router.get("/", response_model=list[PostListResponse])
async def get_posts(
    session: db_dep,
    tag_id: int | None = None,
    category_id: int | None = None,
    is_active: bool | None = None,
):
    stmt = select(Post)

    if tag_id:
        stmt = (
            stmt.join(post_tag_m2_table, Post.id == post_tag_m2_table.c.post_id)
            .join(Tag, post_tag_m2_table.c.tag_id == Tag.id)
            .where(Tag.id == tag_id)
        )

    if category_id:
        stmt = stmt.where(Post.category_id == category_id)

    if is_active is not None:
        stmt = stmt.where(Post.is_active == is_active)

    stmt = stmt.order_by(Post.created_at.desc())

    res = session.execute(stmt)
    return res.scalars().unique().all()


@router.get("/{slug}/", response_model=PostListResponse)
async def get_post(session: db_dep, slug: str):
    stmt = select(Post).where(Post.slug.like(f"%{slug}%"))
    res = session.execute(stmt)
    post = res.scalars().first()

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    return post


@router.post("/post/create/")
async def post_create(session: db_dep, create_data: PostCreateRequest):
    post = Post(
        title=create_data.title,
        body=create_data.body,
        slug=generate_slug(create_data.title),
    )

    session.add(post)
    session.commit()
    session.refresh(post)

    return post


@router.put("/posts/")
async def post_update(session: db_dep, post_id: int, update_data: PostUpdateRequest):
    stmt = select(Post).where(Post.id == post_id)
    res = session.execute(stmt)
    post = res.scalars().first()

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    if update_data.title:
        post.title = update_data.title
        post.slug = generate_slug(update_data.title)

    if update_data.body:
        post.body = update_data.body

    if update_data.is_active:
        post.is_active = update_data.is_active

    session.commit()
    session.refresh(post)

    return post


@router.patch("/posts/")
async def post_update_patch(
    session: db_dep, post_id: int, update_data: PostUpdateRequest
):
    stmt = select(Post).where(Post.id == post_id)
    res = session.execute(stmt)
    post = res.scalars().first()

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    if update_data.title:
        post.title = update_data.title
        post.slug = generate_slug(update_data.title)

    if update_data.body:
        post.body = update_data.body

    if update_data.is_active:
        post.is_active = update_data.is_active

    session.commit()
    session.refresh(post)

    return post


@router.delete("/posts/", status_code=204)
async def post_delete(session: db_dep, post_id: int):
    stmt = select(Post).where(Post.id == post_id)
    res = session.execute(stmt)
    post = res.scalars().first()

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    session.delete(post)
    session.commit()


@router.get("/trending/", response_model=list[PostListResponse])
async def trending_posts(session: db_dep, limit: int = 5):
    stmt = (
        select(Post)
        .where(Post.is_active == True)
        .order_by(Post.views.desc())
        .limit(limit)
    )

    res = session.execute(stmt)
    return res.scalars().all()


@router.get("/for-you/")
async def for_you_posts(session: db_dep):
    stmt = (
        select(Post)
        .where(Post.is_active == True)
        .order_by(Post.likes.desc(), Post.views.desc())
        .limit(10)
    )
    res = session.execute(stmt)

    return res.scalars().all()


@router.get("/weather/")
async def weather():
    return {"city": "Tashkent", "temp": "+12°C", "status": "Cloudy"}


@router.get("/search/")
async def search_posts(session: db_dep, q: str):
    stmt = select(Post).where(Post.title.ilike(f"%{q}%"))
    return session.execute(stmt).scalars().all()


@router.post("/{post_id}/like/")
async def like_post(session: db_dep, post_id: int):
    post = session.get(Post, post_id)
    if not post:
        raise HTTPException(404)
    post.likes += 1
    session.commit()
    return {"likes": post.likes}


@router.post("/")
async def create_post(session: db_dep, title: str, body: str):
    post = Post(title=title, body=body, slug=generate_slug(title))
    session.add(post)
    session.commit()

    return post


@router.post("/{post_id}/upload/")
async def upload_file(file: UploadFile = File()):
    return {"filename": file.filename}


@router.post("/{post_id}/comment/")
async def comment_post(session: db_dep, post_id: int, text: str):
    comment = Comment(post_id=post_id, body=text)
    session.add(comment)
    session.commit()

    return comment


async def response_time_middleware(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    response.headers["X-Response-Time"] = str(time.time() - start)
    return response


REQUESTS = {}


async def rate_limiter(ip: str):
    now = int(time())
    REQUESTS.setdefault(ip, [])
    REQUESTS[ip] = [t for t in REQUESTS[ip] if now - t < 60]

    if len(REQUESTS[ip]) > 60:
        raise HTTPException(429, "Too many requests")

    REQUESTS[ip].append(now)


@router.delete("/cleanup/trash/")
async def delete_trash_comments(session: db_dep, background: BackgroundTasks):
    def task():
        stmt = delete(Comment).where(Comment.is_trash == True)
        session.execute(stmt)
        session.commit()

    background.add_task(task)
    return {"status": "cleanup started"}