#!/usr/bin/env bash

for file in data/*.sql; do
    temp_filename=$(basename "$file")
    filename="${temp_filename%.*}"
    psql -f "${file}" >"nf/$filename.txt"
done
