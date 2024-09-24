from fastapi import FastAPI

app = FastAPI()

app.username = "Chideraa"


@app.get("/")
async def home():
    return f"Welcome home, {app.username}."


@app.get("/login")
async def login(username):
    app.username = username
    return f"{app.username} is presently logged in."


@app.delete("/reset")
async def reset():
    app.username = ""
