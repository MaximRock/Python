#!/bin/bash
set -e

FILE=./src

if [ -d "$FILE" ]; 
then
    echo "
    ==== $FILE - is a directory. ===="
else mkdir "$FILE" 
    echo "
    ==== $FILE - directory created. ====";
fi

cd ../test-koshelek-ru-selenium

echo "
    ==== installation vmbox ubuntu 22.04 ===="

vagrant up qa