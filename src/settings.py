import os

from dotenv import load_dotenv

from src.common.ext import parse_host

load_dotenv(".env.local")

HOST = parse_host(os.getenv("HOST", "0.0.0.0"))
PORT = int(os.getenv("PORT", 8000))
