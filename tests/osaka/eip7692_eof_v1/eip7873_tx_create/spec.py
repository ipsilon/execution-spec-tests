"""EOF V1 Constants used throughout all tests."""

TXCREATE_FAILURE = 0

CREATOR_CONTRACT_BYTECODE = (
    "EF0001 010004 020001002c 040000 00"
    # Types section
    + "00 80 0005"
    # Code section
    # Enough calldata or revert?
    # rjumpi(5, iszero(64 + calldatasize() + OP_LT)) + revert(0, 0)
    + "6040 36 10 15 E10003 5F 5F FD"
    # Copy input data to memory
    # calldatacopy(0, 64, 64 + calldatasize() + OP_SUB)
    + "6040 36 03 6040 5F 37"
    # TXCREATE with arguments
    # txcreate()
    # .initcode(calldataload(0))
    # .input(0, 64 + calldatasize() + OP_SUB)
    # .salt(calldataload(32))
    # .value(OP_CALLVALUE)
    + "6040 36 03 5F 6020 35 34 5F 35 ED"
    # Creation successful or revert?
    # rjumpi(5, OP_DUP1) + revert(0, 0)
    + "80 E10003 5F 5F FD"
    # RETURN new address
    # ret_top()
    + "5F 52 6020 5F F3"
)
