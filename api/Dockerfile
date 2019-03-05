FROM tiangolo/uwsgi-nginx:python3.5

# set location of ini file
ENV UWSGI_INI uwsgi.ini

# create uwsgi log dir
RUN mkdir /uwsgi
RUN touch /uwsgi/uwsgi.log

# create api dir
RUN mkdir /api
WORKDIR /api

EXPOSE 80