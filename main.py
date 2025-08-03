import asyncio
import logging
from bot.telegram_bot import start_bot
from monitoring.ultra_fast_monitor import UltraFastMonitor

# Минимальное логирование
logging.basicConfig(level=logging.WARNING)

async def main():
    """Запуск бота"""
    print("🚀 Запуск PumpSwap Bot с Telegram интерфейсом...")
    print("📱 Откройте Telegram и найдите вашего бота")
    
    # Запуск мониторинга и бота параллельно
    monitor = UltraFastMonitor()
    
    tasks = [
        start_bot(),  # Telegram бот
        monitor.monitor_all_sources_continuously()  # Мониторинг
    ]
    
    try:
        await asyncio.gather(*tasks)
    except KeyboardInterrupt:
        print("\n🛑 Бот остановлен пользователем")
    except Exception as e:
        print(f"\n❌ Критическая ошибка: {e}")

if __name__ == "__main__":
    asyncio.run(main())
