from fastapi import APIRouter, status


router = APIRouter(tags=["Health Check"])


@router.get("/")
async def root():
    """The root endpoint, just a greetings"""
    return {"message": "Welcome to this Assignment"}

@router.get("/health")
async def healthcheck():
    """The healthcheck endpoint returning 200 status code == OK"""
    return {"status": f"{status.HTTP_200_OK}_OK"}