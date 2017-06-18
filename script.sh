#!/bin/sh
egrep "^$1$" /usr/share/dict/words

if [ $? -eq 0 ]; then
    echo Bad Password
else
    echo Maybe a good password
fi
