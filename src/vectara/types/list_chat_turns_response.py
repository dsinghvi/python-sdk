# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .turn import Turn
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class ListChatTurnsResponse(UniversalBaseModel):
    turns: typing.Optional[typing.List[Turn]] = pydantic.Field(default=None)
    """
    List of turns.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
