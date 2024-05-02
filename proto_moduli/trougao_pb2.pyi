from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Tacka(_message.Message):
    __slots__ = ("x", "y")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    x: int
    y: int
    def __init__(self, x: _Optional[int] = ..., y: _Optional[int] = ...) -> None: ...

class Trougao(_message.Message):
    __slots__ = ("A", "B", "C")
    A_FIELD_NUMBER: _ClassVar[int]
    B_FIELD_NUMBER: _ClassVar[int]
    C_FIELD_NUMBER: _ClassVar[int]
    A: Tacka
    B: Tacka
    C: Tacka
    def __init__(self, A: _Optional[_Union[Tacka, _Mapping]] = ..., B: _Optional[_Union[Tacka, _Mapping]] = ..., C: _Optional[_Union[Tacka, _Mapping]] = ...) -> None: ...

class ParametriTrougla(_message.Message):
    __slots__ = ("obim", "povrsina")
    OBIM_FIELD_NUMBER: _ClassVar[int]
    POVRSINA_FIELD_NUMBER: _ClassVar[int]
    obim: float
    povrsina: float
    def __init__(self, obim: _Optional[float] = ..., povrsina: _Optional[float] = ...) -> None: ...
