import requests


class TrackerAPI:
    def __init__(
        self,
        apiUrl="https://tracker.sharedway.app",
        restPath="/api",
        socketPath="/api/socket",
        token="bJw1kfQP3TbRDCFfnqEXIQNSNc8Pgn0L",
    ):
        self.session = requests.Session()
        self.apiUrl = apiUrl
        self.restPath = restPath
        self.socketPath = socketPath
        self.token = token
        self.baseUrl = "{apiUrl}{restPath}".format(
            apiUrl=self.apiUrl, restPath=self.restPath
        )
        self.sessionUrl = "{baseUrl}/session?token={userToken}".format(
            userToken=self.token, baseUrl=self.baseUrl
        )
        self.devicesUrl = "{baseUrl}/devices".format(baseUrl=self.baseUrl)
        self.serverUrl = "{baseUrl}/server".format(baseUrl=self.baseUrl)

        self.session.get(self.sessionUrl)

    def serverDevices(self, trackerIMEI=None):
        url = self.devicesUrl
        if trackerIMEI:
            url = "{url}?uniqueId={imei}".format(url=url, imei=trackerIMEI)
        devices = self.session.get(url)
        try:
            return devices.json()
        except Exception:
            return None

    def devicePosition(self, positionID=None):
        url = "{baseUrl}/positions".format(baseUrl=self.baseUrl)

        if positionID:
            url = "{url}?id={id}".format(url=url, id=positionID)

        positions = self.session.get(url)
        try:
            return positions.json()
        except Exception:
            return None

    def serverStatus(self):
        server = self.session.get(self.serverUrl)
        return server.status_code

    def serverInfo(self):
        server = self.session.get(self.serverUrl)
        try:
            return server.json()
        except Exception:
            return None
