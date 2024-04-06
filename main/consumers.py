from channels.generic.websocket import AsyncWebsocketConsumer
import json


class PostConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Присоединение к WebSocket
        await self.accept()

    async def disconnect(self, close_code):
        # Отсоединение от WebSocket
        pass

    async def notify_new_post(self, event):
        new_post = event['new_post']
        # Отправляем уведомление о новом посте клиенту
        await self.send(text_data=json.dumps({
            'type': 'alert',
            'message': f'Новый пост: {new_post}'
        }))
