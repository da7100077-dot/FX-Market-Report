import httpx
import logging

logger = logging.getLogger(__name__)
FRANKFURTER_BASE_URL = "https://api.frankfurter.app"

async def fetch_exchange_rates(base_currency: str):
    url = f"{FRANKFURTER_BASE_URL}/latest"
    params = {"from": base_currency.upper()}
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            return data.get("rates")
    except Exception as e:
        logger.error(f"Error fetching rates for {base_currency}: {e}")
        return None
