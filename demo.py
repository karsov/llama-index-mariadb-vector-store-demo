"""
This is a demo of the MariaDB vector store integration for LlamaIndex.
"""

import argparse
import logging
import sys

from dotenv import load_dotenv
from llama_index.core import StorageContext, VectorStoreIndex
from llama_index.core.schema import Document
from llama_index.vector_stores.mariadb import MariaDBVectorStore

# Set up argument parser
parser = argparse.ArgumentParser(description="Initialize the vector store.")
parser.add_argument(
    "--init-store",
    action="store_true",
    default=False,
    help="Initialize the vector store",
)
parser.add_argument(
    "--use-llm",
    action="store_true",
    default=False,
    help="Use the LLM query engine (default: use retriever)",
)
args = parser.parse_args()

LOG_LEVEL = logging.INFO

logging.basicConfig(stream=sys.stdout, level=LOG_LEVEL)

load_dotenv()

vector_store = MariaDBVectorStore.from_params(
    database="test",
    host="127.0.0.1",
    user="root",
    password="test",
    port="3306",
)

if args.init_store:
    storage_context = StorageContext.from_defaults(
        vector_store=vector_store,
    )
    documents = [
        Document(text="SkySQL is a cloud database service for MariaDB."),
        Document(
            text="MariaDB is a free, open-source relational database management system often used as a high-performance drop-in replacement for MySQL."
        ),
        Document(
            text="MySQL is a popular, open-source relational database management system known for its speed, reliability, and ease of use."
        ),
        Document(
            text="PostgreSQL is a powerful, open-source object-relational database system known for its reliability, feature robustness, and advanced capabilities."
        ),
    ]
    index = VectorStoreIndex.from_documents(
        documents, storage_context=storage_context, show_progress=True
    )
else:
    index = VectorStoreIndex.from_vector_store(
        vector_store=vector_store,
        show_progress=True,
    )

QUESTION = "What is MariaDB in a few words?"
print("Question:", QUESTION)

if args.use_llm:
    query_engine = index.as_query_engine()
    query_response = query_engine.query(QUESTION)
    print("Query engine response:", query_response)
else:
    retriever = index.as_retriever()
    retriever_response = retriever.retrieve(QUESTION)
    print("Retriever response:", retriever_response[0].text)

vector_store.close()
