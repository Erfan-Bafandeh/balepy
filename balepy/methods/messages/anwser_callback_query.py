from balepy.objects import HTTPMethod

import balepy


class AnwserCallbackQuery:

    async def anwser_callback_query(
            self: "balepy.Client",
            callback_query_id: str,
            text: str = None,
            show_alert: bool = False
    ):
        params = {
            'callback_query_id': callback_query_id,
            'text': text,
            'show_alert': show_alert
        }
        return await self.api.execute(name="answerCallbackQuery", method=HTTPMethod.POST, data=params)
