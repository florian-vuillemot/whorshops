FROM python:3.8-buster AS base

# Create tag user and group tag
WORKDIR /src

# Install printer dependancies
RUN apt update -y

# Be sure to install latest pip
RUN python -m pip install --upgrade pip

# Install webserver dependancy
RUN pip install gunicorn[gevent]

# Copy application
COPY ./tags /src
# Install application dependancies
RUN pip install pipenv==2018.11.26 && pipenv install --system --deploy

#RUN python manage.py collectstatic --noinput
#RUN python manage.py check --deploy

#############################################
################ DATABASE ###################
#############################################
FROM base AS appli_migration
CMD python manage.py migrate


#############################################
################## TESTS ####################
#############################################
FROM base AS test
RUN python manage.py test


#############################################
################### RUN #####################
#############################################
FROM base AS run
EXPOSE 8000
CMD ["gunicorn", "-c", "gunicorn.py", "tags.wsgi"]
