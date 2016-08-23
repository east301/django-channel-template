#!/bin/bash
#
# (c) $year$ $name$
#
# This file is part of $name$,
# released under Apache License Version 2.0 (http://www.apache.org/licenses/LICENCE).
#

set -e

/opt/$name$/docker/wait-mysql.py
exec $name$-cli runworker --no-color
