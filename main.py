import os

import uvicorn
from dotenv import load_dotenv

load_dotenv()

host = os.getenv("HOST", "127.0.0.1")
port = int(os.getenv("PORT", 3000))
workers = int(os.getenv("WORKERS", 1))
reload = os.getenv("RELOAD", "False").lower() in ("true", "1", "t")

if __name__ == "__main__":
    uvicorn.run("src.app:app", host=host, port=port, reload=reload, workers=workers)
