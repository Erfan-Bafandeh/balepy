class ChatPhoto:
    
    def __init__(self, data: dict):
        self.data = data
    
    @property
    def small_file_id(self) -> str:
        return self.data.get("small_file_id")
    
    @property
    def small_file_unique_id(self) -> str:
        return self.data.get("small_file_unique_id")
    
    @property
    def big_file_id(self) -> str:
        return self.data.get("big_file_id")
    
    @property
    def big_file_unique_id(self) -> str:
        return self.data.get("big_file_unique_id")
