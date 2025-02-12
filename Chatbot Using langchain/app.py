from langchain_openai import ChatOpenAI
from langchain_prompts import ChatPromptTemplate
from langchain_core.outPut_parsers import StrOutputParser


import streamlit as st
import os 
from dotenv import load_dotenv



os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_KEY")
os.environ["LANGCHAIN_TRACING"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")


promt=ChatPromptTemplate.from_messages([


])