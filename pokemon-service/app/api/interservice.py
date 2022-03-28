import os
import httpx
from app.config import get_settings


def team_exists(team_id: int):
    url = get_settings().team_service_url
    r = httpx.get(f'{url}{team_id}')
    return True if r.status_code == 200 else False
