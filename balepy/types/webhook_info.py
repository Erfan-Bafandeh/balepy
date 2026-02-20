class WebHookInfo:
    
    def __init__(self, data: dict):
        self.data = data["result"]
    
    @property
    def url(self) -> int:
        return self.data.get("url")
