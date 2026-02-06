"""

from fastapi import APIRouter
import httpx

from app.schemas.weather import WeatherResponse

router = APIRouter(prefix="/weather", tags=["Weather"])

API_KEY = "e40c71cc1dac4429877b594995730afe"


@router.get("/weather/today", response_model=WeatherResponse)
async def get_today_weather(city: str):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            )
            response.raise_for_status()
    except Exception as e:
        raise httpx.HTTPError(status_code=400, detail=str(e))

    return response.json()

    """

from fastapi import APIRouter, HTTPException
import httpx


from app.schemas import WeatherResponse

router = APIRouter(prefix="/weather", tags=["Weather"])

API_KEY = "214d21e00f9b966bc4ade4ce7d85de22"


@router.get("/weather/today/", response_model=WeatherResponse)
async def get_weather_today(city: str):
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.get(
                url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}"
            )
            resp.raise_for_status()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    return resp.json()