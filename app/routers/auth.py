'''

from fastapi import APIRouter, Response, Cookie

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login/")
async def login(response: Response):
    response.set_cookie(
        key="access_token",
        value="fake-token",
        httponly=True,
        max_age=100,
    )
    return {"login": True}


@router.get("/me/")
async def me(access_token: str | None = Cookie(default=None)):
    return {"token": access_token}


@router.post("/logout/")
async def logout(response: Response):
    response.delete_cookie("access_token")
    return {"logout": True}


@router.get("/check/")
async def check_auth(access_token: str | None = Cookie(default=None)):
    return {"authenticated": bool(access_token)}


@router.post("/refresh/")
async def refresh(response: Response):
    response.set_cookie(
        key="access_token",
        value="new-token",
        httponly=True,
        max_age=100,
    )
    return {"refresh": True}

    '''

""""
from datetime import datetime

from pydantic import BaseModel, EmailStr, model_validator
from zxcvbn import zxcvbn


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

        if zxcvbn(self.password) and zxcvbn(self.password)["score"] < 4:
            raise ValueError("password is weak")
        return self


class UserLoginRequest(BaseModel):
    email: EmailStr
    password: str


"""
Before -> validation process -> after
"""


class UserRegisterResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime


class UserProfileResponse(BaseModel):
    id: int
    email: EmailStr
    first_name: str | None = None
    last_name: str | None = None
    bio: str | None = None

    """


from datetime import datetime

from pydantic import BaseModel, EmailStr, model_validator
from zxcvbn import zxcvbn

from app.schemas.common import ProfessionInline

class UserRegisterRequest(BaseModel):
    email: Emailstr
    password: str
    password2: str

    @model_validator(mode="after")
    def check_passwords_match(self) -> "UserRegisterRequest":
        if self.password != self.password2:
            raise ValueError("passwords do not match")
        
        if len(self.password) < 8:
            raise ValueError("password must be at least 8 characters long")
        
        if zxcvbn(self.password) and zxcvbn(self.password) ["score"] < 2:
            raise ValueError("password is weak")
        return self
    

    class UserLoginRequest(BaseModel):
        email: EmailStr
        password: str


        """
        
        Before -> validation process -> after

        """

        class UserRegisterResponse(BaseModel):
            id: int 
            email: EmailStr
            created_at: datetime


        class UserProfilResponse(BaseModel):
            id: int
            email: Emailstr
            first_name: str | None = None 
            last_name: str  | None = None
            bio: str  | None = None 
            posts_count: int
            posts_read_count: int
            profession: ProfessionInline  | None = None 
            is_active: bool
            is_staff: bool
            is_superuser: bool
            is_deleted: bool


        class UserProfilUpdateRequest(BaseModel):
            first_name: str | None = None 
            last_name: str  | None = None 
            bio: str  | None = None 
            profession_id: int 

    



    
