test:
	django-admin.py test --settings=chatovod.test_settings chatovod
coverage:
	export DJANGO_SETTINGS_MODULE=chatovod.test_settings && \
	coverage run --branch --source=chatovod `which django-admin.py` test chatovod && \
	coverage report --omit="chatovod/test*"
pep8:
	flake8 chatovod
sphinx:
	cd docs && sphinx-build -b html -d .build/doctrees . .build/html
