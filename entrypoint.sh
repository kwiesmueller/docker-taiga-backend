#!/bin/bash

set -e

public_hostname=${PUBLIC_HOSTNAME:-'taiga.benjamin-borbe.de'}
public_register_enabled=${PUBLIC_REGISTER_ENABLED:-'False'}

default_from=${default_from:-'smtp@benjamin-borbe.de'}

database_host=${DATABASE_HOST:-'taiga-postgres'}
database_name=${DATABASE_NAME:-'taiga'}
database_user=${DATABASE_USER:-'taiga'}
database_password=${DATABASE_PASSWORD:-'Bri72GuWPpaly1qu'}
database_port=${DATABASE_PORT:-'5432'}

smtp_host=${SMTP_HOST:-'smtp'}
smtp_port=${SMTP_PORT:-'25'}

secret_key=${SECRET_KEY:-'Z2nwo3KDU24Qie7jX2uStFuukaJ92JFO'}

sed_script=""
for var in public_register_enabled public_hostname default_from database_host database_name database_user database_password database_port smtp_host smtp_port secret_key; do
  sed_script+="s,{{$var}},${!var},g;"
done

echo "create local.py"
cat /taiga/settings/local.py.template | sed -e "$sed_script" > /taiga/settings/local.py

echo "create static"
cd /taiga && python manage.py collectstatic --noinput

echo "migrate database"
python manage.py migrate

echo "starting django $@"
exec "$@"
