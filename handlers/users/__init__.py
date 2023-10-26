from aiogram import Router

from .start import router as start_router

router = Router()
router.include_router(router=start_router)
