# line-bot
<h3>製作line聊天機器人很大的時間會是在架設上面<br>
把程式碼放到雲端上去執行 少部分在寫程式</h3>
• 使用者手機=>雲端line server=>轉載web app<br>
• line messaging api註冊<br>
• 取得token/channel secret 啟用webhooks<br>
• flask架設伺服器<br>
• Heroku雲端伺服器<br>
• github專案放到雲端伺服器執行<br>

<h3>簡易對話回覆</h3>
<pre>
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = '很抱歉,您說什麼'

    if '給我貼圖' in msg:
        sticker_message = StickerSendMessage(
            package_id='1',
            sticker_id='11'
        )

        line_bot_api.reply_message(
            event.reply_token,
            sticker_message)
        return

    if msg in ['hi', 'Hi']:
        r = '嗨'
    elif msg == '你吃飯了嗎':
        r = '還沒'
    elif msg == '你是誰':
        r = '我是機器人'
    elif '訂位' in msg:
        r = '您想訂位,是嗎?'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))
</pre>