"""tbd."""  # noqa: E501

# import pytest

# from ethereum_test_base_types.composite_types import Storage
# from ethereum_test_tools import (
#     Account,
#     Alloc,
#     Environment,
#     EOFException,
#     EOFTestFiller,
#     StateTestFiller,
#     Transaction,
# )
# from ethereum_test_tools.vm.opcode import Opcodes as Op
# from ethereum_test_types.eof.v1 import Container, Section

# from . import EOF_FORK_NAME, REFERENCE_SPEC_GIT_PATH, REFERENCE_SPEC_VERSION
# from .helpers import value_code_worked
# from .spec import MAX_STACK_HEIGHT

# REFERENCE_SPEC_GIT_PATH = REFERENCE_SPEC_GIT_PATH
# REFERENCE_SPEC_VERSION = REFERENCE_SPEC_VERSION

# pytestmark = pytest.mark.valid_from(EOF_FORK_NAME)


# def test_swapn2_all_valid_immediates(
#     state_test: StateTestFiller,
#     pre: Alloc,
# ):
#     """Test case for all valid SWAPN2 immediates."""
#     env = Environment()
#     sender = pre.fund_eoa()
#     n = 256
#     values = range(0x500, 0x500 + 257)

#     contract_address = pre.deploy_contract(
#         code=sum(Op.PUSH2[v] for v in values)
#         + sum(Op.SSTORE(x, Op.SWAPN2[0xFF - x]) for x in range(0, n))
#         + Op.STOP,
#     )
#     values_rotated = list(values[1:]) + [values[0]]
#     post = {
#         contract_address: Account(
#             storage=dict(zip(range(0, n), reversed(values_rotated), strict=False))
#         )
#     }

#     tx = Transaction(
#         to=contract_address,
#         gas_limit=10_000_000,
#         sender=sender,
#     )
#     state_test(
#         env=env,
#         pre=pre,
#         post=post,
#         tx=tx,
#     )

# FIXME: salvage misplaced swapn2 test
# @pytest.mark.parametrize(
#     "swapn_operand",
#     [
#         0,
#         2**8 - 1,
#     ],
# )
# def test_dupn2_on_max_stack(
#     state_test: StateTestFiller,
#     pre: Alloc,
#     swapn_operand: int,
# ):
#     """Test case out of bounds SWAPN2 (max stack)."""
#     env = Environment()
#     sender = pre.fund_eoa()
#     storage = Storage()

#     contract_address = pre.deploy_contract(
#         code=Op.SSTORE(storage.store_next(value_code_worked, "code_failed"), value_code_worked)
#         + sum(Op.PUSH2[v] for v in range(0, MAX_STACK_HEIGHT))
#                 + Op.SWAPN2[swapn_operand]
#                 + Op.STOP,
#                 storage=storage.canary()
#             )
#     post = {
#         contract_address: Account(
#             storage=storage.canary()
#         )
#     }

#     tx = Transaction(
#         to=contract_address,
#         gas_limit=10_000_000,
#         sender=sender,
#     )
#     state_test(
#         env=env,
#         pre=pre,
#         post=post,
#         tx=tx,
#     )


# @pytest.mark.parametrize(
#     "stack_height",
#     [
#         0,
#         1,
#         21,
#         2**8 - 1,
#     ],
# )
# def test_swapn_stack_underflow(
#     stack_height: int,
#     eof_test: EOFTestFiller,
# ):
#     """Test case out of bounds SWAPN (underflow)."""
#     eof_code = Container(
#         sections=[
#             Section.Code(
#                 code=sum(Op.PUSH2[v] for v in range(0, stack_height))
#                 + Op.SWAPN[stack_height]
#                 + Op.STOP,
#                 # This is also tested in test_all_opcodes_stack_underflow()
#                 # so make it differ by the declared stack height.
#                 max_stack_height=stack_height + 1,
#             )
#         ],
#     )
#     eof_test(
#         container=eof_code,
#         expect_exception=EOFException.STACK_UNDERFLOW,
#     )


# @pytest.mark.parametrize(
#     "swapn_arg,stack_height",
#     [pytest.param(5, 9, id="5_of_9"), pytest.param(12, 30, id="12_of_30")],
# )
# def test_swapn_simple(
#     stack_height: int,
#     swapn_arg: int,
#     pre: Alloc,
#     state_test: StateTestFiller,
# ):
#     """Test case for simple SWAPN operations."""
#     sender = pre.fund_eoa()
#     contract_address = pre.deploy_contract(
#         code=Container(
#             sections=[
#                 Section.Code(
#                     code=sum(Op.PUSH2[v] for v in range(stack_height, 0, -1))
#                     + Op.SWAPN[swapn_arg]
#                     + sum((Op.PUSH1(v) + Op.SSTORE) for v in range(1, stack_height + 1))
#                     + Op.STOP,
#                     max_stack_height=stack_height + 1,
#                 )
#             ],
#         )
#     )

#     storage = {v: v for v in range(1, stack_height + 1)}
#     storage[1], storage[swapn_arg + 2] = storage[swapn_arg + 2], storage[1]
#     print(storage)
#     post = {contract_address: Account(storage=storage)}

#     tx = Transaction(to=contract_address, sender=sender, gas_limit=10_000_000)

#     state_test(env=Environment(), pre=pre, post=post, tx=tx)
