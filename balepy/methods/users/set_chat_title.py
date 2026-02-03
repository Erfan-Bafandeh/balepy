from balepy.objects import HTTPMethod

import balepy


class SetChatTitle:

    async def set_chat_title(
            self: "balepy.Client",
            chat_id: str,
            title: str
    ):
        params = {
            'chat_id': chat_id,
            'title': title
        }
        return await self.api.execute(name="setChatTitle", method=HTTPMethod.POST, data=params)