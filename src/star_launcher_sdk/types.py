from pathlib import PurePosixPath
from typing import Annotated  # noqa: TID251

# noinspection PyProtectedMember
from annotated_types import Not
from annotated_types import Predicate
from pydantic import Base64Bytes
from pydantic import Field
from pydantic import HttpUrl
from pydantic import NonNegativeInt

EmptyDict = Annotated[dict, Field(max_length=0)]
EmptyList = Annotated[list, Field(max_length=0)]

# noinspection PyTypeChecker
AbsolutePath = Annotated[PurePosixPath, Predicate(PurePosixPath.is_absolute)]
# noinspection PyTypeChecker
RelativeExePath = Annotated[
    PurePosixPath, Predicate(lambda path: path.suffix == ".exe"), Predicate(Not(PurePosixPath.is_absolute))
]
# noinspection PyTypeChecker
RelativeZipPath = Annotated[
    PurePosixPath, Predicate(lambda path: path.suffix == ".zip"), Predicate(Not(PurePosixPath.is_absolute))
]

ImageUrl = Annotated[HttpUrl, Predicate(lambda url: url.path.endswith((".jpg", ".jpeg", ".png")))]
JsonUrl = Annotated[HttpUrl, Predicate(lambda url: url.path.endswith(".json"))]

Crc64 = Annotated[NonNegativeInt, Field(lt=2**64)]  # CRC-64/XZ

Base64Sha512 = Annotated[Base64Bytes, Field(min_length=64, max_length=64)]  # SHA-512
