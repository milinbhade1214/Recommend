import sys
import os
from pathlib import Path

# Add src to the path
sys.path.append(str(Path(__file__).resolve().parents[1]/"src"))

from data_loader import load_ratings_data
from recommender import PopularityRecommender, UserCFRecommender


def main():
    # Load ratings data
    ratings_df = load_ratings_data()
    print(f"Loaded {len(ratings_df)} ratings")

    # Train model
    model = PopularityRecommender()
    print("Training Popularity Recommender...")
    model.fit(ratings_df)
    print("Training completed")

    # save model
    model_output_path = "../models/popular.pkl"
    os.makedirs(os.path.dirname(model_output_path), exist_ok=True)
    model.save(model_output_path)

    print(f"Model trained and saved to {model_output_path}")

if __name__ == "__main__":
    main()
