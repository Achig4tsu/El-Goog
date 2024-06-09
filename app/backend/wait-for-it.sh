#!/bin/bash

host="$1"
shift
cmd="$@"

until mysql -h "$host" -u "root" -p"password" -e "select 1" > /dev/null 2>&1; do
  >&2 echo "MariaDB is unavailable - sleeping"
  sleep 1
done

>&2 echo "MariaDB is up - executing command"
exec $cmd
