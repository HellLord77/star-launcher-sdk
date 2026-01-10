from typing import Literal

from pydantic import BaseModel
from pydantic import ByteSize
from pydantic_extra_types.semantic_version import SemanticVersion

from star_launcher_sdk.types import EmptyList
from star_launcher_sdk.types import RelativeZipPath


class GameInfo(BaseModel):
    game_lowest_version: SemanticVersion
    game_latest_version: SemanticVersion
    game_latest_file_path: RelativeZipPath
    game_start_exe_name: str
    game_file_size: Literal[""]
    game_file_size_type: Literal[""]
    crc64: Literal[""]
    size: Literal[0]
    file_url: Literal[""]
    decompression_size: ByteSize
    config_id: Literal[0]
    game_start_params: EmptyList | None = None
