import base64
import re
from dataclasses import dataclass
from io import BytesIO
from typing import Dict, Literal, Tuple

import httpx
from httpx import NetworkError
from PIL import Image

T_Strength = Literal["conservative", "denoise3x", "no-denoise"]

zh_num = "零一二三四五六七八九十"
strength_map: Dict[T_Strength, Tuple[str, ...]] = {
    "conservative": ("保守",),
    "denoise3x": ("强力", "三级", "3级"),
    "no-denoise": ("无", "不"),
}


@dataclass
class Model:
    scale: int = 2
    strength: T_Strength = "denoise3x"

    def __repr__(self) -> str:
        return f"up{self.scale}x-latest-{self.strength}.pth"

    def __str__(self) -> str:
        text = f"超分倍率: {self.scale}倍\n降噪配置: {strength_map[self.strength][0]}"
        if self.strength != "conservative":
            text += "降噪"
        return text


def get_model(text: str) -> Model:
    model = Model()

    if match := re.search(
        r"(?P<scale>.{1})[倍x]", text, re.IGNORECASE
    ):
        try:
            model.scale = zh_num.index(match["scale"])
        except ValueError:
            model.scale = int(match["scale"])

    for k, v in strength_map.items():
        if any(i in text for i in v):
            model.strength = k

    return model


async def enhance_image(img_url: str, model: Model) -> str:
    async with httpx.AsyncClient() as client:
        res = await client.get(img_url)
    if res.is_error:
        raise NetworkError("无法获取此图像")

    image = Image.open(BytesIO(res.content)).convert("RGB")
    if image.width * image.height >= 150_0000:
        image.thumbnail((1300, 1300))
    image.save(imageData := BytesIO(), format="jpeg")
    img_b64 = base64.b64encode(imageData.getvalue()).decode()

    url_push = "http://134.175.32.157:9999/api/predict"
    data = {
        "fn_index": 0,
        "data": [
            f"data:image/jpeg;base64,{img_b64}",
            repr(model),
            2,
        ],
    }

    async with httpx.AsyncClient() as client:
        res = await client.post(url_push, json=data, timeout=60)

    if res.is_error:
        raise NetworkError(f"网络出错: {res.status_code}")

    data = res.json()

    img_data = data["data"][0].split(",")[1]

    return f"base64://{img_data}"
