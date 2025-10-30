from fastapi import APIRouter, status, Response, Request


router = APIRouter(tags=["Cookies"])


@router.post("/set-cookie")
def set_cookie(response: Response):  # pragma: no cover
    """setting a custome cookie showcasing cookies mnanagement"""
    response.set_cookie(key="test", value="something")
    return {"message": "Cookie has been set successfully"}


@router.get("/get-cookie")
def get_cookie(request: Request):  # pragma: no cover
    """Getting cookies"""
    return {"requested cookie": request.cookies.get("test")}