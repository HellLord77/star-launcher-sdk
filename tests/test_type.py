from base64 import b64encode
from hashlib import sha512
from os import urandom

import pytest
from pydantic import TypeAdapter
from pydantic import ValidationError


def test_absolute_path():
    from star_launcher_sdk.types import AbsolutePath

    absolute_path_adapter = TypeAdapter(AbsolutePath)

    absolute_path_adapter.validate_strings("/absolute/path/to/file.zip")
    absolute_path_adapter.validate_python(AbsolutePath("/another/absolute/path"))

    with pytest.raises(ValidationError):
        absolute_path_adapter.validate_strings("relative/path/to/file.zip")
    with pytest.raises(ValidationError):
        absolute_path_adapter.validate_python(AbsolutePath("relative/path"))


def test_relative_exe_path():
    from star_launcher_sdk.types import RelativeExePath

    relative_exe_path_adapter = TypeAdapter(RelativeExePath)

    relative_exe_path_adapter.validate_strings("relative/path/to/file.exe")
    relative_exe_path_adapter.validate_python(RelativeExePath("another/relative/path/file.exe"))

    with pytest.raises(ValidationError):
        relative_exe_path_adapter.validate_strings("/absolute/path/to/file.exe")
    with pytest.raises(ValidationError):
        relative_exe_path_adapter.validate_strings("relative/path/to/file.txt")
    with pytest.raises(ValidationError):
        relative_exe_path_adapter.validate_python(RelativeExePath("/absolute/path/file.exe"))
    with pytest.raises(ValidationError):
        relative_exe_path_adapter.validate_python(RelativeExePath("relative/path/file.txt"))


def test_relative_zip_path():
    from star_launcher_sdk.types import RelativeZipPath

    relative_zip_path_adapter = TypeAdapter(RelativeZipPath)

    relative_zip_path_adapter.validate_strings("relative/path/to/file.zip")
    relative_zip_path_adapter.validate_python(RelativeZipPath("another/relative/path/file.zip"))

    with pytest.raises(ValidationError):
        relative_zip_path_adapter.validate_strings("/absolute/path/to/file.zip")
    with pytest.raises(ValidationError):
        relative_zip_path_adapter.validate_strings("relative/path/to/file.txt")
    with pytest.raises(ValidationError):
        relative_zip_path_adapter.validate_python(RelativeZipPath("/absolute/path/file.zip"))
    with pytest.raises(ValidationError):
        relative_zip_path_adapter.validate_python(RelativeZipPath("relative/path/file.txt"))


def test_root_url():
    from star_launcher_sdk.types import RootUrl

    root_url_adapter = TypeAdapter(RootUrl)

    root_url_adapter.validate_strings("https://example.com/")
    # noinspection HttpUrlsUsage
    root_url_adapter.validate_python(RootUrl("http://another-example.org/"))

    with pytest.raises(ValidationError):
        root_url_adapter.validate_strings("https://example.com/path")
    with pytest.raises(ValidationError):
        # noinspection HttpUrlsUsage
        root_url_adapter.validate_python(RootUrl("http://another-example.org/path"))


def test_image_url():
    from star_launcher_sdk.types import ImageUrl

    image_url_adapter = TypeAdapter(ImageUrl)

    image_url_adapter.validate_strings("https://example.com/image.png")
    image_url_adapter.validate_python(ImageUrl("https://example.com/another_image.jpg"))
    image_url_adapter.validate_python(ImageUrl("https://example.com/yet_another_image.jpeg"))

    with pytest.raises(ValidationError):
        image_url_adapter.validate_strings("https://example.com/image")
    with pytest.raises(ValidationError):
        image_url_adapter.validate_python(ImageUrl("https://example.com/another_image.gif"))


def test_json_url():
    from star_launcher_sdk.types import JsonUrl

    json_url_adapter = TypeAdapter(JsonUrl)

    json_url_adapter.validate_strings("https://example.com/data.json")
    json_url_adapter.validate_python(JsonUrl("https://example.com/another_data.json"))

    with pytest.raises(ValidationError):
        json_url_adapter.validate_strings("https://example.com/data")
    with pytest.raises(ValidationError):
        json_url_adapter.validate_python(JsonUrl("https://example.com/another_data.xml"))


def test_crc64():
    from star_launcher_sdk.types import Crc64

    crc64_adapter = TypeAdapter(Crc64)

    crc64_adapter.validate_python(0)
    crc64_adapter.validate_python(2**64 - 1)
    crc64_adapter.validate_strings("1234567890123456789")

    with pytest.raises(ValidationError):
        crc64_adapter.validate_python(-1)
    with pytest.raises(ValidationError):
        crc64_adapter.validate_python(2**64)
    with pytest.raises(ValidationError):
        crc64_adapter.validate_strings("-1234567890123456789")
    with pytest.raises(ValidationError):
        crc64_adapter.validate_strings("18446744073709551616")


def test_base64_sha512():
    from star_launcher_sdk.types import Base64Sha512

    base64_sha512_adapter = TypeAdapter(Base64Sha512)

    data1 = urandom(256)
    encoded1 = b64encode(sha512(data1).digest())
    base64_sha512_adapter.validate_strings(encoded1.decode())

    data2 = urandom(1024)
    encoded2 = b64encode(sha512(data2).digest())
    base64_sha512_adapter.validate_strings(encoded2.decode())

    with pytest.raises(ValidationError):
        base64_sha512_adapter.validate_strings("short_base64_string")
    with pytest.raises(ValidationError):
        base64_sha512_adapter.validate_strings("a" * 65)
    with pytest.raises(ValidationError):
        base64_sha512_adapter.validate_python(b"short_bytes")
