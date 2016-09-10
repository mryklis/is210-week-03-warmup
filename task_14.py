#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" test logical and equality operators """

IS_TRUE = True

IS_FALSE = False

IS_NONE = None

INTEGER_EQUIV= ( IS_TRUE == 1 ) and ( IS_FALSE == 0 )
print INTEGER_EQUIV