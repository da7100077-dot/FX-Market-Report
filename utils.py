import httpx
import logging
import asyncio

logger = logging.getLogger(__name__)
FRANKFURTER_BASE_URL = "https://api.frankfurter.app"

async def fetch_exchange_rates(base_currency: str):
    """Fetch exchange rates from Frankfurter API with fallback data."""
    url = f"{FRANKFURTER_BASE_URL}/latest"
    params = {"from": base_currency.upper()}
    
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            rates = data.get("rates")
            if rates:
                return rates
    except Exception as e:
        logger.error(f"Error fetching rates for {base_currency}: {e}")
    
    # Return fallback data if API fails
    return get_fallback_rates(base_currency.upper())

def get_fallback_rates(base_currency: str):
    """Provide static exchange rates as fallback when API is down."""
    fallback_rates = {
        "USD": {
            "EUR": 0.9200, "GBP": 0.7900, "JPY": 148.50, "CHF": 0.8850,
            "AUD": 1.5200, "CAD": 1.3650, "NZD": 1.6500, "CNY": 7.2450,
            "INR": 83.50, "BRL": 5.4500, "ZAR": 18.50, "MXN": 18.90,
            "SGD": 1.3450, "HKD": 7.8200, "KRW": 1330.00, "SEK": 10.50,
            "NOK": 10.70, "TRY": 32.50, "RUB": 92.00, "PLN": 4.0500
        },
        "EUR": {
            "USD": 1.0870, "GBP": 0.8587, "JPY": 161.50, "CHF": 0.9620,
            "AUD": 1.6520, "CAD": 1.4830, "NZD": 1.7930, "CNY": 7.8750,
            "INR": 90.75, "BRL": 5.9250, "ZAR": 20.10, "MXN": 20.55,
            "SGD": 1.4620, "HKD": 8.5000, "KRW": 1445.00, "SEK": 11.41,
            "NOK": 11.63, "TRY": 35.35, "RUB": 100.00, "PLN": 4.4000
        },
        "GBP": {
            "USD": 1.2650, "EUR": 1.1645, "JPY": 188.00, "CHF": 1.1200,
            "AUD": 1.9250, "CAD": 1.7270, "NZD": 2.0880, "CNY": 9.1700,
            "INR": 105.70, "BRL": 6.9000, "ZAR": 23.40, "MXN": 23.95,
            "SGD": 1.7030, "HKD": 9.8950, "KRW": 1685.00, "SEK": 13.30,
            "NOK": 13.55, "TRY": 41.15, "RUB": 116.50, "PLN": 5.1250
        },
        "JPY": {
            "USD": 0.00673, "EUR": 0.00619, "GBP": 0.00532, "CHF": 0.00596,
            "AUD": 0.01025, "CAD": 0.00919, "NZD": 0.01110, "CNY": 0.0488,
            "INR": 0.562, "BRL": 0.0367, "ZAR": 0.1245, "MXN": 0.1273,
            "SGD": 0.00906, "HKD": 0.0526, "KRW": 8.95, "SEK": 0.0708,
            "NOK": 0.0721, "TRY": 0.2188, "RUB": 0.619, "PLN": 0.0273
        }
    }
    
    # Return rates for the requested base, or USD rates as default
    return fallback_rates.get(base_currency, fallback_rates["USD"])
