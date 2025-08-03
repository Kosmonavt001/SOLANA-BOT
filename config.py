import os
from dotenv import load_dotenv

load_dotenv()

CONFIG = {
    # 🔑 API КЛЮЧИ
    "API_KEYS": {
        "HELIUS": os.getenv("HELIUS_API_KEY", ""),
        "BIRDEYE": os.getenv("BIRDEYE_API_KEY", ""),
        "JUPITER": os.getenv("JUPITER_API_KEY", ""),
        "SOLSCAN": os.getenv("SOLSCAN_API_KEY", ""),
    },
    
    # 🤖 TELEGRAM
    "TELEGRAM": {
        "BOT_TOKEN": os.getenv("TELEGRAM_BOT_TOKEN", ""),
        "CHAT_ID": os.getenv("TELEGRAM_CHAT_ID", ""),
        "ADMIN_CHAT_ID": os.getenv("TELEGRAM_ADMIN_CHAT_ID", ""),
    },
    
    # 🔐 WALLET
    "WALLET": {
        "PRIVATE_KEY": os.getenv("PRIVATE_KEY", ""),
        "PUBLIC_KEY": os.getenv("PUBLIC_KEY", ""),
    },
    
    # 🚀 SOLANA RPC
    "SOLANA": {
        "RPC_ENDPOINT": os.getenv("SOLANA_RPC", "https://api.mainnet-beta.solana.com"),
        "BACKUP_RPC": os.getenv("SOLANA_BACKUP_RPC", "https://solana-api.projectserum.com"),
        "JITO_RPC": os.getenv("JITO_RPC", "https://mainnet.block-engine.jito.wtf:443"),
        "COMMITMENT": "confirmed",
    },
    
    # 📊 БЕЗОПАСНЫЕ ФИЛЬТРЫ
    "FILTERS": {
        "min_liquidity": 100_000,
        "min_volume": 50_000,
        "min_liquidity_ratio": 0.10,
        "max_fdv_ratio": 3.0,
        "min_volume_ratio": 0.05,
        "max_holder_concentration": 0.50,
    },
    
    # 💰 ТОРГОВЫЕ ПАРАМЕТРЫ
    "TRADING": {
        "default_amount_sol": 0.1,
        "max_amount_sol": 1.0,
        "slippage": 0.05,
        "priority_fee": 100000,
        "jito_tip": 1000000,
        "max_concurrent_trades": 5,
    },
    
    # 📈 СТРАТЕГИИ ПРОДАЖИ
    "SELL_STRATEGIES": {
        "default": {
            "take_profit": 10.0,
            "stop_loss": -0.3,
            "trailing_stop": 0.1,
            "timeout_hours": 24,
        },
        "aggressive": {
            "take_profit": 3.0,
            "stop_loss": -0.15,
            "trailing_stop": 0.05,
            "timeout_hours": 6,
        },
        "conservative": {
            "take_profit": 20.0,
            "stop_loss": -0.2,
            "trailing_stop": 0.15,
            "timeout_hours": 168,
        }
    },
    
    # 🛡️ БЕЗОПАСНОСТЬ И ПРОВЕРКИ
    "SECURITY": {
        "enable_rugcheck": True,
        "enable_scam_detection": True,
        "enable_pumpfun_check": True,
        "max_risk_level": "MEDIUM",
        "blacklist_tokens": [],
        "whitelist_tokens": [],
    },
    
    # ⚡ ПРОИЗВОДИТЕЛЬНОСТЬ
    "PERFORMANCE": {
        "connection_pool_size": 100,
        "request_timeout": 3,
        "cache_expire_time": 3600,
        "monitoring_interval": 1.0,
        "price_check_interval": 0.5,
        "max_concurrent_checks": 20,
    },
    
    # 📊 API ENDPOINTS
    "API_ENDPOINTS": {
        "RAYDIUM": "https://api.raydium.io/v2/sdk/liquidity/mainnet.json",
        "PUMP_FUN": "https://public-api.pump.fun",
        "RUGCHECK": "https://rugcheck.xyz/",
        "BIRDEYE": "https://public-api.birdeye.so",
        "JUPITER": "https://price.jup.ag/v1/price",
        "SOLSCAN": "https://public-api.solscan.io",
    },
    
    # 🚨 СКАМ ДЕТЕКТОР
    "SCAM_DETECTION": {
        "liquidity_drain_threshold": 0.3,
        "volume_spike_threshold": 10.0,
        "price_drop_threshold": 0.2,
        "holder_concentration_threshold": 0.5,
        "fdv_spike_threshold": 0.5,
        "check_interval": 30,
    }
}
