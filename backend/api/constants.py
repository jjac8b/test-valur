import os
from pydantic import BaseModel


class Constants(BaseModel):
    django_secret: str
    frontend_port: str
    debug: bool


constants = Constants(
    django_secret=os.environ["DJANGO_SECRET"],
    frontend_port=os.environ["FRONTEND_PORT"],
    debug=True if os.environ["DEBUG"] == "True" else False,
)
