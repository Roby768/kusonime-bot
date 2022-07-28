from pyrogram import Client

class TelegramBot(Client):
    def __init__(self, bot_token, **kwargs):
        super().__init__(
            session_name = "TelegramBot", 
            api_id = 961780, 
            api_hash = "bbbfa43f067e1e8e2fb41f334d32a6a7", 
            bot_token = 1813711209:AAFrcQNty1tiKuTOvlfk9SZPwzMPuKTE4Nw, 
            plugins = dict(root = 'KusonimeBot/plugins'),
            **kwargs
        )
