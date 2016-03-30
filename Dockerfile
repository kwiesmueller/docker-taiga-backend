FROM python:3.4.3
MAINTAINER Benjamin Borbe <bborbe@rocketnews.de>

RUN set -x \
    && apt-get update --quiet \
    && apt-get install --quiet --yes --no-install-recommends gettext \
    && apt-get clean

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
