"""Simple Python backend with FastAPI showcasing DevOps skills"""

from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as Excp
from app.health_service.routes import router as health
from app.cookies.routes import router as cookies

tags_metadata = [
    {
        "name": "Vital Signs Assignment",
        "description": "Simple backend with FastAPI.",
        "externalDocs": {
            "description": "Building backend using FastAPI easier than ever!",
            "url": "https://github.com/DevSepOps",
        },
    }
]


@asynccontextmanager
async def lifespan(fastapi_app: FastAPI):  # pragma: no cover
    """Simple lifespan without auto-migration due to not having a Database"""
    print(f"🎯 {fastapi_app.title} is started")
    yield
    print("🛑 Application shutting down...")


app = FastAPI(
    lifespan=lifespan,
    openapi_tags=tags_metadata,
    title="Vital Signs Assignment",
    description="Simple backend application with FastAPI",
    summary="Healthcheck endpoint and code testing using pytest",
    version="1.0.0",
    contact={
        "name": "Sepehr Maadani",
        "url": "https://github.com/sepehrmdn77",
        "email": "sepehrmaadani98@gmail.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://choosealicense.com/",
    },
)


app.include_router(health)
app.include_router(cookies)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(Excp)
async def http_exception_handler(request: Request, exc: Excp):
    """Defining the desired exception handler"""
    print(f"HTTPException occurred: {exc.status_code} - {exc.detail}")
    error_response = {
        "error": True,
        "status_code": exc.status_code,
        "detail": exc.detail,
        "path": request.url.path,
    }
    return JSONResponse(status_code=exc.status_code, content=error_response)
