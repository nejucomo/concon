#! /usr/bin/env python

import unittest

# Note, we do not test frozenset.

from concon import ConstraintError, OverwriteError
from concon import frozendict, frozenlist
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


class BlockedMethodsTests (unittest.TestCase):

    def test_frozendict(self):
        self._check_blocked_methods(frozendict({}))

    def test_frozenlist(self):
        self._check_blocked_methods(frozenlist({}))

    # Note, we do not test frozenset.

    def test_appendonlydict(self):
        self._check_blocked_methods(appendonlydict({}))

    def test_appendonlylist(self):
        self._check_blocked_methods(appendonlylist({}))

    def test_appendonlyset(self):
        self._check_blocked_methods(appendonlyset({}))

    def _check_blocked_methods(self, obj):
        for name in obj.get_blocked_method_names():
            method = getattr(obj, name)
            try:
                r = method(42)
            except ConstraintError, e:
                self.assertEqual(e.args, (obj, name, (42,), {}))
                self.assertEqual(
                    str(e),
                    "Attempt to call %r.%s (42,) {} violates constraint." % (obj, name))
            else:
                self.fail('Blocked method %r.%s returned %r' % (obj, name, r))



if __name__ == '__main__':
    unittest.main()
