from .log import Log
from .credential.mam import Mam


class Credential:

    log = Log()
    mam = Mam()

    def __init__(self):
        pass
