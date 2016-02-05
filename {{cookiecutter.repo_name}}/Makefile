bootstrap:
		mkdir -p var/log
		mkdir -p var/www/static
		mkdir -p var/www/media
		mkdir -p etc
		cp .example-env etc/.{{ cookiecutter.repo_name }}-env


virtualenv:
		virtualenv env --python=python3
		env/bin/pip install --upgrade pip

install:
		env/bin/pip install -r requirements/development.txt


migrate:
		env/bin/python manage.py migrate
