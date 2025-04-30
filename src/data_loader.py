import pandas as pd
import numpy as np
from pathlib import Path

# Set base directory relative to project root
BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data" / "ml-latest-small"
PROCESSED_DIR = BASE_DIR / "data" / "processed"

# Data path
ratings_path = DATA_DIR / "ratings.csv"
movies_path = DATA_DIR / "movies.csv"
output_path = PROCESSED_DIR / "ratings_clean.csv"

def load_raw_data():
    movies_df = pd.read_csv(movies_path)
    ratings_df = pd.read_csv(ratings_path)
    return movies_df, ratings_df


'''
Join on movieId

Drop timestamp

Encode userId and movieId into dense ints

Optional: parse genres (multi-hot or simple string split)

Save the final DataFrame to data/processed/ratings_clean.csv
'''
def preprocess(path):
    # Load the raw data
    movies_df, ratings_df = load_raw_data()

    # Merge the dataframes on movieID
    merged_df = pd.merge(ratings_df, movies_df, on="movieId")

    # Drop the timestamp column
    merged_df.drop(columns=["timestamp"], inplace=True)

    # Encode userId and movieId into dense ints
    merged_df["userId"] = pd.factorize(merged_df["userId"])[0]
    merged_df["movieId"] = pd.factorize(merged_df["movieId"])[0]

    # Parse genres (optional)
    merged_df["genres"] = merged_df["genres"].apply(lambda x: x.split("|"))
    merged_df["genres"] = merged_df["genres"].apply(lambda x: [genre.strip() for genre in x])
    merged_df["genres"] = merged_df["genres"].apply(lambda x: ", ".join(x))

    # Save the final DataFrame to data/processed/ratings_clean.csv
    merged_df.to_csv(output_path, index=False)


if __name__ == "__main__":
    # Create processed directory if it doesn't exist
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    # Preprocess the data
    preprocess(output_path)
    print(f"Preprocessed data saved to {output_path}")




