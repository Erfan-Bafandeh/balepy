from .users import Users
from .updates import Updates
from .messages import Messages
from .payments import Payments


class Methods(Users, Updates, Messages, Payments):
    pass
