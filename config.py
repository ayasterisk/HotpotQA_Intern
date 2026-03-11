import os
from dotenv import load_dotenv

load_dotenv()

NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USERNAME = os.getenv("NEO4J_USERNAME")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")
NEO4J_DATABASE = os.getenv("NEO4J_DATABASE")

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

DATA_PATH = "hotpot_mini_1k"

EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"