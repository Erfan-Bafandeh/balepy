from .get_me import GetMe
from .log_out import LogOut
from .ban_chat_member import BanChatMember
from .unban_chat_member import UnbanChatMember
from .promote_chat_member import PromoteChatMember


class Users(GetMe,
            LogOut,
            BanChatMember,
            UnbanChatMember,
            PromoteChatMember
            ):
    pass
