import pytest
from ethereum_test_exceptions import EOFException
from ethereum_test_types.eof.v1 import Container, Section

REFERENCE_SPEC_GIT_PATH = 'EIPS/eip-663.md'
REFERENCE_SPEC_VERSION = 'b658bb87fe039d29e9475d5cfaebca9b92e0fca2'

@pytest.mark.parametrize(
    'container',
    [
        Container(
            name='validInvalid_10',
            raw_bytes="ef000101000402000100010400010000800000efef",
            validity_error=EOFException.UNDEFINED_INSTRUCTION,
        ),
        Container(
            name='validInvalid_11',
            raw_bytes="ef0001010004020001000504000100008000013030505000ef",
            validity_error=EOFException.INVALID_MAX_STACK_HEIGHT,
        ),
        Container(
            name='validInvalid_12',
            raw_bytes="ef0001010004020001000504000100008000033030505000ef",
            validity_error=EOFException.INVALID_MAX_STACK_HEIGHT,
        ),
        Container(
            name='validInvalid_13',
            raw_bytes="ef00010100040200010004040001000080000130505000ef",
            validity_error=EOFException.STACK_UNDERFLOW,
        ),
        Container(
            name='validInvalid_14',
            raw_bytes="ef000101000c0200030037000b001f0400010000800400000a000a00640064e30002e30002e30002e30002e30002e30002e30002e30002e30002e300023030303030303030303030303030303030303030303030300030303030303030303030e4e30001e30001e30001e30001e30001e30001e30001e30001e30001e30001e4ef",
            validity_error=EOFException.MAX_STACK_HEIGHT_ABOVE_LIMIT,
        ),
        Container(
            name='validInvalid_15',
            raw_bytes="ef000101000802000200070004040001000180000200000001300150e3000100305000e4ef",
            validity_error=EOFException.INVALID_FIRST_SECTION_TYPE,
        ),
        Container(
            name='validInvalid_16',
            raw_bytes="ef000101000802000200060003040001000001000200800001303001e50001305000ef",
            validity_error=EOFException.INVALID_FIRST_SECTION_TYPE,
        ),
        Container(
            name='validInvalid_17',
            raw_bytes="ef000101000802000200040001040001000080000000800000e300020000ef",
            validity_error=EOFException.INVALID_CODE_SECTION_INDEX,
        ),
        Container(
            name='validInvalid_18',
            raw_bytes="ef00010100040200010004040001000080000130015000ef",
            validity_error=EOFException.STACK_UNDERFLOW,
        ),
        Container(
            name='validInvalid_19',
            raw_bytes="ef0001010008020002000600040400010000800002020000005f80e3000100505050e4ef",
            validity_error=EOFException.STACK_UNDERFLOW,
        ),
        Container(
            name='validInvalid_20',
            raw_bytes="ef0001010008020002000600050400010000800002020000035f80e300010082505050e4ef",
            validity_error=EOFException.STACK_UNDERFLOW,
        ),
        Container(
            name='validInvalid_21',
            raw_bytes="ef0001010008020002000600040400010000800002020000025f80e3000100915050e4ef",
            validity_error=EOFException.STACK_UNDERFLOW,
        ),
        Container(
            name='validInvalid_22',
            raw_bytes="ef000101000802000200040005040001000080000000000001e30001005b600056e4ef",
            validity_error=EOFException.UNDEFINED_INSTRUCTION,
        ),
        Container(
            name='validInvalid_23',
            raw_bytes="ef000101000802000200040007040001000080000000000001e30001005b6001600057e4ef",
            validity_error=EOFException.UNDEFINED_INSTRUCTION,
        ),
        Container(
            name='validInvalid_24',
            raw_bytes="ef00010100040200010006040001000080000260016002ff00ef",
            validity_error=EOFException.UNDEFINED_INSTRUCTION,
        ),
        Container(
            name='validInvalid_25',
            raw_bytes="ef0001010004020001001004000100008000076001600260036004600560066007f200ef",
            validity_error=EOFException.UNDEFINED_INSTRUCTION,
        ),
        Container(
            name='validInvalid_26',
            raw_bytes="ef000101000802000200040004040001000080000000000000e3000100e00010e4ef",
            validity_error=EOFException.INVALID_RJUMP_DESTINATION,
        ),
        Container(
            name='validInvalid_27',
            raw_bytes="ef000101000802000200040004040001000080000000000000e3000100e0ff00e4ef",
            validity_error=EOFException.INVALID_RJUMP_DESTINATION,
        ),
        Container(
            name='validInvalid_28',
            raw_bytes="ef000101000c02000300060004000104000100008000000000000000800000e30001e50002e00001e400ef",
            validity_error=EOFException.INVALID_RJUMP_DESTINATION,
        ),
        Container(
            name='validInvalid_29',
            raw_bytes="ef000101000c02000300060004000104000100008000000000000000800000e30001e50002e0fffce400ef",
            validity_error=EOFException.INVALID_RJUMP_DESTINATION,
        ),
        Container(
            name='validInvalid_30',
            raw_bytes="ef000101000802000200060007040001000080000200020003e30001505000600160026003e4ef",
            validity_error=EOFException.STACK_HIGHER_THAN_OUTPUTS,
        ),
        Container(
            name='validInvalid_31',
            raw_bytes="ef000101000802000200040008040001000080000000000001e3000100e0000160ff60ffe4ef",
            validity_error=EOFException.INVALID_RJUMP_DESTINATION,
        ),
        Container(
            name='validInvalid_32',
            raw_bytes="ef000101000802000200040009040001000080000000000001e30001006001e1000160ff50e4ef",
            validity_error=EOFException.INVALID_RJUMP_DESTINATION,
        ),
        Container(
            name='validInvalid_33',
            raw_bytes="ef0001010004020001001304000100008000016001e204000000010001000200010060ff5000ef",
            validity_error=EOFException.INVALID_RJUMP_DESTINATION,
        ),
        Container(
            name='validInvalid_34',
            raw_bytes="ef0001010004020001001304000100008000016001e204000000010001fffe00010060ff5000ef",
            validity_error=EOFException.INVALID_RJUMP_DESTINATION,
        ),
        Container(
            name='validInvalid_35',
            raw_bytes="ef000101000402000100050400010000800000e000010000ef",
            validity_error=EOFException.UNREACHABLE_INSTRUCTIONS,
        ),
        Container(
            name='validInvalid_36',
            raw_bytes="ef0001010004020001000a04000100008000016001e100020000305000ef",
            validity_error=EOFException.UNREACHABLE_INSTRUCTIONS,
        ),
        Container(
            name='validInvalid_37',
            raw_bytes="ef0001010004020001000f04000100008000016001e2010002000430500000305000ef",
            validity_error=EOFException.UNREACHABLE_INSTRUCTIONS,
        ),
        Container(
            name='validInvalid_38',
            raw_bytes="ef00010100080200020005000304000100008000010200000230e30001005050e4ef",
            validity_error=EOFException.STACK_UNDERFLOW,
        ),
        Container(
            name='validInvalid_39',
            raw_bytes="ef0001010004020001000804000100008000046000600060006000ef",
            validity_error=EOFException.MISSING_STOP_OPCODE,
        ),
        Container(
            name='validInvalid_40',
            raw_bytes="ef000101000402000100090400010000800004600060006000600001ef",
            validity_error=EOFException.MISSING_STOP_OPCODE,
        ),
        Container(
            name='validInvalid_41',
            raw_bytes="ef000101000402000100090400010000800004600060006000600034ef",
            validity_error=EOFException.MISSING_STOP_OPCODE,
        ),
        Container(
            name='validInvalid_42',
            raw_bytes="ef000101000402000100090400010000800004600060006000600003ef",
            validity_error=EOFException.MISSING_STOP_OPCODE,
        ),
        Container(
            name='validInvalid_43',
            raw_bytes="ef0001010004020001000d0400010000800006600060006000600060006000a4ef",
            validity_error=EOFException.MISSING_STOP_OPCODE,
        ),
        Container(
            name='validInvalid_44',
            raw_bytes="ef0001010004020001000304000100008000013050e4ef",
            validity_error=EOFException.INVALID_NON_RETURNING_FLAG,
        ),
        Container(
            name='validInvalid_46',
            raw_bytes="ef0001010008020002000600050400010000800001000000023050e300010030305050e4ef",
        ),
        Container(
            name='validInvalid_47',
            raw_bytes="ef0001010010020004000600060006000304000100008000010000000100000001000000013050e30001003050e30002e43050e30003e43050e4ef",
        ),
        Container(
            name='validInvalid_48',
            raw_bytes="ef000101000402000100030400060000800001305000ef",
            validity_error=EOFException.TOPLEVEL_CONTAINER_TRUNCATED,
        ),
        Container(
            name='validInvalid_49',
            raw_bytes="ef000101000402000100010400010000800000feef",
        ),
        Container(
            name='validInvalid_50',
            raw_bytes="ef0001010004020001000504000100008000023030505000ef",
        ),
        Container(
            name='validInvalid_51',
            raw_bytes="ef000101000c0200030036000b001f04000100008003ff000a000a00640064e30002e30002e30002e30002e30002e30002e30002e30002e30002e3000230303030303030303030303030303030303030303030300030303030303030303030e4e30001e30001e30001e30001e30001e30001e30001e30001e30001e30001e4ef",
        ),
        Container(
            name='validInvalid_52',
            raw_bytes="ef00010100080200020005000404000100008000010100000230e3000100300150e4ef",
        ),
        Container(
            name='validInvalid_53',
            raw_bytes="ef0001010008020002000700040400010000800001000100023050e300015000303001e4ef",
        ),
        Container(
            name='validInvalid_54',
            raw_bytes="ef0001010004020001000504000100008000023030015000ef",
        ),
        Container(
            name='validInvalid_55',
            raw_bytes="ef0001010004020001000504000100008000013050e50000ef",
        ),
        Container(
            name='validInvalid_56',
            raw_bytes="ef00010100080200020006000204000100008000010100000160ffe300010050e4ef",
        ),
        Container(
            name='validInvalid_57',
            raw_bytes="ef0001010008020002000600050400010000800002020000035f80e300010081505050e4ef",
        ),
        Container(
            name='validInvalid_58',
            raw_bytes="ef0001010008020002000600040400010000800002020000025f80e3000100905050e4ef",
        ),
        Container(
            name='validInvalid_59',
            raw_bytes="ef000101000802000200030004040001000080000000800000e50001e0000000ef",
        ),
        Container(
            name='validInvalid_60',
            raw_bytes="ef000101000802000200040009040001000080000000000001e30001006001e10001e4e0fffcef",
        ),
        Container(
            name='validInvalid_61',
            raw_bytes="ef000101000802000200040007040001000080000000000000e3000100e00000e00000e4ef",
        ),
        Container(
            name='validInvalid_62',
            raw_bytes="ef000101000802000200030007040001000080000000800001e500016000e100003000ef",
        ),
        Container(
            name='validInvalid_63',
            raw_bytes="ef000101000802000200030009040001000080000000800001e500016000e1000230503000ef",
        ),
        Container(
            name='validInvalid_65',
            raw_bytes="ef000101000802000200030008040001000080000000800002e500016000e10001303000ef",
        ),
        Container(
            name='validInvalid_66',
            raw_bytes="ef000101000802000200050003040001000080000100010001e30001500060ffe4ef",
        ),
        Container(
            name='validInvalid_67',
            raw_bytes="ef0001010004020001000f04000100008000016001e2040000000000000000000000ef",
        ),
        Container(
            name='validInvalid_68',
            raw_bytes="ef0001010004020001001204000100008000016001e2040000000100010000000100305000ef",
        ),
        Container(
            name='validInvalid_69',
            raw_bytes="ef000101000402000100040400010000800000e0000000ef",
        ),
        Container(
            name='validInvalid_7',
            raw_bytes="ef000101000802000100030400010000800001305000ef",
            validity_error=EOFException.INVALID_SECTION_BODIES_SIZE,
        ),
        Container(
            name='validInvalid_70',
            raw_bytes="ef0001010004020001000904000100008000016001e1000100305000ef",
        ),
        Container(
            name='validInvalid_71',
            raw_bytes="ef0001010004020001000f04000100008000016001e2010002000430503050305000ef",
        ),
        Container(
            name='validInvalid_72',
            raw_bytes="ef0001010008020002000600030400010000800002020000023030e30001005050e4ef",
        ),
        Container(
            name='validInvalid_73',
            raw_bytes="ef000101000402000100090400010000800004600060006000600000ef",
        ),
        Container(
            name='validInvalid_74',
            raw_bytes="ef0001010004020001000904000100008000046000600060006000f3ef",
        ),
        Container(
            name='validInvalid_75',
            raw_bytes="ef0001010004020001000904000100008000046000600060006000fdef",
        ),
        Container(
            name='validInvalid_76',
            raw_bytes="ef0001010004020001000904000100008000046000600060006000feef",
        ),
        Container(
            name='validInvalid_8',
            raw_bytes="ef000101000402000100030400010000800001305000000bad",
            validity_error=EOFException.INVALID_SECTION_BODIES_SIZE,
        ),
        Container(
            name='validInvalid_9',
            raw_bytes="ef000101000302000100030400010000800001305000ef",
            validity_error=EOFException.INVALID_TYPE_SECTION_SIZE,
        ),
    ],
    ids=lambda x: x.name,
)
def test_eof_validation(eof_test, container):
    eof_test(container=container)
