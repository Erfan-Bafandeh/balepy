from balepy.objects import HTTPMethod

import balepy


class BanChatMember:

    async def ban_chat_member(
            self: "balepy.Client",
            chat_id: int,
            user_id: int
    ):
        params = {
            'chat_id': chat_id,
            'user_id': user_id
        }
        return await self.api.execute(name="banChatMember", method=HTTPMethod.POST, data=params)
