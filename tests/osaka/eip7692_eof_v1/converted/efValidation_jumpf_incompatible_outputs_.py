import pytest
from ethereum_test_exceptions import EOFException
from ethereum_test_types.eof.v1 import Container, Section

REFERENCE_SPEC_GIT_PATH = 'EIPS/eip-663.md'
REFERENCE_SPEC_VERSION = 'b658bb87fe039d29e9475d5cfaebca9b92e0fca2'

@pytest.mark.parametrize(
    'container',
    [
        Container(
            name='jumpf_incompatible_outputs_0',
            raw_bytes="ef000101000c02000300040005000404000000008000030003000200050003e3000100e500025f5f5f5f5fe4",
            validity_error=EOFException.JUMPF_DESTINATION_INCOMPATIBLE_OUTPUTS,
        ),
    ],
    ids=lambda x: x.name,
)
def test_eof_validation(eof_test, container):
    eof_test(container=container)
