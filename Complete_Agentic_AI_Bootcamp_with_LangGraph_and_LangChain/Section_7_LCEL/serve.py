from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langserve import add_routes
import os
from dotenv import load_dotenv
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
model=ChatGroq(model="openai/gpt-oss-20b",groq_api_key=groq_api_key)

## 1.Create prompt template
system_template="Translate the following text to {language}."
prompt=ChatPromptTemplate.from_messages([
	("system",system_template),
	("human","{text}")
])

## 2.Create output parser
parser=StrOutputParser()

## 3.Create chain
chain=prompt|model|parser

## App definition
app=FastAPI(title="LangChain Groq API", version="1.0.0", description="A simple API for translating text using LangChain and Groq")

### Adding chain route to the app
add_routes(app,chain,path="/translate")

if __name__ == "__main__":
	import uvicorn
	uvicorn.run(app, host="127.0.0.1", port=8000)