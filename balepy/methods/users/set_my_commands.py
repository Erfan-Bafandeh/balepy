from typing import Optional
from balepy.objects import HTTPMethod
from balepy.types import BotCommand
import balepy

class SetMyCommands:
    async def set_my_commands(self: "balepy.Client", commands: list[BotCommand]) -> dict:
        params = {
            'commands': [cmd.to_dict() for cmd in commands]
        }
        return await self.api.execute(name="setMyCommands", method=HTTPMethod.POST, data=params)
