#!/bin/true
#
# patches.py - part of autospec
# Copyright (C) 2015 Intel Corporation
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Parse config files
#


patches = []
autoreconf = False


def apply_patches(file):
    counter = 1
    for p in patches:
        name = p.split(None, 1)[0]
        if name == p:
            options = "-p1"
        else:
            options = p.split(None, 1)[1]
        if not p.split()[0].endswith(".nopatch"):
            file.write("%%patch%d %s\n" % (counter, options))
        counter = counter + 1
