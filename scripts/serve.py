import sys
from pathlib import Path


# Add src to the Python path
sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from fastapi import FastAPI
from src.api import setup_routes
from src.recommender import PopularityRecommender


app = FastAPI()

# Load model
model_path = Path("models/popular.pkl")
if not model_path.exists():
    raise FileNotFoundError(f"Trained model not found at {model_path}")

model = PopularityRecommender.load(model_path)

# Setup routes
setup_routes(app, model)