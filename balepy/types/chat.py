class Chat:
    
    def __init__(self, data: dict):
        self.data = data["result"]
    
    @property
    def id(self) -> int:
        return self.data.get("id")
    
    @property
    def type(self) -> bool:
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
    
    
