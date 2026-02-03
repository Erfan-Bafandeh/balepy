from balepy.objects import HTTPMethod

import balepy


class ExportChatInviteLink:

    async def export_chat_invite_link(
            self: "balepy.Client",
            chat_id: str
    ):
        params = {
            'chat_id': chat_id
        }
        return await self.api.execute(name="exportChatInviteLink", method=HTTPMethod.POST, data=params)