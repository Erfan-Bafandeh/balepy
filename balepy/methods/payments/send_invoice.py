from typing import Optional, Union

from balepy.objects import HTTPMethod
from balepy.types import LabeledPrice

import balepy

import json


class SendInvoice:

    async def send_invoice(
            self: "balepy.Client",
            chat_id: Union[int, str],
            title: str,
            description: str,
            payload: str,
            prices: list[LabeledPrice],
            photo_url: Optional[str] = None,
            photo_size: Optional[int] = None,
            photo_width: Optional[int] = None,
            photo_height: Optional[int] = None,
            need_name: Optional[bool] = None,
            need_phone_number: Optional[bool] = None,
            need_email: Optional[bool] = None,
            is_flexible: Optional[bool] = None,
            reply_to_message_id: Optional[int] = None,
            reply_markup: Optional[dict] = None
    ) -> dict:
        params = {
            "chat_id": chat_id,
            "title": title,
            "description": description,
            "payload": payload,
            "provider_token": self.wallet_token,
            "prices": json.dumps([p.to_dict() for p in prices], ensure_ascii=False),
            "photo_url": photo_url,
            "photo_size": photo_size,
            "photo_width": photo_width,
            "photo_height": photo_height,
            "need_name": need_name,
            "need_phone_number": need_phone_number,
            "need_email": need_email,
            "is_flexible": is_flexible,
            "reply_to_message_id": reply_to_message_id,
            "reply_markup": reply_markup
        }
        return await self.api.execute(name="sendInvoice", method=HTTPMethod.POST, data=params)
