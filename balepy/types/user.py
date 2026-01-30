class User:
    
    def __init__(self, data: dict):
        self.data = data
    
    @property
    def id(self) -> int:
        return self.data.get("id")
    
    @property
    def is_bot(self) -> bool:
        return self.data.get("is_bot")
    
    @property
    def first_name(self) -> str:
        return self.data.get("first_name")
    
    @property
    def last_name(self) -> str:
        return self.data.get("last_name")
    
    @property
    def username(self) -> str:
        return self.data.get("username")
    
    @property
    def language_code(self) -> str:
        return self.data.get("language_code")
