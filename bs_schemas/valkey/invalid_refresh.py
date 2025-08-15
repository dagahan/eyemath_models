from ..base_schema import *


class InvalidRefresh(BaseModel):  # {refresh_hash} {expire_time} {autoremove after refresh_token valid time is over}
    pass #  all of data is in title