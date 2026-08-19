WELCOME_TEXT = (
    "Welcome to *FX Market Report*!\n\n"
    "I provide daily forex market updates, analysis, trends, and educational insights.\n"
    "Use the buttons below to explore market data and learn about forex.\n\n"
    "⚠️ *Disclaimer*: This bot provides general educational and market information only. "
    "It does not constitute financial advice or trading recommendations."
)

HELP_TEXT = (
    "Use the inline buttons to navigate:\n"
    "• Market Overview – current exchange rates for major pairs\n"
    "• Currency Pairs – view rates for any base currency\n"
    "• Market Education – learn forex concepts\n"
    "• About – information about this bot\n"
    "• Disclaimer – legal notice\n\n"
    "Commands: /start, /help, /market, /pairs, /education, /about, /disclaimer"
)

ABOUT_TEXT = (
    "*About FX Market Report*\n\n"
    "FX Market Report is an informational and educational bot designed to help users understand "
    "the global foreign exchange market. It provides:\n"
    "• Live exchange rates (using Frankfurter API)\n"
    "• Educational articles on forex basics\n\n"
    "This bot is not an investment service, broker, or financial adviser. "
    "All content is for educational purposes only."
)

DISCLAIMER_TEXT = (
    "*Disclaimer*\n\n"
    "The information provided by FX Market Report is for general educational and informational "
    "purposes only. It does not constitute financial advice, investment advice, trading advice, "
    "or any other type of advice. You should not rely on the content of this bot to make any "
    "financial decisions. Always do your own research and consult with a licensed financial "
    "professional before making investment decisions.\n\n"
    "Past performance is not indicative of future results. Trading forex involves substantial "
    "risk of loss and is not suitable for every investor."
)

MAIN_MENU_BUTTONS = [
    ("📊 Market Overview", "overview"),
    ("💱 Currency Pairs", "pairs"),
    ("📚 Market Education", "education"),
    ("📅 Economic Calendar", "calendar"),
    ("ℹ️ About", "about"),
    ("⚖️ Disclaimer", "disclaimer"),
]

EDUCATION_TOPICS = {
    "what_is_forex": {
        "title": "What is Forex?",
        "content": (
            "Forex (foreign exchange) is the global marketplace for trading national currencies "
            "against one another. It is the largest and most liquid financial market in the world, "
            "with daily trading volumes exceeding $6 trillion.\n\n"
            "Currencies are traded in pairs, e.g., EUR/USD. The first currency is the base, "
            "the second is the quote. The exchange rate tells you how much of the quote currency "
            "you need to buy one unit of the base currency."
        )
    },
    "currency_pairs": {
        "title": "Currency Pairs",
        "content": (
            "Currency pairs are divided into:\n"
            "• *Major Pairs* – include USD and one of EUR, GBP, JPY, CHF, CAD, AUD, NZD.\n"
            "• *Cross Pairs* – pairs without USD, e.g., EUR/GBP.\n"
            "• *Exotic Pairs* – include a major currency and a currency from an emerging economy, "
            "e.g., USD/TRY.\n\n"
            "The base currency is the first in the pair; the quote currency is the second."
        )
    },
    "bid_ask_spread": {
        "title": "Bid, Ask, and Spread",
        "content": (
            "• *Bid* – the price at which you can sell the base currency.\n"
            "• *Ask* – the price at which you can buy the base currency.\n"
            "• *Spread* – the difference between bid and ask, and it represents the broker's cost.\n\n"
            "A narrower spread typically means higher liquidity."
        )
    },
    "pip": {
        "title": "Pip",
        "content": (
            "A pip (percentage in point) is the smallest price move in a currency pair. "
            "For most pairs, a pip is the fourth decimal place (0.0001). For JPY pairs, "
            "it is the second decimal place (0.01).\n\n"
            "Example: if EUR/USD moves from 1.1050 to 1.1051, that is a 1‑pip move."
        )
    },
    "leverage": {
        "title": "Leverage",
        "content": (
            "Leverage allows traders to control a large position with a small amount of capital. "
            "It is expressed as a ratio, e.g., 100:1 means you can control $100,000 with only $1,000.\n\n"
            "While leverage can magnify profits, it also magnifies losses. Use caution."
        )
    },
    "margin": {
        "title": "Margin",
        "content": (
            "Margin is the collateral required to open and maintain a leveraged position. "
            "It is usually expressed as a percentage of the position size.\n\n"
            "If the market moves against you, your broker may issue a margin call, requiring "
            "you to deposit additional funds or close positions."
        )
    },
    "market_sessions": {
        "title": "Market Sessions",
        "content": (
            "The forex market is open 24 hours a day, 5 days a week. The main trading sessions are:\n"
            "• *Sydney* (10 PM – 7 AM GMT)\n"
            "• *Tokyo* (12 AM – 9 AM GMT)\n"
            "• *London* (8 AM – 5 PM GMT)\n"
            "• *New York* (1 PM – 10 PM GMT)\n\n"
            "Overlap periods (e.g., London/New York) have the highest liquidity and volatility."
        )
    },
    "risk_management": {
        "title": "Basic Risk Management",
        "content": (
            "• Never risk more than you can afford to lose.\n"
            "• Use stop‑loss orders to limit losses.\n"
            "• Avoid over‑leveraging.\n"
            "• Diversify your trading strategies.\n"
            "• Keep a trading journal to analyze your performance."
        )
    },
    "fundamental_analysis": {
        "title": "Fundamental Analysis",
        "content": (
            "Fundamental analysis evaluates currencies based on economic indicators, such as:\n"
            "• Interest rates\n"
            "• Inflation\n"
            "• GDP growth\n"
            "• Employment data\n"
            "• Political stability\n\n"
            "Traders use these factors to assess the strength or weakness of a currency."
        )
    },
    "technical_analysis": {
        "title": "Technical Analysis Basics",
        "content": (
            "Technical analysis studies price charts and patterns to predict future movements. "
            "Common tools include:\n"
            "• Support and resistance levels\n"
            "• Moving averages\n"
            "• Relative Strength Index (RSI)\n"
            "• Fibonacci retracements\n\n"
            "It relies on the idea that history tends to repeat itself."
        )
    }
}
