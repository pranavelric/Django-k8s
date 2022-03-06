[![Django & Kubernetes Logo](https://d33wubrfki0l68.cloudfront.net/4c72e1c6194c527ec80d559eacff223825020194/751c4/img/blog/2019-10-18-deploy-django-to-kubernetes/header-django-kubernetes-tutorial.png)]()
# Django & Kubernetes

Deploy a Django application into a Kubernetes cluster in Digital Ocean.



## Cloning this Repo?
Make sure you create `web/.env` and fill in the following variables:

```
DEBUG=1
REGION=texas
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_PASSWORD=mydjangopw
DJANGO_SUERPUSER_EMAIL=hello@temp.com
DJANGO_SECRET_KEY=fix_this_later
POSTGRES_READY=0
POSTGRES_DB=dockerdb
POSTGRES_PASSWORD=mysecretpassword
POSTGRES_USER=myuser
POSTGRES_HOST=localhost
POSTGRES_PORT=5434
REDIS_HOST=redis_db
REDIS_PORT=6388
```
> If you change `POSTGRES_PORT` or `REDIS_PORT` be sure to update those values in `docker-compose.yaml`
Once you have the above `.env` file, navigate to your project root (right where `docker-compose.yaml` is) and run:

```
docker compose up -d
```
This will create a `postgresql` database that's running in the background for you. To bring this database down just run:

```
docker compose down
```
The data in the database will be persistent so you can run `docker compose up -d` again with confidence. 


Also in the root of your project:

```
python3.6 -m venv venv
source venv/bin/activate
pip install -r web/requirements.txt
```
This will ensure your Django project is ready to be used locally.
