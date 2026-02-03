from balepy.objects import HTTPMethod

import balepy


class GetChatMember:

    async def get_chat_member(
            self: "balepy.Client",
            chat_id: str,
            user_id: int
    ):
        params = {
            'chat_id': chat_id,
            'user_id': user_id
        }
        return await self.api.execute(name="getChatMember", method=HTTPMethod.POST, data=params)