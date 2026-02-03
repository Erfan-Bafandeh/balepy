from balepy.objects import HTTPMethod

import balepy


class GetChat:

    async def get_chat(
            self: "balepy.Client",
            chat_id: str
    ):
        params = {
            'chat_id': chat_id
        }
        return await self.api.execute(name="getChat", method=HTTPMethod.POST, data=params)