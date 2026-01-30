from balepy.objects import HTTPMethod
from balepy.types import LabeledPrice

import balepy

import json


class SendInvoice:

    async def send_invoice(
            self: "balepy.Client",
            chat_id: str,
            title: str,
            description: str,
            payload: str,
            prices: list[LabeledPrice],
            photo_url: str = None,
            reply_to_message_id: int = None
    ):
        params = {
            "chat_id": chat_id,
            "title": title,
            "description": description,
            "payload": payload,
            "provider_token": self.wallet_token,
            "prices": f"{json.dumps([{"label": price.label, "amount": price.amount} for price in prices], ensure_ascii=False)}",
            "photo_url": photo_url,
            "reply_to_message_id": reply_to_message_id
        }
        return await self.api.execute(name="sendInvoice", method=HTTPMethod.POST, data=params)
