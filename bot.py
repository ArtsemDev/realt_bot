from handlers.users import router as users_router
from settings import dp, bot


@dp.startup()
async def on_startup():
    await bot.delete_webhook()


if __name__ == '__main__':
    dp.include_router(router=users_router)
    dp.run_polling(bot)
