from channels.generic.websocket import AsyncJsonWebsocketConsumer
import hashlib


class SessionBase(AsyncJsonWebsocketConsumer):
    device = ""
    group = ""
    inputproperty = ""
    lastContents = {}

    @property
    def group_name(self):
        return "%s-%s-%s" % (self.device, self.group, self.inputproperty)

    @property
    def groupID(self):
        return hashlib.md5(self.group_name.encode("utf-8")).hexdigest()

    async def receive_json(self, content):
        self.lastContents[self.groupID] = content
        print(content)
        await self.channel_layer.group_send(
            self.group_name, {"type": "group_message", "content": content}
        )

    async def group_message(self, event):
        message = event["content"]
        await self.send_json(message)

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)


class GpsSession(SessionBase):
    async def connect(self):
        if "device" in self.scope["url_route"]["kwargs"]:
            self.device = self.scope["url_route"]["kwargs"]["device"]

        if "group" in self.scope["url_route"]["kwargs"]:
            self.group = self.scope["url_route"]["kwargs"]["group"]

        if "inputproperty" in self.scope["url_route"]["kwargs"]:
            self.inputproperty = self.scope["url_route"]["kwargs"]["inputproperty"]

        await self.channel_layer.group_add(self.group_name, self.channel_name)
        if self.groupID in self.lastContents.keys():
            await self.channel_layer.group_send(
                self.group_name,
                {"type": "group_message", "content": self.lastContents[self.groupID]},
            )

        await self.accept()
