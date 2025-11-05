all: init run

init:
		pip install -r requirements.txt --break-system-packages

run:
		python3 sample/main.py
