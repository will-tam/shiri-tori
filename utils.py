#!/usr/bin/python3
# -*- coding: utf-8 -*-

######################

def xor(a, b):
    """
    Find a XOR b.
    @parameters : a = first term.
                  b = second term.
    @return : a XOR B it self.
    """
    return (not a) & b | a & (not b)
