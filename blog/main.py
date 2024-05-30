from fastapi import FastAPI

from blog.database.database import engine, Base
from .controllers import blog_controller, user_controller

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(blog_controller.router)
app.include_router(user_controller.router)
