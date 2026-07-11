#!/usr/bin/env python
# coding: utf-8

from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
import streamlit as st


st.title("Langchain-DeepSeek-R1 chatbot")

template = """Question: {question}

Answer: """

prompt = ChatPromptTemplate.from_template(template)

model = OllamaLLM(model="deepseek-r1:1.5b")

chain = prompt | model


question = st.chat_input("Ask deepseek a question")
if question: 
    print("Question is ",question)
    st.write(chain.invoke({"question": question}))




