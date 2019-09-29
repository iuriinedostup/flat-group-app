NO_COLOR=\033[0m
WHITE_BOLD=\033[1;37m
YELLOW=\033[1;33m
GREEN=\033[32;01m

.EXPORT_ALL_VARIABLES:

help:
		@echo "\n$(WHITE_BOLD)Revolut Python Challenge - Nester$(NO_COLOR)\n"
		@echo "Please use \`make <target>' where <target> is one of"
		@echo "  setup             	to create virtual environment and install project requirements"
		@echo "  test              	to run code-style checker and tests suit via tox framework"
		@echo "  virtualenv        	to create virtual environment"
		@echo "  clean             	to remove virtual environment"
		@echo "  test-requirements 	to install tox framework in the virtual environment"


setup: clean virtualenv requirements test-requirements

virtualenv:
		virtualenv -p python3 $(CURDIR)/venv

test-requirements:
		$(CURDIR)/venv/bin/pip install tox

requirements:
		$(CURDIR)/venv/bin/pip install -r requirements.txt

clean:
		rm -rf $(CURDIR)/venv

test:
		. $(CURDIR)/venv/bin/activate; tox

.PHONY: clean test virtualenv
