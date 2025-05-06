import os
from dotenv import load_dotenv
import cloudinary

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
load_dotenv(dotenv_path=os.path.join(BASE_DIR, ".env"))

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
STATIC_DIR = os.path.join("static_image")

cloudinary.config(
    cloud_name = os.getenv("CLOUDINARY_IMAGE_CLOUD_NAME"),
    api_key = os.getenv("CLOUDINARY_IMAGE_API_KEY"),
    api_secret = os.getenv("CLOUDINARY_IMAGE_API_SECRET"),
    secure=True
)