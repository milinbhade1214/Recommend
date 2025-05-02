from fastapi import FastAPI, HTTPException, Request

def setup_routes(app: FastAPI, model):
    @app.get("/recommend")
    def recommend(user_id: int, k: int = 5):
        try:
            recommendations = model.recommend(user_id, top_k=k)
            return {"recommended_movie_ids": recommendations}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))