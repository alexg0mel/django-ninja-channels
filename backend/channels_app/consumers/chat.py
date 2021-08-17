from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.username = "Anonymous"

    async def connect(self):
        print('connect')
        print(self.scope)
        print(self.scope['user-agent'])
        await self.accept()
        await self.send(text_data="[Welcome %s!]" % self.username)

    async def receive(self, *, text_data):
        print('receive, text_data=', text_data)
        if text_data.startswith("/name"):
            self.username = text_data[5:].strip()
            await self.send(text_data="[set your username to %s]" % self.username)
        if text_data == 'Ping':
            await self.send(text_data="Pong")
        else:
            await self.send(text_data=self.username + ": " + text_data)

    async def disconnect(self, message):
        pass
