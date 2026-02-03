from balepy.objects import HTTPMethod

import balepy


class PromoteChatMember:

    async def promote_chat_member(
            self: "balepy.Client",
            chat_id: int,
            user_id: int,
            can_change_info: bool = None,
            can_post_messages: bool = None,
            can_edit_messages: bool = None,
            can_delete_messages: bool = None,
            can_manage_video_chats: bool = None,
            can_invite_users: bool = None,
            can_restrict_members: bool = None,
            
    ):
        params = {
            'chat_id': chat_id,
            'user_id': user_id,
            'can_change_info': can_change_info,
            'can_post_messages': can_post_messages,
            'can_edit_messages': can_edit_messages,
            'can_delete_messages': can_delete_messages,
            'can_manage_video_chats': can_manage_video_chats,
            'can_invite_users': can_invite_users,
            'can_restrict_members': can_restrict_members
        }
        return await self.api.execute(name="promoteChatMember", method=HTTPMethod.POST, data=params)
