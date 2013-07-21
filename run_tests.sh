#!/bin/bash

PYTHONPATH=".:$PYTHONPATH"


echo '=== pyflakes ==='
pyflakes ./concon.py || exit $?
echo 'pyflakes completed.'


echo -e '\n=== Running unittests ==='
TRIAL=$(which trial)

if ! [ -x "$TRIAL" ];
then
    echo 'Could not find trial; it is in the Twisted package.'
    exit -1
fi


coverage run --branch ./concon.py --verbose
STATUS=$?

echo -e '\n--- Generating Coverage Report ---'
coverage html --include='concon*'

echo 'Report generated.'

[ "$STATUS" -eq 0 ] || exit $STATUS

exit "$STATUS"
