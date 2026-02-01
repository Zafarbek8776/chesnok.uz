from fastapi import FastAPI,Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from app.database import get_db
from app.models import Post
from app.utils import generate_slug
from app.schemas import PostCreateRequest, PostListResponse
from app.routers import posts_router


app = FastAPI(
    title="Chesnokdek achchiq yangiliklar",
    description="Chesnokuz - news website inspired from Qalampir.uz, built in FastAPI",
)

app.include_router(posts_router)



@app.get("/posts/")
async def get_posts(session: Session = Depends(get_db)):
    stmt = select(Post).order_by(Post.created_at.desc())
    res = session.execute(stmt)
    return res.scalars().all()


@app.post("/post/create/")
async def post_create(
    create_data: PostCreateRequest, session: Session = Depends(get_db)
):
    post = Post(
        title=create_data.title,
        body=create_data.body,
        slug=generate_slug(create_data.title),
    )

    session.add(post)
    session.commit()
    session.refresh(post)

    return post



@app.put("/posts/{post_id}/")
def user_update(user_id: int):
    try:
        user = users_db[user_id]
        user["name"] = generate_random_string(10)
        user["age"] = random.randint(1, 60)
        users_db[user_id] = user

        return user
    except KeyError:
        return JSONResponse(
            content={"error": "User not found"}, status_code=status.HTTP_404_NOT_FOUND
        )
    
@app.put("/users/{user_id}2/")
def user_update(user_id: int):
    try:
        user = users_db[user_id]
        user["name"] = generate_random_string(10)
        user["age"] = random.randint(1, 60)
        users_db[user_id] = user

        return user
    except KeyError:
        return JSONResponse(
            content={"error": "User not found"}, status_code=status.HTTP_404_NOT_FOUND
        )
    
@app.put("/users/{user_id}3/")
def user_update(user_id: int):
    try:
        user = users_db[user_id]
        user["name"] = generate_random_string(10)
        user["age"] = random.randint(1, 60)
        users_db[user_id] = user

        return user
    except KeyError:
        return JSONResponse(
            content={"error": "User not found"}, status_code=status.HTTP_404_NOT_FOUND
        )
    

    @app.delete("/users/{user_id}/")
def user_delete(user_id: int):
    try:
        del users_db[user_id]
        return JSONResponse(status_code=204)
    except KeyError:
        return JSONResponse(
            content={"error": "User not found"}, status_code=status.HTTP_404_NOT_FOUND
        )
    
    @app.patch("/users/{user_id}/")
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
    
@app.patch("/users/{user_id}2/")
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




    
    

    
    