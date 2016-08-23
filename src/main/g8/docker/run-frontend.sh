#!/bin/bash
#
# (c) $year$ $name$
#
# This file is part of $name$,
# released under Apache License Version 2.0 (http://www.apache.org/licenses/LICENCE).
#

set -e

/opt/$name$/docker/wait-mysql.py
exec daphne -b 0.0.0.0 -p 8080 $name$.asgi:channel_layer
