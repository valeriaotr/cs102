from homework08_new.vkapi import config  # type: ignore
from homework08_new.vkapi.session import Session  # type: ignore

session = Session(config.VK_CONFIG["domain"])
