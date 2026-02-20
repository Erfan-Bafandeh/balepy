from balepy.types import ChatPhoto

class ChatFullInfo:
    
    def __init__(self, data: dict):
        self.data = data["result"]
    
    @property
    def id(self) -> int:
        return self.data.get("id")
    
    @property
    def type(self) -> str:
        return self.data.get("type")
    
    @property
    def title(self) -> str:
        return self.data.get("title")
    
    @property
    def username(self) -> str:
        return self.data.get("username")
    
    @property
    def first_name(self) -> str:
        return self.data.get("first_name")
    
    @property
    def last_name(self) -> str:
        return self.data.get("last_name")
    
    @property
    def photo(self) -> ChatPhoto:
        return ChatPhoto(self.data.get("photo"))
    
    @property
    def bio(self) -> str:
        return self.data.get("bio")
    
    @property
    def description(self) -> str:
        return self.data.get("description")
    
    @property
    def invite_link(self) -> str:
        return self.data.get("invite_link")
    
    @property
    def linked_chat_id(self) -> str:
        return self.data.get("linked_chat_id")
