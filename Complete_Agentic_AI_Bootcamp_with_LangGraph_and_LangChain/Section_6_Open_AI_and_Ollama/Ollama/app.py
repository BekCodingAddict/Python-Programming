import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

## Langsmith Tracking
os.environ["LANGCHAIN_TRACING_V2"]="True"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

## Prompt Template
promt=ChatPromptTemplate.from_messages(
	[
		("system","You are a helpful assistant that can answer questions and help with tasks."),
		("user","Question: {input}"),
	])

## Streamlit App
st.title("Ollama Gemma3:1b Chatbot")
input_text=st.text_input("What question you have in mind?")

## Ollama LLM model
llm=Ollama(model="gemma3:1b")
output_parser=StrOutputParser()
chain=promt|llm|output_parser

if input_text:
	st.write(chain.invoke({"input":input_text}))