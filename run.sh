cd src
export ELECTRUM_USER=electrumgithub
export ELECTRUM_PASSWORD=electrumgithubpassword
python run.py
# uvicorn run:app --host 0.0.0.0 --port 7000 --reload