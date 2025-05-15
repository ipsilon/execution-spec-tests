"""tbd."""  # noqa: E501

import pytest

from ethereum_test_base_types.composite_types import Storage
from ethereum_test_tools import (
    Account,
    Alloc,
    Environment,
    StateTestFiller,
    Transaction,
)
from ethereum_test_tools.vm.opcode import Opcodes as Op

from . import EOF_FORK_NAME, REFERENCE_SPEC_GIT_PATH, REFERENCE_SPEC_VERSION
from .helpers import value_code_worked

REFERENCE_SPEC_GIT_PATH = REFERENCE_SPEC_GIT_PATH
REFERENCE_SPEC_VERSION = REFERENCE_SPEC_VERSION


# Marking two forks to ensure JUMPDEST analysis is not altered for contracts containing new opcodes
# TODO: not sure if this is the best way to test behavior across forks
pytestmark = pytest.mark.valid_at("Prague", EOF_FORK_NAME)


@pytest.mark.parametrize(
    "suffix",
    [
        0x00,
        0x01,
        0x5B,
        0x5E,
        0x5F,
    ]
    + list(range(0x60, 0x7F))
    + [0xFE, 0xFF],
)
@pytest.mark.parametrize(
    "swapn_operand",
    [
        0,
        0x5B,
        0x60,
        0x61,
        0x7F,
        2**8 - 1,
    ],
)
@pytest.mark.parametrize("add_jumpdest", [True, False])
def test_swapn2_jumpdest_analysis(
    state_test: StateTestFiller,
    pre: Alloc,
    suffix: int,
    swapn_operand: int,
    add_jumpdest: bool,
):
    """Test case ensuring SWAPN2 doesn't alter jumpdest analysis."""
    env = Environment()
    sender = pre.fund_eoa()
    storage = Storage()

    swapn2_code = Op.SWAPN2 + bytes([suffix]) + bytes([swapn_operand])
    contract_address = pre.deploy_contract(
        code=Op.SSTORE(storage.store_next(value_code_worked, "code_worked"), value_code_worked)
        + Op.JUMP(Op.ADD(Op.PC, len(swapn2_code) + 3))
        + swapn2_code
        + (Op.JUMPDEST if add_jumpdest else Op.PUSH0)
        + Op.STOP,
        storage=storage.canary(),
    )
    valid_destination = (
        # Jumping to the Op.STOP without Op.JUMPDEST always fails
        add_jumpdest
        # PUSH2 and above as suffix would consume the Op.JUMPDEST
        and not (0x61 <= suffix <= 0x7F)
        # PUSH1 and above after a non-PUSH suffix would consume the Op.JUMPDEST
        and not (suffix != 0x60 and 0x60 <= swapn_operand <= 0x7F)
    )
    post = {
        contract_address: Account(storage=storage.canary() if not valid_destination else storage)
    }

    tx = Transaction(
        to=contract_address,
        gas_limit=10_000_000,
        sender=sender,
    )
    state_test(
        env=env,
        pre=pre,
        post=post,
        tx=tx,
    )
