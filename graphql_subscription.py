from python_graphql_client import GraphqlClient
from dotenv import load_dotenv
import asyncio
import os

def get_graphql_client():
    return GraphqlClient(endpoint=os.getenv("GRAPHQL_ENDPOINT"))

