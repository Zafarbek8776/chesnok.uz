
"""

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

    """


from datetime import datetime

from pydantic import BaseModel, EmailStr, model_validator


class PostCreateRequest(BaseModel):
    title: str
    body: str


class PostListResponse(BaseModel):
    id: int
    title: str
    slug: str
    body: str
    is_active: bool
    created_at: datetime

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 6,
                    "title": "O'zbekistonning YaIM si 130 mlrddan oshdi.",
                    "slug": "ozbekistonning-yaim-si-130-mlrddan-oshdi",
                    "body": "O'zbekiston Markaziy Osiyodagi eng kuchli davlat boldi",
                    "is_active": True,
                    "created_at": "2026-19-01T13:01:18.001Z",
                }
            ]
        }
    }


class PostUpdateRequest(BaseModel):
    title: str | None = None
    body: str | None = None
    is_active: bool | None = None


class TagCreateRequest(BaseModel):
    name: str
    slug: str


class TagUpdateRequest(BaseModel):
    name: str | None = None


class TagListResponse(BaseModel):
    id: int
    name: str
    slug: str


class CategoryListResonse(BaseModel):
    id: int | None = None
    name: str | None = None


class CategoryCreateRequest(BaseModel):
    name: str | None = None


class ProfessionCreateRequest(BaseModel):
    name: str


class ProfessionListResponse(BaseModel):
    id: int
    name: str


class ProfessionUpdateRequest(BaseModel):
    name: str


class WeatherCoord(BaseModel):
    lon: float
    lat: float


class WeatherInline(BaseModel):
    id: int
    main: str
    description: str
    icon: str


class WeatherMainInline(BaseModel):
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    humidity: int
    sea_level: int
    grnd_level: int


class WeatherResponse(BaseModel):
    coord: WeatherCoord
    weather: list[WeatherInline]
    # base: str
    # main: WeatherMainInline
    # visibility: int
    # wind: dict[str, float] | None = None
    # rain: dict[str, float] | None = None
    # clouds: dict[str, int] | None = None
    # dt: int
    # sys: dict[str, int | str] | None = None
    # timezone: int
    # id: int
    # name: str
    # cod: int

class ProfessionInline(BaseModel):
    id: int
    name: str

class UserCreateRequest(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    first_name: str | None = None
    last_name: str | None = None


class RefreshTokenRequest(BaseModel):
    refresh_token: str


class UserLoginRequest(BaseModel):
    email: EmailStr
    password: str


class UserProfileResponse(BaseModel):
    id: int
    email: EmailStr
    first_name: str | None = None
    last_name: str  | None = None
    bio: str | None = None
    posts_count: int
    posts_read_count: int
    profession: ProfessionInline  | None = None 
    is_active: bool
    is_staff: bool
    is_superuser: bool
    is_deleted: bool


class UserRegisterRequest(BaseModel):
    email: EmailStr
    password: str
    password2: str

    @model_validator(mode="after")
    def check_passwords_match(self) -> "UserRegisterRequest":
        if self.password != self.password2:
            raise ValueError("passwords do not match")

        if len(self.password) < 8:
            raise ValueError("password must be at least 8 characters long")

        return self