#
# (c) $year$ $name$
#
# This file is part of $name$,
# released under Apache License Version 2.0 (http://www.apache.org/licenses/LICENCE).
#

FROM python:3.5-slim
MAINTAINER $author$ <$email$>

ENV VERSION 0.0.0

RUN mkdir -p /opt/$name$
ADD ./docker /opt/$name$/docker

RUN apt-get update\
    && apt-get install -y file gcc\
    && pip install /opt/$name$/docker/$name$-\$VERSION-py3-none-any.whl\
    && pip install -r /opt/$name$/docker/requirements-production.txt\
    && apt-get remove -y gcc\
    && apt-get autoremove -y\
    && apt-get clean -y\
    && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*
