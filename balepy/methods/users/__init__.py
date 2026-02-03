from .get_me import GetMe
from .log_out import LogOut
from .ban_chat_member import BanChatMember


class Users(GetMe,
            LogOut,
            BanChatMember
            ):
    pass
