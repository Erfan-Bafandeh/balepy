from balepy.objects import HTTPMethod

import balepy


class EditMessageCaption:

    async def edit_message_caption(
            self: "balepy.Client",
            chat_id: str,
            message_id: int,
            caption: str = None,
            reply_markup: dict = None
    ):
        params = {
            'chat_id': chat_id,
            'message_id': message_id,
            'caption': caption,
            'reply_markup': reply_markup
        }
        return await self.api.execute(name='editMessageCaption', method=HTTPMethod.POST, data=params)
