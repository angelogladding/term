# [`term`][1]: tools for a metamodern terminal environment
# Copyright (c) MMXVIII- @[Angelo Gladding][2]
#
# This program is free software: it is distributed in the hope that it
# will be useful, but *without any warranty*; without even the implied
# warranty of merchantability or fitness for a particular purpose. You
# can redistribute it and/or modify it under the terms of the @@[GNU's
# Not Unix][3] [Affero General Public License][4] as published by the
# @@[Free Software Foundation][5], either version 3 of the License, or
# any later version.
#
# *[GNU]: GNU's Not Unix
#
# [1]: //lahacker.net/code/term
# [2]: //lahacker.net
# [3]: //gnu.org
# [4]: //gnu.org/licenses/agpl
# [5]: //fsf.org

from setuptools import setup

setup(requires=["argcomplete", "sh"],
      discover=__file__)
