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