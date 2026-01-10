from datetime import datetime
from typing import Annotated  # noqa: TID251

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic.alias_generators import to_camel
from pydantic_extra_types.semantic_version import SemanticVersion

from star_launcher_sdk.types import Base64Sha512
from star_launcher_sdk.types import RelativeExePath

from .update_file_info import UpdateFileInfo


class UpdateInfo(BaseModel):
    version: SemanticVersion
    files: Annotated[list[UpdateFileInfo], Field(min_length=1, max_length=1)]
    path: RelativeExePath
    sha512: Base64Sha512
    release_date: datetime

    model_config = ConfigDict(alias_generator=to_camel)
