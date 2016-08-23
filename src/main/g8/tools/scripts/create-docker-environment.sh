#!/bin/bash
#
# (c) $year$ $name$
#
# This file is part of $name$,
# released under Apache License Version 2.0 (http://www.apache.org/licenses/LICENCE).
#

source=\$(cd \$(dirname "\$0")/../.. && pwd)
destination=\$1

mkdir -p \$destination/config

cp \$source/docker-compose.yml \$destination/docker-compose.yml
cp \$source/docker/env.template \$destination/env
cp \$source/docker/$name$_settings_template.py \$destination/config/$name$_settings.py
