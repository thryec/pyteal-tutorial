from pyteal import *
from pyteal.ast.bytes import Bytes
from pyteal_helpers import program

def approval():
    # locals 
    local_opponent = Bytes("opponent") # byteslice 
    local_wager = Bytes("wager") # uint64 
    local_commitment = Bytes("commitment") #byteslice
    local_reveal = Bytes("reveal") # byteslice 

    #operations 
    op_challenge = Bytes("challenge")
    op_accept = Bytes("accept")
    op_reveal = Bytes("reveal")

    @Subroutine(TealType.none)
    def reset(): 
        return Seq(
            App.localPut(Int(0),local_opponent, Bytes(""))
        )

    return program.event(
        init = Approve(),
        opt_in=Seq(
            reset(),
            Approve()
        )
    )

def clear(): 
    return Approve() 