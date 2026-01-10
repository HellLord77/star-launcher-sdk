from enum import Enum

from httpx import URL


class UpdateUrl(URL, Enum):
    HEAVEN_BURNS_RED_GLOBAL = "https://launcher-pkg-en.yo-star.com/pubplat/game_launcher/install_pkg/launcher/HBR_EN/"

    MAHJONG_SOUL_GLOBAL = "https://launcher-pkg-en.yo-star.com/pubplat/game_launcher/install_pkg/launcher/MajSoul_EN/"
    MAHJONG_SOUL_JAPAN = "https://launcher-pkg-jp.yo-star.com/pubplat/game_launcher/install_pkg/launcher/MajSoul_JP/"
    MAHJONG_SOUL_KOREA = "https://launcher-pkg-kr.yo-star.com/pubplat/game_launcher/install_pkg/launcher/MajSoul_KR/"

    STELLA_SORA_CHINA = (
        "https://game-launcher-ss-cn.yostar.net/pubplat/game-launcher-cn/install_pkg/launcher/StellaSora_CN/"
    )
    STELLA_SORA_GLOBAL = "https://launcher-pkg-ss-en.yo-star.com/install_pkg/game_launcher/StellaSora_EN/"
    STELLA_SORA_JAPAN = "https://launcher-pkg-ss-jp.yo-star.com/install_pkg/game_launcher/StellaSora_JP/"
    STELLA_SORA_KOREA = "https://launcher-pkg-ss-kr.yo-star.com/install_pkg/game_launcher/StellaSora_KR/"
