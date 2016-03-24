#!/bin/bash

set -e

database_host=${DATABASE_HOST:-'taiga-postgres.default.svc.cluster.local'}
database_name=${DATABASE_NAME:-'taiga'}
database_user=${DATABASE_USER:-'taiga'}
database_password=${DATABASE_PASSWORD:-'Bri72GuWPpaly1qu'}
database_port=${DATABASE_PORT:-'5432'}

smtp_host=${SMTP_HOST:-'smtp.default.svc.cluster.local'}
smtp_port=${SMTP_PORT:-'25'}

secret_key=${SECRET_KEY:-'Z2nwo3KDU24Qie7jX2uStFuukaJ92JFO'}

sed_script=""
for var in database_host database_name database_user database_password database_port smtp_host smtp_port secret_key; do
  sed_script+="s,{{$var}},${!var},g;"
done

echo "create local.py"
cat /taiga/settings/local.py.template | sed -e "$sed_script" > /taiga/settings/local.py

exec "$@"