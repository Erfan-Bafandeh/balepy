from typing import Optional, Union
from balepy.objects import HTTPMethod
from balepy.types import ChatPermissions
import balepy
import json


class RestrictChatMember:

    async def restrict_chat_member(
            self: "balepy.Client",
            chat_id: Union[int, str],
            user_id: int,
            permissions: ChatPermissions,
            until_date: Optional[int] = None
    ) -> dict:
        params = {
            'chat_id': chat_id,
            'user_id': user_id,
            'permissions': json.dumps(permissions.to_dict()),
            'until_date': until_date
        }
        return await self.api.execute(name="restrictChatMember", method=HTTPMethod.POST, data=params)
