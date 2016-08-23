#
# (c) $year$ $name$
#
# This file is part of $name$,
# released under Apache License Version 2.0 (http://www.apache.org/licenses/LICENCE).
#

import json

from django.core.management import BaseCommand


# ================================================================================
# json
# ================================================================================

class JSONLineOutputCommand(BaseCommand):
    def log(self, **kwargs):
        self.stdout.write(json.dumps(kwargs, sort_keys=True))
