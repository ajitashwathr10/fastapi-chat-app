from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .router import auth, chat, group, file

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth")
app.include_router(chat.router, prefix="/chat")
app.include_router(group.router, prefix="/group")
app.include_router(file.router, prefix="/file")

@app.get("/")
async def root():
    return {"message": "Welcome to the chat application!"}
