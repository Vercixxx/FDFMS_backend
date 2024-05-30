#!/bin/bash

for dir in */; do

    if [ -d "${dir}migrations" ]; then
        echo "Czyszczenie ${dir}migrations..."

        find "${dir}migrations" -mindepth 1 -maxdepth 1 -exec rm -rf {} +

        touch "${dir}migrations/__init__.py"

        echo "Zakończono czyszczenie ${dir}migrations."
    fi
done

echo "Zakończono czyszczenie migrations w każdym katalogu."

