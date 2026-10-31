#!/usr/bin/env python3
"""Verify selected ACS PUMS sample counts; pass path to psam_p25.csv."""
import collections
import csv
import hashlib
import sys
from pathlib import Path

path = Path(sys.argv[1])
cols = ('PUMA', 'AGEP', 'SEX', 'MAR', 'CIT', 'OCCP')
with path.open(newline='', encoding='utf-8') as source:
    rows = list(csv.DictReader(source))
n = len(rows)
occ = collections.Counter(row['OCCP'] for row in rows)
groups = collections.Counter(tuple(row[col] or 'NA' for col in cols) for row in rows)
singletons = sum(size == 1 for size in groups.values())
print('person CSV sha256:', hashlib.sha256(path.read_bytes()).hexdigest())
print('rows:', n)
print('OCCP nonempty values:', len(occ) - int('' in occ))
print('OCCP blank:', occ[''])
print('OCCP 0440:', occ['0440'])
for i, col in enumerate(cols, start=1):
    categories = len({row[col] or 'NA' for row in rows})
    observed = len({tuple(row[k] or 'NA' for k in cols[:i]) for row in rows})
    print('prefix:', '+'.join(cols[:i]), 'new field categories:', categories, 'observed groups:', observed)
print('six-field groups:', len(groups))
print('singletons:', singletons, 'percentage:', 100 * singletons / n)
print('mean group size for a randomly selected row:', sum(v*v for v in groups.values()) / n)
