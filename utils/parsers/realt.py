from json import loads
from typing import Literal

from aiohttp import ClientSession
from bs4 import BeautifulSoup

from utils.types import FlatDetail


class RealtParser:

    BASE_URL: str = "https://realt.by"
    SALE_FLAT_ENDPOINTS: dict[str, str] = {
        "mogilev-region": "/mogilev-region/sale/flats/",
        "brest-region": "/brest-region/sale/flats/",
    }
    RENT_FLAT_ENDPOINT: str = "/rent/flat-for-long/"

    @classmethod
    async def request(cls, url, params, action) -> str:
        async with ClientSession(base_url=cls.BASE_URL) as session:
            response = await session.get(
                url=(url + params) if action == "sale" else (cls.RENT_FLAT_ENDPOINT + params),
            )
            print(response.real_url)
            return await response.text()

    @classmethod
    def parse_html(cls, html: str) -> list[FlatDetail]:
        soup = BeautifulSoup(markup=html, features="lxml")
        data = loads(soup.find(name="script", attrs={"id": "__NEXT_DATA__"}).text)
        objs = []
        for flat in data.get("props").get("pageProps").get("initialState").get("objectsListing").get("objects"):
            objs.append(FlatDetail(**flat))
        return objs

    @classmethod
    async def get(cls, params: dict, region: str = None, action: Literal["rent", "sale"] = "sale"):
        params = "?" + "&".join(f"{k}={v}" for k, v in params.items())
        html = await cls.request(cls.SALE_FLAT_ENDPOINTS.get(region, "/sale/flats/"), params, action)
        return cls.parse_html(html=html)
