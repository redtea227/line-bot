from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('3xVY29YC9I71FLsBHCtPEQ+JmzcRVkJ4cdLCGxDrOrLCpNCPR8rxFW/t1XnxQiPT92iH497oAz+mF2YDYKhH4e0laWQNXx9mMiTdapSUDQULD37iS+F9pP8t1iDDcLuAs43sqbFuPeneYZcZlr+G1gdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('6a734d65036ed40120fc9f112484e4e7')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()