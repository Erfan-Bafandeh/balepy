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
    ):
        params = {
            "title": title,
            "description": description,
            "payload": payload,
            "provider_token": self.wallet_token,
            "prices": f"{json.dumps([{"label": price.label, "amount": price.amount} for price in prices], ensure_ascii=False)}"
        }
        return await self.api.execute(name="CreateInvoiceLink", method=HTTPMethod.POST, data=params)
