from balepy.objects import HTTPMethod

import balepy


class GetChatAdministrators:

    async def get_chat_administrators(
            self: "balepy.Client",
            chat_id: str
    ):
        params = {
            'chat_id': chat_id
        }
        return await self.api.execute(name="getChatAdministrators", method=HTTPMethod.POST, data=params)