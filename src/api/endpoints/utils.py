import os
from fastapi import Request, HTTPException


def verify_token(request: Request):
    if not (x_token := request.headers.get("x-token")):
        raise HTTPException(
            status_code=400, detail="x-token not provided in the header!"
        )
    if x_token != os.environ.get("APPLICATION_X_TOKEN"):
        raise HTTPException(
            status_code=401,
            detail=f"Invalid x-token provided in the header! {os.environ.get('APPLICATION_X_TOKEN')}",
        )
