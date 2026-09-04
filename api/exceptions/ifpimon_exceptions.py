
class IFPIMonNotFoundError(Exception):
    def __init__(self, ifpimon_id: int):
        self.ifpimon_id = ifpimon_id