from fastapi import FastAPI

from app.routers import (
    category_router,
    tags_router,
    users_router,
    auth_router,
    posts_router
    profession_router,
    weather_router,
    lesson_router,

)
from app.exceptions import (
    zero_division_error_exc,
    AbrorSleepyException,
    Abror_sleepy_error_exc,
)
from app.admin.settings import admin

app = FastAPI(
    title="Chesnokdek achchiq yangiliklar",
    description="Chesnokuz - news website inspired from Qalampir.uz, built in FastAPI",
)

app.include_router(auth_router)
app.include_router(category_router)
app.include_router(tags_router)
app.include_router(users_router)
app.include_router(posts_router)
app.include_router(weather_router)
app.include_router(lesson_router)


app.add_exception_handler(ZeroDivisionError, zero_division_error_exc)
app.add_exception_handler(AbrorSleepyException, Abror_sleepy_error_exc)

admin.mount_to(app=app)