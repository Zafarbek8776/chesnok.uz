from fastapi import APIRouter, HTTPException
from sqlalchemy import select

from app.models import Category
from app.database import db_dep
from app.schemas import (
    CategoryListResponse,
    CategoryCreateRequest,
    CategoryUpdateRequest,
)
from app.utils import generate_slug


router = APIRouter(prefix="/categories", tags=["Categories"])


@router.get("/", response_model=list[CategoryListResponse])
async def get_posts(session: db_dep, is_active: bool = None):
    stmt = select(Category)

    if is_active is not None:
        stmt = stmt.where(Category.is_active == is_active)

    stmt = stmt.order_by(Category.created_at.desc())
    res = session.execute(stmt)
    return res.scalars().all()


@router.get("/{slug}/", response_model=CategoryListResponse)
async def get_post(session: db_dep, slug: str):
    stmt = select(Category).where(Category.slug.like(f"%{slug}%"))
    res = session.execute(stmt)
    post = res.scalars().first()

    if not post:
        raise HTTPException(status_code=404, detail="Category not found")

    return post


@router.post("/post/create/")
async def post_create(session: db_dep, create_data: CategoryCreateRequest):
    post = Category(
        title=create_data.title,
        body=create_data.body,
        slug=generate_slug(create_data.title),
    )

    session.add(post)
    session.commit()
    session.refresh(post)

    return post


@router.put("/posts/")
async def post_update(
    session: db_dep, post_id: int, update_data: CategoryUpdateRequest
):
    stmt = select(Category).where(Category.id == post_id)
    res = session.execute(stmt)
    post = res.scalars().first()

    if not post:
        raise HTTPException(status_code=404, detail="Category not found")

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
    session: db_dep, post_id: int, update_data: CategoryUpdateRequest
):
    stmt = select(Category).where(Category.id == post_id)
    res = session.execute(stmt)
    post = res.scalars().first()

    if not post:
        raise HTTPException(status_code=404, detail="Category not found")

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
    stmt = select(Category).where(Category.id == post_id)
    res = session.execute(stmt)
    post = res.scalars().first()

    if not post:
        raise HTTPException(status_code=404, detail="Category not found")

    session.delete(post)
    session.commit()