#!/usr/bin/env python
# Copyright 2024 Remy Blank <remy@c-space.org>
# SPDX-License-Identifier: CC-BY-NC-SA-4.0

import pathlib
import re
import sys


digits_re_bytes = re.compile(br'(\d+)')
digits_re_str = re.compile(r'(\d+)')


def natural_sort(s):
    pat = digits_re_bytes if isinstance(s, bytes) else digits_re_str
    parts = pat.split(s)
    parts[1::2] = map(int, parts[1::2])
    return parts


def make_entries(names):
    return [f'<a href="{name}">{name}</a>'
            for name in sorted(names, key=natural_sort)]


def main(argv):
    for dirpath, dirnames, filenames in pathlib.Path(argv[1]).walk():
        dest = dirpath / 'index.html'
        print(f"Generating {dest}")
        entries = make_entries([f'{n}/' for n in dirnames])
        entries += make_entries([n for n in filenames if n != 'index.html'])
        entries = ''.join(f'{e}\n' for e in entries)
        dest.write_text(f"""\
<!DOCTYPE html>
<html lang="en">
<!-- Copyright 2024 Remy Blank <remy@c-space.org> -->
<!-- SPDX-License-Identifier: CC-BY-NC-SA-4.0 -->
<head>
  <meta charset="utf-8">
  <title>Index of /{dirpath}</title>
</head>
<body>
<h1>Index of /{dirpath}</h1>
<pre>
{entries}</pre>
</body>
</html>
""")


if __name__ == '__main__':
    sys.exit(main(sys.argv))
