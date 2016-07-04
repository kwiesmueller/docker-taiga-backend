FROM python:3.4.3
MAINTAINER Benjamin Borbe <bborbe@rocketnews.de>

RUN set -x \
	&& DEBIAN_FRONTEND=noninteractive apt-get update --quiet \
	&& DEBIAN_FRONTEND=noninteractive apt-get upgrade --quiet --yes \
	&& DEBIAN_FRONTEND=noninteractive apt-get install --quiet --yes --no-install-recommends gettext postgresql \
	&& DEBIAN_FRONTEND=noninteractive apt-get autoremove --yes \
	&& DEBIAN_FRONTEND=noninteractive apt-get clean

RUN git clone -b stable --single-branch https://github.com/taigaio/taiga-back.git /taiga

ENV HOME /taiga
WORKDIR /taiga

#RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

ADD local.py /taiga/settings/local.py.template

RUN python manage.py compilemessages

EXPOSE 8000

COPY entrypoint.sh /usr/local/bin/
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
