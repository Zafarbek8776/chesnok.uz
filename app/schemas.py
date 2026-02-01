from datetime import datetime
from pydantic import BaseModel


class PostCreateRequest(BaseModel):
    user_id: int
    category_id: int
    title: str
    body: str
    created_at: datetime | None = None


class PostUpdateRequest(BaseModel):
    user_id: int | None = None
    title: str | None = None
    body: str | None = None
    is_active: bool | None = None


class PostListResponse(BaseModel):
    id: int
    title: str
    slug: str
    body: str
    is_active: bool
    created_at: datetime

    model_config = {
        "from_attributes": True,
        "json_schema_extra": {
            "examples": [
                {
                    "id": 6,
                    "title": "O'zbekistonning YaIM si 130 mlrddan oshdi.",
                    "slug": "ozbekistonning-yaim-si-130-mlrddan-oshdi",
                    "body": "O'zbekiston Markaziy Osiyodagi eng kuchli davlat boldi",
                    "is_active": True,
                    "created_at": "2026-01-19T13:01:18.001Z",
                }
            ]
        },
    }


class CategoryListResponse(BaseModel):
    id: int
    title: str
    slug: str
    body: str
    is_active: bool
    created_at: datetime

    model_config = {
        "from_attributes": True,
        "json_schema_extra": {
            "examples": [
                {
                    "id": 2,
                    "title": "Siyosat",
                    "slug": "siyosat",
                    "body": "Siyosiy yangiliklar",
                    "is_active": True,
                    "created_at": "2026-01-18T11:00:00.000Z",
                }
            ]
        },
    }


class CategoryCreateRequest(BaseModel):
    title: str | None = None
    body: str | None = None
    name: str | None = None
    slug: str | None = None


class CategoryUpdateRequest(BaseModel):
    title: str | None = None
    name: str | None = None
    slug: str | None = None


class TagListResponse(BaseModel):
    id: int
    title: str
    slug: str
    body: str
    is_active: bool
    created_at: datetime

    model_config = {
        "from_attributes": True,
        "json_schema_extra": {
            "examples": [
                {
                    "id": 5,
                    "title": "FastAPI",
                    "slug": "fastapi",
                    "body": "Backend texnologiya",
                    "is_active": True,
                    "created_at": "2026-01-17T09:30:00.000Z",
                }
            ]
        },
    }


class TagCreateRequest(BaseModel):
    name: str | None = None


class TagUpdateRequest(BaseModel):
    title: str | None = None
    body: str | None = None


class UserListResponse(BaseModel):
    id: int
    title: str
    slug: str
    body: str
    is_active: bool
    created_at: datetime

    model_config = {
        "from_attributes": True,
        "json_schema_extra": {
            "examples": [
                {
                    "id": 5,
                    "title": "FastAPI",
                    "slug": "fastapi",
                    "body": "Backend texnologiya",
                    "is_active": True,
                    "created_at": "2026-01-17T09:30:00.000Z",
                }
            ]
        },
    }


class UserCreateRequest(BaseModel):
    name: str | None = None
    title: str | None = None
    body: str | None = None


class UserUpdateRequest(BaseModel):
    title: str | None = None
    body: str | None = None


class PostCreate(BaseModel):
    title: str
    body: str

    model_config = {"from_attributes": True}


class PostResponse(BaseModel):
    id: int
    title: str
    body: str
    is_active: bool
    created_at: datetime

    model_config = {"from_attributes": True}

