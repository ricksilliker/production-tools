.PHONY: run
run:
	docker stop tiny-pipeline-api && docker rm tiny-pipeline-api
	docker build -t tiny-pipeline-api ./backend
	docker run -d -p 8080:8080 tiny-pipeline-api


.PHONY: run-local
run-local:
	pip install -r ./backend/requirements.txt
	cd backend && python app.py