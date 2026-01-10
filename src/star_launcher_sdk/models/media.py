from typing import Literal

from pydantic import BaseModel

from .aihelp_customer_complaint import AIHelpCustomerComplaint
from .social_media_resource import SocialMediaResource


class Media(BaseModel):
    social_media_resource_open: Literal[True]
    social_media_resource_list: list[SocialMediaResource]
    contact_customer_complaint: Literal[False]
    contact_customer_complaint_type: Literal[0]
    web_customer_complaint_url: Literal[""]
    aihelp_customer_complaint: AIHelpCustomerComplaint
    mail_customer_complaint_url: Literal[""]
