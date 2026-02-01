from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Post
from app.database import get_db
from app.schemas import PostListResponse, PostCreateRequest


router = APIRouter(prefix="/posts", tags=["Posts"])




@router.get("/")
async def get_posts(session: Session = Depends(get_db)):
    stmt = select(Post).order_by(Post.created_at.desc())
    res = session.execute(stmt)
    return res.scalars().all()


@router.post("")
async def post_create(
    create_data: PostCreateRequest, session: Session = Depends(get_db)
):
    post = Post(
    
@router.patch("/")
def user_patch(user_id: int, user_data):
    try:
        user = users_db[user_id]

        if user_data.name is not None:
         
        title=create_data.title,
        body=create_data.body
    )

    session.add(post)
    session.commit()
    session.refresh(post)

    return post



    
@router.put("/put/")
async def post_update(post_id: int, update_data: PostCreateRequest, session: Session = Depends(get_db),):
    stmt = select(Post).where(Post.id == post_id)
    res = session.execute(stmt)
    post = res.scalars().first()

    post.title = update_data.title
    post.body = update_data.body

    session.commit()
    session.refresh(post)

    return post

    

@router.delete("/delete/")
async def post_delete(post_id: int, session: Session = Depends(get_db),):
    stmt = select(Post).where(Post.id == post_id)
    res = session.execute(stmt)
    post = res.scalars().first()

    session.delete(post)
    session.commit()

    return {"detail": "Post o‘chirildi"}

    
@router.patch("/")
def user_patch(user_id: int, user_data):
    try:
        user = users_db[user_id]

        if user_data.name is not None:
            user["name"] = user_data.name

        if user_data.age is not None:
            user["age"] = user_data.age

        if user_data.is_active is not None:
            user["is_active"] = user_data.is_active

        users_db[user_id] = user
        return user

    except KeyError:
        return JSONResponse(
            content={"error": "User not found"},
            status_code=status.HTTP_404_NOT_FOUND
        )
    
@router.patch("/")
def user_patch(user_id: int, user_data):
    try:
        user = users_db[user_id]

        if user_data.name is not None:
            user["name"] = user_data.name

        if user_data.age is not None:
            user["age"] = user_data.age

        if user_data.is_active is not None:
            user["is_active"] = user_data.is_active

        users_db[user_id] = user
        return user

    except KeyError:
        return JSONResponse(
            content={"error": "User not found"},
            status_code=status.HTTP_404_NOT_FOUND
        )


