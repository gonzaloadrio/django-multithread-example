import json

from channels.generic.websocket import AsyncWebsocketConsumer

from core.views import kmeans


class CoreConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        cpu = -1
        if 'cpu' in data:
            cpu = data['cpu']

        print(text_data)

        # Parallel(n_jobs=-1)(delayed(np.sqrt)(i ** 2) for i in range(100))
        centers = kmeans(cpu)

        # print(centers)
        await self.send(text_data=json.dumps({
            'message': centers.tolist()
        }))
