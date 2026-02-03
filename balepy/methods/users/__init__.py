from .get_me import GetMe
from .log_out import LogOut
from .ban_chat_member import BanChatMember
from .unban_chat_member import UnbanChatMember
from .promote_chat_member import PromoteChatMember
from .set_chat_photo import SetChatPhoto
from .leave_chat import LeaveChat
from .get_chat import GetChat


class Users(GetMe,
            LogOut,
            BanChatMember,
            UnbanChatMember,
            PromoteChatMember,
            SetChatPhoto,
            LeaveChat,
            GetChat
            ):
    pass
