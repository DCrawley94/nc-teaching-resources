#!/usr/bin/env bash

psql -f sql/create_database.sql >outputs/db_setup.txt
