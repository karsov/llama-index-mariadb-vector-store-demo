# LlamaIndex MariaDB Vector Store Demo

## Usage

### Install the dependencies

```shell
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Run the MariaDB container

```shell
docker compose up
```

### Run the Python script

Before running the demo script, make sure you have set the `OPENAI_API_KEY` environment variable either via `export` or in a `.env` file.

```shell
# The first time, initialize the vector store
python demo.py --init-store

# Then, you can use the already initialized vector store
python demo.py

# If you want to use the LLM query engine on top of the vector search, use the following command
python demo.py --use-llm

# To explore the MariaDB table used as the backend of the vector store
mariadb -h 127.0.0.1 -u root -ptest test 
```

### Clean up

```shell
docker compose down
```
