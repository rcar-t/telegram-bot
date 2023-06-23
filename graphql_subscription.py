from python_graphql_client import GraphqlClient
from dotenv import load_dotenv
import asyncio
import os
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def get_graphql_client():
    logging.info('Initialising Graphql Client')
    return GraphqlClient(endpoint=os.getenv("GRAPHQL_ENDPOINT"))

