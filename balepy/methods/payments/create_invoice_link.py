from balepy.objects import HTTPMethod
from balepy.types import LabeledPrice

import balepy

import json


class CreateInvoiceLink:

    async def create_invoice_link(
            self: "balepy.Client",
            title: str,
            description: str,
            payload: str,
            prices: list[LabeledPrice]
    ) -> dict:
        params = {
            "title": title,
            "description": description,
            "payload": payload,
            "provider_token": self.wallet_token,
            "prices": json.dumps([p.to_dict() for p in prices], ensure_ascii=False)
        }
        return await self.api.execute(name="createInvoiceLink", method=HTTPMethod.POST, data=params)
