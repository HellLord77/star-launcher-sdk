from pydantic_extra_types.semantic_version import SemanticVersion

from star_launcher_sdk.types import RelativeZipPath

from .base import Base


class ManifestUrlParams(Base):
    version: SemanticVersion
    file_path: RelativeZipPath
