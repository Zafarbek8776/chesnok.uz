"""

from fastapi import APIRouter, HTTPException
from sqlalchemy import select

from app.models import Tag
from app.database import db_dep
from app.schemas import TagListResponse, TagCreateRequest, TagUpdateRequest
from app.utils import generate_slug


router = APIRouter(prefix="/tags", tags=["Tags"])


@router.get("/", response_model=list[TagListResponse])
async def get_posts(session: db_dep, is_active: bool = None):
    stmt = select(Tag)

    if is_active is not None:
        stmt = stmt.where(Tag.is_active == is_active)

    stmt = stmt.order_by(Tag.created_at.desc())
    res = session.execute(stmt)
    return res.scalars().all()


@router.get("/{slug}/", response_model=TagListResponse)
async def get_post(session: db_dep, slug: str):
    stmt = select(Tag).where(Tag.slug.like(f"%{slug}%"))
    res = session.execute(stmt)
    post = res.scalars().first()

    if not post:
        raise HTTPException(status_code=404, detail="Tag not found")

    return post


@router.post("/post/create/")
async def post_create(session: db_dep, create_data: TagCreateRequest):
    post = Tag(
        title=create_data.title,
        body=create_data.body,
        slug=generate_slug(create_data.title),
    )

    session.add(post)
    session.commit()
    session.refresh(post)

    return post


@router.put("/posts/")
async def post_update(session: db_dep, post_id: int, update_data: TagUpdateRequest):
    stmt = select(Tag).where(Tag.id == post_id)
    res = session.execute(stmt)
    post = res.scalars().first()

    if not post:
        raise HTTPException(status_code=404, detail="Tag not found")

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
    session: db_dep, post_id: int, update_data: TagUpdateRequest
):
    stmt = select(Tag).where(Tag.id == post_id)
    res = session.execute(stmt)
    post = res.scalars().first()

    if not post:
        raise HTTPException(status_code=404, detail="Tag not found")

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
    stmt = select(Tag).where(Tag.id == post_id)
    res = session.execute(stmt)
    post = res.scalars().first()

    if not post:
        raise HTTPException(status_code=404, detail="Tag not found")

    session.delete(post)
    session.commit()
    
    """

from fastapi import APIRouter, HTTPException
from sqlalchemy import select

from app.models import Tag
from app.database import db_dep
from app.schemas import TagCreateRequest, TagListResponse, TagUpdateRequest
from app.utils import generate_slug

router = APIRouter(prefix="/tag", tags=["Tag"])


@router.get("/{slug}", response_model=TagListResponse)
async def get_tag(session: db_dep, slug: str):
    stmt = select(Tag).where(Tag.slug.like(f"%{slug}%"))
    res = session.execute(stmt)
    tag = res.scalar().first()

    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")

    return tag


@router.post("/create/", response_model=TagCreateRequest)
async def tag_create(session: db_dep, create_data: TagCreateRequest):
    tag = Tag(
        name=create_data.name,
        slug=generate_slug(create_data.name),
    )

    session.add(tag)
    session.commit()
    session.refresh(tag)

    return tag


@router.put("{tag_id}", response_model=TagUpdateRequest)
async def tag_update_put(session: db_dep, tag_id: int, update_data: TagUpdateRequest):
    stmt = select(Tag).where(Tag.id == tag_id)
    res = session.execute(stmt)
    tag = res.scalar().first()

    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")

    tag.name = update_data.name
    tag.slug = generate_slug(update_data.name)

    session.commit()
    session.refresh(tag)

    return tag


@router.patch("{tag_id}", response_model=TagUpdateRequest)
async def tag_update_patch(session: db_dep, tag_id: int, update_data: TagUpdateRequest):
    stmt = select(Tag).where(Tag.id == tag_id)
    res = session.execute(stmt)
    tag = res.scalar().first()

    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")

    tag.name = update_data.name
    tag.slug = generate_slug(update_data.name)

    session.commit()
    session.refresh(tag)

    return tag


@router.delete("{tag_id}")
async def delete_tag(session: db_dep, tag_id: int):
    stmt = select(Tag).where(Tag.id == tag_id)
    res = session.execute(stmt)
    tag = res.scalar().first()

    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")

    session.delete(tag)
    session.commit()