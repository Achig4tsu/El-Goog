#!/usr/bin/env bash
#   Use this script to test if a given TCP host/port are available

# wait-for-it.sh mariadb:3306 -- /usr/src/app/venv/bin/python /usr/src/app/main.py

set -e

host="mariadb"
shift
port="3306"
shift

cmd="$@"

until nc -z "$host" "$port"; do
  >&2 echo "MariaDB is unavailable - sleeping"
  sleep 1
done

>&2 echo "MariaDB is up - executing command"
exec $cmd
