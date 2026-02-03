from balepy.objects import HTTPMethod

import balepy


class GetFile:

    async def get_file(
            self: "balepy.Client",
            file_id: str
    ):
        params = {
            'file_id': file_id
        }
        return await self.api.execute(name="getFile", method=HTTPMethod.POST, data=params)
