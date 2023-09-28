import asyncpraw
from config import settings

from fastapi import FastAPI
import uvicorn

reddit = asyncpraw.Reddit(
    client_id=settings.REDDIT_CLIENT_ID,
    client_secret=settings.REDDIT_CLIENT_SECRET,
    user_agent=settings.REDDIT_USER_AGENT,
)

async def get_top_subreddits():
    top_subreddits = reddit.subreddits.popular(limit=5)

    subreddit_info = []
    async for subreddit in top_subreddits:
        subreddit_info.append({
            'name': subreddit.display_name,
            'subscribers': subreddit.subscribers
        })

    return subreddit_info


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/subreddits")
async def subreddits():
    return {"output": await get_top_subreddits()}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


