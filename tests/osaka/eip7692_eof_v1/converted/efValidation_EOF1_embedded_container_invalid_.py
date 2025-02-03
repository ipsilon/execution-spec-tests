import pytest
from ethereum_test_exceptions import EOFException
from ethereum_test_types.eof.v1 import Container, Section

REFERENCE_SPEC_GIT_PATH = 'EIPS/eip-663.md'
REFERENCE_SPEC_VERSION = 'b658bb87fe039d29e9475d5cfaebca9b92e0fca2'

@pytest.mark.parametrize(
    'container',
    [
        Container(
            name='EOF1_embedded_container_invalid_0',
            raw_bytes="ef0001010004020001000603",
            validity_error=EOFException.INCOMPLETE_SECTION_NUMBER,
        ),
        Container(
            name='EOF1_embedded_container_invalid_1',
            raw_bytes="ef000101000402000100060300",
            validity_error=EOFException.INCOMPLETE_SECTION_NUMBER,
        ),
        Container(
            name='EOF1_embedded_container_invalid_2',
            raw_bytes="ef00010100040200010006030001",
            validity_error=EOFException.MISSING_HEADERS_TERMINATOR,
        ),
        Container(
            name='EOF1_embedded_container_invalid_3',
            raw_bytes="ef0001010004020001000603000100",
            validity_error=EOFException.INCOMPLETE_SECTION_SIZE,
        ),
        Container(
            name='EOF1_embedded_container_invalid_4',
            raw_bytes="ef000101000402000100060300010014",
            validity_error=EOFException.MISSING_HEADERS_TERMINATOR,
        ),
        Container(
            name='EOF1_embedded_container_invalid_5',
            raw_bytes="ef00010100040200010006030000040000000080000160005d000000",
            validity_error=EOFException.ZERO_SECTION_SIZE,
        ),
        Container(
            name='EOF1_embedded_container_invalid_6',
            raw_bytes="ef000101000402000100060300010000040000000080000160005d000000",
            validity_error=EOFException.ZERO_SECTION_SIZE,
        ),
        Container(
            name='EOF1_embedded_container_invalid_7',
            raw_bytes="ef000101000402000100060300010014040000000080000160005d000000",
            validity_error=EOFException.INVALID_SECTION_BODIES_SIZE,
        ),
        Container(
            name='EOF1_embedded_container_invalid_8',
            raw_bytes="ef0001010004020001000603010100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001040000000080000160005d0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
            validity_error=EOFException.TOO_MANY_CONTAINERS,
        ),
    ],
    ids=lambda x: x.name,
)
def test_eof_validation(eof_test, container):
    eof_test(container=container)
