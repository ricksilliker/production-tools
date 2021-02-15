.PHONY: run
run:
	docker stop tiny-pipeline-api && docker rm tiny-pipeline-api
	docker build -t tiny-pipeline-api ./backend
	docker run -d -p 8080:8080 tiny-pipeline-api


.PHONY: run-local
run-local:
	pip install -r ./backend/requirements.txt
	cd backend && python app.py


.PHONY: backup-db
backup-db:
	docker exec -t production-tools_db_1 pg_dumpall -c -U postgres > dump_`date +%d-%m-%Y"_"%H_%M_%S`.sql


.PHONY: restore-db
restore-db:
	cat $(SQL_FILE) | docker exec -i production-tools_db_1 psql -U postgres