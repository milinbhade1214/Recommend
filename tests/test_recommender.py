import pytest
import pandas as pd
from pathlib import Path
from src.recommender import PopularityRecommender

# Fixture to create mock ratings
@pytest.fixture
def mock_ratings():
    data = {
        "userId": [1, 2, 3, 1, 2, 3, 4, 5],
        "movieId": [10, 20, 30, 10, 20, 30, 10, 10],
        "rating": [4, 5, 3, 5, 4, 4, 3, 5],
    }
    return pd.DataFrame(data)

def test_popularity_model_fit(mock_ratings):
    model = PopularityRecommender()
    model.fit(mock_ratings)
    assert model.popularity_scores is not None
    assert isinstance(model.popularity_scores, pd.Series)

def test_popularity_model_recommends_top_movies(mock_ratings):
    model = PopularityRecommender()
    model.fit(mock_ratings)
    recs = model.recommend(user_id=1, top_k=5)
    assert isinstance(recs, list)
    assert len(recs) == 5
    assert all(isinstance(m, int) for m in recs)

def test_recommendation_is_consistent(mock_ratings):
    model = PopularityRecommender()
    model.fit(mock_ratings)
    recs1 = model.recommend(user_id=1, top_k=3)
    recs2 = model.recommend(user_id=2, top_k=3)
    # Popularity-based model should return same recs regardless of user
    assert recs1 == recs2