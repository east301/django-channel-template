#
# (c) $year$ $name$
#
# This file is part of $name$,
# released under Apache License Version 2.0 (http://www.apache.org/licenses/LICENCE).
#

from channels.asgi import get_channel_layer

from .apps.common.config import configure_settings_module_path


configure_settings_module_path()
channel_layer = get_channel_layer()
