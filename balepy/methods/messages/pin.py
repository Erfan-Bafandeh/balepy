from balepy.objects import HTTPMethod

import balepy


class PinChatMessage:

    async def pin(
            self: "balepy.Client",
            chat_id: str,
            message_id: int
    ):
        params = {
            'chat_id': chat_id,
            'message_id': message_id,
        }
        return await self.api.execute(name="pinChatMessage", method=HTTPMethod.POST, data=params)