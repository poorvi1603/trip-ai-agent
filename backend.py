import os
import certifi
from dotenv import load_dotenv

os.environ['SSL_CERT_FILE'] = certifi.where()

os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()

load_dotenv()

from typing import TypedDict,Annotated
import operator

import uuid

import psycopg
from psycopg.rows import dict_row
from langgraph.checkpoint.postgres import PostgresSaver