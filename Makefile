all: init run

init:
		pip install -r requirements.txt

run:
		python3 sample/main.py
