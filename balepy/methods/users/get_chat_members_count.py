from balepy.objects import HTTPMethod

import balepy


class GetChatMembersCount:

    async def get_chat_members_count(
            self: "balepy.Client",
            chat_id: str
    ):
        params = {
            'chat_id': chat_id
        }
        return await self.api.execute(name="getChatMembersCount", method=HTTPMethod.POST, data=params)