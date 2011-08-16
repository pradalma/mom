#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import unittest2
from mom.os.patterns import \
    match_path_against, _match_path, match_path, filter_paths, match_any_paths

class Test_match_path_against(unittest2.TestCase):
    def test_all(self):
        self.assertTrue(match_path_against(
            "/home/username/foobar/blah.py", ["*.py", "*.txt"], False))
        self.assertFalse(match_path_against(
            "/home/username/foobar/blah.py", ["*.PY", "*.txt"], True))
        self.assertTrue(match_path_against(
            "/home/username/foobar/blah.py", ["*.PY", "*.txt"], False))
        self.assertFalse(match_path_against(
            "C:\\windows\\blah\\BLAH.PY", ["*.py", "*.txt"]))
        self.assertTrue(match_path_against(
            "C:\\windows\\blah\\BLAH.PY", ["*.py", "*.txt"], False))

class Test__match_path(unittest2.TestCase):
    def test_all(self):
        self.assertTrue(_match_path("/users/gorakhargosh/foobar.py",
            ["*.py"], ["*.PY"]))
        self.assertFalse(_match_path("/users/gorakhargosh/FOOBAR.PY",
            ["*.py"], ["*.PY"], True))
        self.assertFalse(_match_path("/users/gorakhargosh/foobar/",
            ["*.py"], ["*.txt"], False))

    def test_ValueError_when_conflicting_patterns(self):
        self.assertRaises(ValueError, _match_path,
                          "/users/gorakhargosh/FOOBAR.PY", ["*.py"], ["*.PY"],
                          False)

class Test_match_path(unittest2.TestCase):
    def test_all(self):
        self.assertTrue(match_path("/Users/gorakhargosh/foobar.py"))
        self.assertTrue(match_path("/Users/gorakhargosh/foobar.py",
                                   case_sensitive=False))
        self.assertTrue(match_path("/users/gorakhargosh/foobar.py",
                                   ["*.py"], ["*.PY"], True))
        self.assertFalse(match_path("/users/gorakhargosh/FOOBAR.PY",
                                    ["*.py"], ["*.PY"], True))
        self.assertFalse(match_path("/users/gorakhargosh/foobar/",
                                    ["*.py"], ["*.txt"], False))

    def test_ValueError_when_conflicting_patterns(self):
        self.assertRaises(ValueError, match_path,
                          "/users/gorakhargosh/FOOBAR.PY",
                          ["*.py"], ["*.PY"], False)


class Test_filter_paths(unittest2.TestCase):
    def test_all(self):
        pathnames = set(["/users/gorakhargosh/foobar.py",
                         "/var/cache/pdnsd.status",
                         "/etc/pdnsd.conf",
                         "/usr/local/bin/python"])
        self.assertEqual(set(filter_paths(pathnames)), pathnames)
        self.assertEqual(set(filter_paths(pathnames, case_sensitive=False)),
                         pathnames)
        self.assertEqual(set(filter_paths(pathnames,
                                          ["*.py", "*.conf"],
                                          ["*.status"],
                                          case_sensitive=True)),
                         set(["/users/gorakhargosh/foobar.py",
                              "/etc/pdnsd.conf"]))

class Test_match_any_paths(unittest2.TestCase):
    def test_all(self):
        pathnames = set([
            "/users/gorakhargosh/foobar.py",
            "/var/cache/pdnsd.status",
            "/etc/pdnsd.conf",
            "/usr/local/bin/python"]
        )
        self.assertTrue(match_any_paths(pathnames))
        self.assertTrue(match_any_paths(pathnames, case_sensitive=False))
        self.assertTrue(match_any_paths(pathnames, ["*.py", "*.conf"],
            ["*.status"],
            case_sensitive=True))
        self.assertFalse(match_any_paths(pathnames, ["*.txt"],
            case_sensitive=False))
        self.assertFalse(match_any_paths(pathnames, ["*.txt"],
                                         case_sensitive=True))
        