#!/bin/bash
# the allowed methods in an server 
curl -s -I -X OPTIONS "$1" | grep 'Allow:' | cut -f2- -d' '
