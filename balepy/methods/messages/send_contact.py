from balepy.objects import HTTPMethod

import balepy


class SendContact:

    async def send_contact(
            self: "balepy.Client",
            chat_id: str,
            phone_number: str,
            first_name: str,
            last_name: str = None,
            reply_to_message_id: int = None,
            reply_markup: dict = None
    ):
        params = {
            'chat_id': chat_id,
            'phone_number': phone_number,
            'first_name': first_name,
            'last_name': last_name,
            'reply_to_message_id': reply_to_message_id,
            'reply_markup': reply_markup
        }
        return await self.api.execute(name="sendContact", method=HTTPMethod.POST, data=params)
