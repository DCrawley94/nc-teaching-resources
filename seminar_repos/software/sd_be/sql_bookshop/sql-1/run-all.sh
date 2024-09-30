#!/bin/bash
for file in "./"*.sql; do
    psql -f "${file}" > ./outputs/${file%.sql}.txt
done