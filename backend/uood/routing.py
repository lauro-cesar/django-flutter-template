from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.db import close_old_connections
import base64
from django.urls import re_path
from uood.gps import GpsSession
from django.contrib.auth import authenticate


class TokenAuthMiddleware:
    def __init__(self, inner):
        self.inner = inner

    def __call__(self, scope):
        headers = dict(scope["headers"])
        if b"authorization" in headers:
            try:
                token_name, token_key = headers[b"authorization"].decode().split()
                i = base64.b64decode(token_key)
                username, password = i.decode().split(":")
                user = authenticate(scope, username=username, password=password)
                if user is not None:
                    scope["user"] = user
                    close_old_connections()
            except Exception:
                pass
        return self.inner(scope)


application = ProtocolTypeRouter(
    {
        "websocket": TokenAuthMiddleware(
            AuthMiddlewareStack(
                (
                    URLRouter(
                        [
                            re_path(
                                r"^uood/sync/(?P<device>[\w-]+)/(?P<group>[.\w-]+)/(?P<inputproperty>[\w-]+)/$",
                                GpsSession,
                            ),
                        ]
                    )
                )
            )
        )
    }
)
