from typing import Union
from balepy.objects import HTTPMethod
from balepy.types import ChatPermissions
import balepy
import json


class SetChatPermissions:

    async def set_chat_permissions(
            self: "balepy.Client",
            chat_id: Union[int, str],
            permissions: ChatPermissions
    ) -> dict:
        params = {
            'chat_id': chat_id,
            'permissions': json.dumps(permissions.to_dict())
        }
        return await self.api.execute(name="setChatPermissions", method=HTTPMethod.POST, data=params)
