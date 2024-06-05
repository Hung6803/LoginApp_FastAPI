from fastapi import FastAPI
from login_app.user import router as user_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Login App")

origins = [
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(user_router.router)


