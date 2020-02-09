# -*- coding: utf-8 -*-
"""Namespace: ZeekygenExample."""

import enum


@enum.unique
class SimpleEnum(enum.IntFlag):
    """Documentation for the “SimpleEnum” type goes here.
    It can span multiple lines.

    
    c.f. {html_path}
    """

    _ignore_ = 'SimpleEnum _'
    SimpleEnum = vars()

    # Documentation for particular enum values is added like this.
    # And can also span multiple lines.
    SimpleEnum['ONE'] = enum.auto()

    # Or this style is valid to document the preceding enum value.
    SimpleEnum['TWO'] = enum.auto()

    SimpleEnum['THREE'] = enum.auto()

    # And some documentation for “FOUR”.
    SimpleEnum['FOUR'] = enum.auto()

    # Also “FIVE”.
    SimpleEnum['FIVE'] = enum.auto()