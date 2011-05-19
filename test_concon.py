#! /usr/bin/env python

import unittest

from concon import ConstraintError, OverwriteError
from concon import frozendict, frozenlist, frozenset
from concon import appendonlydict, appendonlylist, appendonlyset
from concon import define_constrained_subtype, setitem_without_overwrite, update_without_overwrite


class SetItemWithoutOverwriteTests (unittest.TestCase):

    def test__setitem_without_overwrite__no_overwrite(self):
        d = {'a': 'apple'}
        setitem_without_overwrite(d, 'b', 'banana')
        self.assertEqual(d, {'a': 'apple', 'b': 'banana'})

    def test__setitem_without_overwrite__with_overwrite(self):
        d = {'a': 'apple'}
        try:
            setitem_without_overwrite(d, 'a', 'applause')
        except OverwriteError, e:
            self.assertEqual(e.args, ('a', 'applause', 'apple'))
            self.assertEqual(
                str(e),
                "Attempted overwrite of key 'a' with new value 'applause' overwriting old value 'apple'")
        else:
            self.fail('setitem_without_overwrite allowed overwrite: %r' % (d,))


if __name__ == '__main__':
    unittest.main()
