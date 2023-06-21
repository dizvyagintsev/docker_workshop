from fastapi import FastAPI
from redis import Redis

app = FastAPI()
redis_client = Redis(host='redis', port=6379)


@app.get("/ping_redis")
def ping_redis():
    # raise ValueError

    try:
        redis_status = redis_client.ping()
        if redis_status:
            return {"message": "Redis is up and running!"}
        else:
            return {"message": "Failed to ping Redis server."}
    except Exception as e:
        return {"message": f"Error: {str(e)}"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
