import logging
from fastapi import Request

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

async def log_requests(request: Request, call_next):
    response = await call_next(request)
    logging.info(
        f"{request.method} {request.url} - {response.status_code}"
    )
    return response
