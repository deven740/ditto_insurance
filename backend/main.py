from fastapi import FastAPI
from policy import policy
from fastapi_pagination import add_pagination

app = FastAPI()

add_pagination(app)

app.include_router(policy.router)
