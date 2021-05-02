#!/bin/sh

# Execute each test case in this directory.
for file in *.py; do ./"$file"; done
