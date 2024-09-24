from fastapi import FastAPI

app = FastAPI()

app.username = ""


@app.get("/")
async def home():
    return f"Welcome home, {app.username}."


@app.post("/login")
async def login(username):
    app.username = username


@app.get("/login")
async def login():
    return f"{app.username} is presently logged in."


@app.delete("/reset")
def reset():
    app.username = ""
