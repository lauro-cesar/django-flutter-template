"""[summary]

[description]
"""

from django.urls import re_path
from stripesettings.consumers import Hello

websocket_urlpatterns = [
    re_path(
        r"^channels/hello/(?P<device>[\w-]+)/(?P<group>[.\w-]+)/(?P<inputproperty>[\w-]+)/$",
        Hello.as_asgi(),
    ),
]
