#!/usr/bin/env python
#
# (c) $year$ $name$
#
# This file is part of $name$,
# released under Apache License Version 2.0 (http://www.apache.org/licenses/LICENCE).
#

import argparse
import sys

import jinja2


def entry(text):
    return text.split('=', 1)


def main():
    #
    parser = argparse.ArgumentParser()
    parser.add_argument('template')
    parser.add_argument('entries', metavar='entry', nargs='*', type=entry)
    args = parser.parse_args()

    #
    context = {key: value for key, value in args.entries}

    with open(args.template) as fin:
        template = jinja2.Template(fin.read())
        sys.stdout.write(template.render(context))


if __name__ == '__main__':
    main()
