#!/bin/bash
#
# (c) $year$ $name$
#
# This file is part of $name$,
# released under Apache License Version 2.0 (http://www.apache.org/licenses/LICENCE).
#

set -e

export C_FORCE_ROOT=true

/opt/$name$/docker/wait-mysql.py
exec celery -A $name$ worker --concurrency 1 --no-color --loglevel=INFO
