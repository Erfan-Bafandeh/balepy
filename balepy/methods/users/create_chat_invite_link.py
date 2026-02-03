from balepy.objects import HTTPMethod

import balepy


class CreateChatInviteLink:

    async def create_chat_invite_link(
            self: "balepy.Client",
            chat_id: str
    ):
        params = {
            'chat_id': chat_id
        }
        return await self.api.execute(name="createChatInviteLink", method=HTTPMethod.POST, data=params)