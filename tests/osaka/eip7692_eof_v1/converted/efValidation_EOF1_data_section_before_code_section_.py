import pytest
from ethereum_test_exceptions import EOFException
from ethereum_test_types.eof.v1 import Container, Section

REFERENCE_SPEC_GIT_PATH = 'EIPS/eip-663.md'
REFERENCE_SPEC_VERSION = 'b658bb87fe039d29e9475d5cfaebca9b92e0fca2'

@pytest.mark.parametrize(
    'container',
    [
        Container(
            name='EOF1_data_section_before_code_section_0',
            raw_bytes="ef000101000403000102000100010000800000aafe",
            validity_error=EOFException.MISSING_CODE_HEADER,
        ),
    ],
    ids=lambda x: x.name,
)
def test_eof_validation(eof_test, container):
    eof_test(container=container)
