"""

from fastapi import APIRouter, HTTPException
from sqlalchemy import select

from app.models import User
from app.database import db_dep
from app.schemas import (
    UserCreateRequest,
    UserListResponse,
    UserUpdateRequest,
)
from app.utils import generate_slug


router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=list[UserListResponse])
async def get_posts(session: db_dep, is_active: bool = None):
    stmt = select(User)

    if is_active is not None:
        stmt = stmt.where(User.is_active == is_active)

    stmt = stmt.order_by(User.created_at.desc())
    res = session.execute(stmt)
    return res.scalars().all()


@router.get("/{slug}/", response_model=UserListResponse)
async def get_post(session: db_dep, slug: str):
    stmt = select(User).where(User.slug.like(f"%{slug}%"))
    res = session.execute(stmt)
    post = res.scalars().first()

    if not post:
        raise HTTPException(status_code=404, detail="User not found")

    return post


@router.post("/post/create/")
async def post_create(session: db_dep, create_data: UserCreateRequest):
    post = User(
        title=create_data.title,
        body=create_data.body,
        slug=generate_slug(create_data.title),
    )

    session.add(post)
    session.commit()
    session.refresh(post)

    return post


@router.put("/posts/")
async def post_update(session: db_dep, post_id: int, update_data: UserCreateRequest):
    stmt = select(User).where(User.id == post_id)
    res = session.execute(stmt)
    post = res.scalars().first()

    if not post:
        raise HTTPException(status_code=404, detail="User not found")

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
    session: db_dep, post_id: int, update_data: UserUpdateRequest
):
    stmt = select(User).where(User.id == post_id)
    res = session.execute(stmt)
    post = res.scalars().first()

    if not post:
        raise HTTPException(status_code=404, detail="User not found")

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
    stmt = select(User).where(User.id == post_id)
    res = session.execute(stmt)
    post = res.scalars().first()

    if not post:
        raise HTTPException(status_code=404, detail="User not found")

    session.delete(post)
    session.commit()

    """

from fastapi import APIRouter, HTTPException
from sqlalchemy import select

from app.database import db_dep
from app.models import User
from app.schemas import UserCreateRequest, UserResponse


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/profile/", response_model=UserResponse)
async def get_profile(db: db_dep, email: str):
    stmt = select(User).where(User.email == email)
    res = db.execute(stmt)
    user = res.scalars().first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User Not found")
    
    return user


@router.post("/create/", response_model=UserResponse)
async def users_create(db: db_dep, user_data: UserCreateRequest):
    new_user = User(
        email=user_data.email,
        password_hash=user_data.password
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user