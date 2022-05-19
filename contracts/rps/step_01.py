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
    def reset(account: Expr): 
        return Seq(
            App.localPut(account,local_wager, Int(0)),
            App.localPut(account,local_commitment, Bytes("")),
            App.localPut(account,local_reveal, Bytes("")), 
            App.localPut(account,local_opponent, Bytes("")), 

        )

    @Subroutine(TealType.none)
    def create_challenge(): 
        return Reject() 

    @Subroutine(TealType.none)
    def accept_challenge(): 
        return Reject() 

    @Subroutine(TealType.none)
    def reveal(): 
        return Reject() 


    return program.event(
        init = Approve(),
        opt_in=Seq(
            reset(Int(0)),
            Approve()
        ),
        no_op=Seq(
            Cond(
                [Txn.application_args[0] == op_challenge, create_challenge()],
                [Txn.application_args[0] == op_accept, accept_challenge()], 
                [Txn.application_args[0] == op_reveal, reveal()]
            ),
            Reject() 
        )
    )

def clear(): 
    return Approve() 