from balepy.objects import HTTPMethod

import balepy


class RevokeChatInviteLink:

    async def revoke_chat_invite_link(
            self: "balepy.Client",
            chat_id: str,
            invite_link: str
    ):
        params = {
            'chat_id': chat_id,
            'invite_link': invite_link
        }
        return await self.api.execute(name="revokeChatInviteLink", method=HTTPMethod.POST, data=params)