from app.database import SessionLocal
from app.models import User, Post, Comment, Category, Tag, Profession, Media

db = SessionLocal()

for i in range(10):
    db.add(Profession(name=f"Profession {i}"))
db.commit()

for i in range(20):
    db.add(
        User(
            email=f"user{i}@mail.com",
            password_hash="123456",
            first_name=f"User{i}",
            profession_id=(i % 10) + 1,
        )
    )
db.commit()

for i in range(10):
    db.add(Category(name=f"Category {i}", slug=f"category-{i}"))
db.commit()

for i in range(10):
    db.add(Tag(name=f"Tag {i}", slug=f"tag-{i}"))
db.commit()

for i in range(20):
    db.add(
        Post(
            user_id=(i % 20) + 1,
            title=f"Post {i}",
            slug=f"post-{i}",
            body="Test post body",
            category_id=(i % 10) + 1,
            is_active=True,
        )
    )
db.commit()

for i in range(20):
    db.add(
        Comment(
            user_id=(i % 20) + 1,
            text=f"Comment {i}",
            is_active=True,
        )
    )
db.commit()

for i in range(10):
    db.add(Media(url=f"https://example.com/media/{i}.jpg"))
db.commit()

db.close()
print("Seed finished")