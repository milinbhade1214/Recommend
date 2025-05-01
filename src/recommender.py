import numpy as np
import pandas as pd
import pickle



class BaseRecommender:
    def fit(self, rating_df: pd.DataFrame):
        raise NotImplementedError
    
    def recommend(self, user_id: int, top_k: int=10) -> list:
        raise NotImplementedError
    
    def save(self, filepath: str):
        with open(filepath, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def load(cls, filepath: str):
        with open(filepath, 'rb') as f:
            return pickle.load(f)
        

class PopularityRecommender(BaseRecommender):
    def fit(self, ratings_df: pd.DataFrame):
        self.popular_movies = (
            ratings_df.groupby('movieId')['rating'].count()
            .sort_values(ascending=False)
        )
    
    def recommend(self, user_id, top_k = 10):
        return self.popular_movies.head(top_k).index.tolist()
    
class UserCFRecommender(BaseRecommender):
    def fit(self, ratings_df: pd.DataFrame):
        # Build user-user similarity matrix
        pass

    def recommend(self, user_id: int, top_k : int = 10) -> list:
        # Return recommendations for this user
        pass