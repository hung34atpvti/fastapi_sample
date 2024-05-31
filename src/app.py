from fastapi import FastAPI

from .controllers import blog_controller, user_controller, auth_controller
from .database.database import engine, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth_controller.router)
app.include_router(blog_controller.router)
app.include_router(user_controller.router)
