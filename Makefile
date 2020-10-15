MSG="New commit"
HOST=localhost
APP_DIR=.
APP_NAME=accounts
PROJECT_DIR=backend

.PHONY : help
help:
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

.PHONY : commit
commit: ## "commit COMMIT_MSG="Commit message" : Add changes to git and commit"
	echo $(MSG)
	git add --all
	git commit -a -S -m "$(MSG)"
	git push



.PHONY : configure
configure: ## "Create virtual env and install requirements"
	python3 -m venv .venv && source .venv/bin/activate && pip install --upgrade pip &&  pip install -r $(PROJECT_DIR)/requirements.txt

.PHONY : djangoshell
djangoshell: ## "Run local django shell"
	source .secrets &&  source .venv/bin/activate && cd $(PROJECT_DIR) && python3 manage.py shell


.PHONY : bash
bash: ## "Run local django shell"
	docker-compose -p backend-api -f $(HOST)-compose.yml exec rest-api bash



.PHONY : runserver
runserver: ## "Run local django devel server"
	source .secrets &&  source .venv/bin/activate && cd $(PROJECT_DIR) && python3 manage.py runserver

.PHONY: login_docker_amazon
login_docker_amazon: ## login docker to amazon
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 509322417204.dkr.ecr.us-east-1.amazonaws.com


.PHONY : amazon_deploy
amazon_deploy: ## "Check linting flake8"
	source .venv/bin/activate &&  flake8 $(PROJECT_DIR)/ --ignore=E501,F401


.PHONY : lint
lint: ## "Check linting flake8"
	source .venv/bin/activate &&  flake8 $(PROJECT_DIR)/ --ignore=E501,F401


.PHONY : create_super_user
create_super_user: ## "run docker-compose exec rest_api python manage.py create_super_user to HOST="localhost" (localhost || amazon)"
	docker-compose -p backend-api -f $(HOST)-compose.yml exec rest-api python manage.py createsuperuser

.PHONY : get_statics
get_statics: ## "run docker-compose exec rest_api python manage.py create_super_user to HOST="localhost" (localhost || amazon)"
	docker-compose -p backend-api -f $(HOST)-compose.yml exec rest-api python manage.py collectstatic



.PHONY : dump_data
dump_data: ## "run docker-compose exec rest_api python manage.py dump_data > initial_data.json to HOST="localhost" (localhost || amazon)"
	docker-compose -p backend-api -f $(HOST)-compose.yml exec rest-api python manage.py dumpdata  sites flatpages accounts  > $(PROJECT_DIR)/initial_data.json



.PHONY : run_docker
run_docker: ## "run docker-compose up to HOST="localhost" (localhost || amazon)"
	docker-compose -p backend-api -f $(HOST)-compose.yml up

.PHONY : build_docker
build_docker: ## "run docker-compose build to HOST="localhost" (localhost || amazon)"
	docker-compose -p backend-api -f $(HOST)-compose.yml build

.PHONY : clean_docker
clean_docker: ## "run docker-compose down -v to HOST="localhost" (localhost || amazon)"
	docker-compose -p backend-api -f $(HOST)-compose.yml down -v


.PHONY : reset_docker
reset_docker: clean_docker build_docker run_docker ## "run clean_docker build_docker run_docker to HOST="localhost" (localhost || amazon)"


.PHONY : test_project
test_project: ## "Run test with coverage"
	source .secrets && source .venv/bin/activate && cd $(PROJECT_DIR) && coverage run  manage.py test


.PHONY : test_app
test_app: ## "Run test with coverage"
	source .secrets && source .venv/bin/activate && cd $(PROJECT_DIR) && coverage run  manage.py test $(APP_NAME)

.PHONY : cover_report
cover_report: ## "show coverage report
	source .venv/bin/activate && cd $(PROJECT_DIR) && coverage report -m

.PHONY : html_report
html_report: ## "show coverage report
	source .venv/bin/activate && cd $(PROJECT_DIR) && coverage html

.PHONY : code_format
code_format: ## "Format code using black -t py38
	source .venv/bin/activate &&  black $(PROJECT_DIR)/ -v -t py38


.PHONY : code_format_check
code_format_check: ## "Check code format with black"
	source .venv/bin/activate &&  black . -v -t py38 --check --diff
