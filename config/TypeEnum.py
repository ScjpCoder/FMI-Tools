from enum import Enum

"""Enumeration of FMU types."""


class FmuType(Enum):
    CS = "CoSimulation"
    ME = "ModelExchange"
