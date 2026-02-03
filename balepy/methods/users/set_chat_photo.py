from balepy.objects import HTTPMethod

import balepy


class SetChatPhoto:

    async def set_chat_photo(
            self: "balepy.Client",
            chat_id: str,
            photo: str
    ):
        params = {
            'chat_id': chat_id,
            'photo': photo
        }
        return await self.api.execute(name="setChatPhoto", method=HTTPMethod.POST, data=params)