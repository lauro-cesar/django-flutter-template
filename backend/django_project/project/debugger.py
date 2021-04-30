from django.utils.encoding import smart_text
from django.conf import settings
from logs.models import RequestLog
import json


class DebugMe:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        ignoreP = ["admin", "static"]

        if request.path.split("/")[1] not in ignoreP:
            if settings.DEBUG:
                r = json.dumps("%s" % request.__dict__, sort_keys=True, indent=4)
                RequestLog.objects.create(request=smart_text(r), path=request.path)

        response = self.get_response(request)
        return response
