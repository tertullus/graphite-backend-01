from fastapi import FastAPI
import json
import cloudinary.api
import cloudinary.uploader
from cloudinary import CloudinaryImage
import cloudinary
from dotenv import load_dotenv
load_dotenv()

config = cloudinary.config(secure=True)

app = FastAPI()

app.username = ""
app.image_url = ""


@app.get("/")
async def home():
    return f"Welcome, {app.username}. Here's the image URL: {app.image_url}"


@app.post("/login")
async def login(username):
    app.username = username


@app.get("/login")
async def login():
    return f"{app.username} is presently logged in."


@app.delete("/reset")
async def reset():
    app.username = ""


@app.post("/upload")
async def upload_image():
    cloudinary.uploader.upload(
        "me.jpg", public_id="me", unique_filename=False, overwrite=True)
    app.image_url = CloudinaryImage("me").build_url()
    return f"The image URL: {app.image_url}"
