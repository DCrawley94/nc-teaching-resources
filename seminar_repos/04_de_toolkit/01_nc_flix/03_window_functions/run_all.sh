#!/usr/bin/env bash

SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &>/dev/null && pwd)
TASK_DIR="$SCRIPT_DIR/tasks"

for file in "$TASK_DIR"/*.sql; do
    temp_file_name=$(basename "$file")
    file_name=${temp_file_name%.*}
    psql -f "$file" >"$TASK_DIR"/"$file_name".txt
done
