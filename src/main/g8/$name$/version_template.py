#
# (c) $year$ $name$
#
# This file is part of $name$,
# released under Apache License Version 2.0 (http://www.apache.org/licenses/LICENCE).
#

import pkg_resources


try:
    VERSION = pkg_resources.require('$name$')[0].version
except:
    VERSION = None

GIT_REVISION = '{{ git_revision }}'
