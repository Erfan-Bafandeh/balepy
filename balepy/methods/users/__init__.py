from .get_me import GetMe
from .log_out import LogOut
from .ban_chat_member import BanChatMember
from .unban_chat_member import UnbanChatMember


class Users(GetMe,
            LogOut,
            BanChatMember,
            UnbanChatMember
            ):
    pass
