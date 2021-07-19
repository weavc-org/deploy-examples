#!/bin/bash
set -e

# this runs after setting up database etc, remove current database
rm -rf /var/lib/postgresql/data/*

# take a backup of master postgres database into our database directory
# this also creates a recovery configuration file
pg_basebackup --host postgres -D /var/lib/postgresql/data -P -U repl -Fp -R

