#!/bin/bash

PYTHONPATH=".:$PYTHONPATH"


echo '=== pyflakes ==='
pyflakes ./concon.py || exit $?
echo 'pyflakes completed.'


echo -e '\n=== Running unittests ==='
coverage run --branch ./concon.py --verbose
STATUS=$?

echo -e '\n--- Generating Coverage Report ---'
coverage html --include='concon*'

echo 'Report generated.'

[ "$STATUS" -eq 0 ] || exit $STATUS

exit "$STATUS"
