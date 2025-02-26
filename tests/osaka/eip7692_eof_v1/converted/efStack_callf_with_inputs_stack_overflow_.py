import pytest

from ethereum_test_exceptions import EOFException
from ethereum_test_types.eof.v1 import Container

REFERENCE_SPEC_GIT_PATH = "EIPS/eip-663.md"
REFERENCE_SPEC_VERSION = "b658bb87fe039d29e9475d5cfaebca9b92e0fca2"


@pytest.mark.parametrize(
    "container",
    [
        Container(
            name="callf_with_inputs_stack_overflow_0",
            raw_bytes="ef00010100080200020bfd000304000000008003ff02000002600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001e300015050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050f35050e4",
        ),
        Container(
            name="callf_with_inputs_stack_overflow_1",
            raw_bytes="ef00010100080200020bff000404000000008003ff03030004600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001e3000150505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050f3600150e4",
        ),
        Container(
            name="callf_with_inputs_stack_overflow_2",
            raw_bytes="ef00010100080200020bff000304000000008003ff03050005600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001e3000150505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050f35f5fe4",
            validity_error=EOFException.STACK_OVERFLOW,
        ),
        Container(
            name="callf_with_inputs_stack_overflow_3",
            raw_bytes="ef00010100080200020bff000504000000008003ff03030005600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001e3000150505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050f35f5f5050e4",
            validity_error=EOFException.STACK_OVERFLOW,
        ),
        Container(
            name="callf_with_inputs_stack_overflow_4",
            raw_bytes="ef00010100080200020c00000504000000008003ff020000036001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001e30001505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050f35f505050e4",
            validity_error=EOFException.STACK_OVERFLOW,
        ),
        Container(
            name="callf_with_inputs_stack_overflow_5",
            raw_bytes="ef00010100080200020bfe000704000000008003ff02000004600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001600160016001e30001505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050f35f5f50505050e4",
            validity_error=EOFException.STACK_OVERFLOW,
        ),
    ],
    ids=lambda x: x.name,
)
def test_eof_validation(eof_test, container):
    eof_test(container=container)
