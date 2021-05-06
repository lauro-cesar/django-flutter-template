from rest_framework.authentication import TokenAuthentication


class APITokenAuthentication(TokenAuthentication):
    """
    Django rest uses Token keyword by default, extending TokenAuth and changed it to Bearer
    """

    keyword = "Bearer"
