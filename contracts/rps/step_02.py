from pyteal import *
from pyteal.ast.bytes import Bytes
from pyteal_helpers import program


def approval():
    return Approve()


def clear():
    return Approve()
