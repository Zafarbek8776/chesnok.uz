from fastapi.requests import Request
from fastapi.responses import JSONResponse
from fastapi import status


class AbrorSleepyException(Exception):
    def __init__(self, msg):



async def zero_division_error_exc(
        request: Request,
        exc: ZeroDivisionError,

):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "message": exc.args[0],

        }, 
    )
async def Abror_sleepy_error_exc(request: Request, exc: AbrorSleepyException):
    return JSONResponse(
        status_code=status.HTTP_406_NOT_ACCEPTABLE, content={"message": exc.msg}
    )        