import secrets
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing import Annotated
from modules.logger import logger
from modules import config


security = HTTPBasic()


def validate_admin(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)],
):
    is_correct_username = secrets.compare_digest(
        credentials.username.encode("utf8"),
        config.ADMIN_USER.encode("utf8")
    )
    is_correct_password = secrets.compare_digest(
        credentials.password.encode("utf8"),
        config.ADMIN_PASS.encode("utf8")
    )
    return (is_correct_username and is_correct_password)
