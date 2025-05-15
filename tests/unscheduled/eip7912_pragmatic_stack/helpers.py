"""A collection of helpers used in 7912 EOF tests."""

import itertools

"""Storage addresses for common testing fields"""
_slot = itertools.count()
next(_slot)  # don't use slot 0
slot_code_worked = next(_slot)

slot_last_slot = next(_slot)

value_code_worked = 0x2015
value_canary_should_not_change = 0x2019
value_canary_to_be_overwritten = 0x2009
