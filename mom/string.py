#!/usr/bin/env python
# -*- coding: utf8 -*-
#
# Copyright (C) 2011 Yesudeep Mangalapilly <yesudeep@gmail.com>
# Copyright (C) 2012 Google, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
:module: mom.string
:synopsis: string module compatibility.

"""

from __future__ import absolute_import

ASCII_UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ASCII_LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
ASCII_LETTERS = ASCII_LOWERCASE + ASCII_UPPERCASE
DIGITS = "0123456789"

PUNCTUATION = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
PRINTABLE = '0123456789abcdefghijklmnopqrstuvwxyz\
ABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
WHITESPACE = '\t\n\x0b\x0c\r '
