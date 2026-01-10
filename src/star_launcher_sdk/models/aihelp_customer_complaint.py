from typing import Literal

from pydantic import BaseModel


class AIHelpCustomerComplaint(BaseModel):
    aihelp_app_id: Literal[""]
    aihelp_domain: Literal[""]
    aihelp_app_key: Literal[""]
    initial_interface: Literal[""]
