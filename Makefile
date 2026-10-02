.PHONY: celery
celery:
	docker compose up -d --force-recreate worker
	docker compose logs -f worker

.PHONY: run
run:
	poetry run python run.py