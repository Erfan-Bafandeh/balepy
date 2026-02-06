from balepy.objects import HTTPMethod

import balepy


class EditMessageReplyMarkup:

    async def edit_message_reply_markup(
            self: "balepy.Client",
            chat_id: str,
            message_id: int,
            reply_markup: dict = None
    ):
        params = {
            'chat_id': chat_id,
            'message_id': message_id,
            'reply_markup': reply_markup
        }
        return await self.api.execute(name='editMessageReplyMarkup', method=HTTPMethod.POST, data=params)
