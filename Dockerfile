FROM python:3.4.3
MAINTAINER Benjamin Borbe <bborbe@rocketnews.de>

RUN git clone -b stable --single-branch https://github.com/taigaio/taiga-back.git /taiga

ENV HOME /taiga
WORKDIR /taiga

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

ADD local.py /taiga/settings/local.py

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
