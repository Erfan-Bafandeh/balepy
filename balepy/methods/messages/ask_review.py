from balepy.objects import HTTPMethod

import balepy


class AskReview:

    async def anwser_callback_query(
            self: "balepy.Client",
            user_id: int,
            delay_seconds: int
    ):
        params = {
            'user_id': user_id,
            'delay_seconds': delay_seconds
        }
        return await self.api.execute(name="askReview", method=HTTPMethod.POST, data=params)
