from typing import Optional

from pydantic import BaseModel, HttpUrl, Field


class FlatDetail(BaseModel):
    title: Optional[str] = Field(default="")
    description: Optional[str] = Field(default="")
    images: list[HttpUrl]
    price_rates: Optional[dict[str, int]] = Field(alias="priceRates")
    area_total: float = Field(alias="areaTotal")
    area_living: float = Field(alias="areaLiving")
    address: str
    location: list[float]
    code: int

    @property
    def caption(self):
        return f"<b>{self.title or ''}</b>\n\n<i>{self.description[:100] if self.description is not None else ''}..</i>"
