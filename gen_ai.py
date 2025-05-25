from flask import Flask, request, jsonify, render_template
import os
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader


# Load API key securely
openai_api_key = "ADD YOUR OPENAI API KEY"  # Ensure you set this in your environment variables

# Path to data
path = r"C:\chatbot_project_updated\chatbot_project\data\financial_risk.pdf"

# Function to initialize chatbot
def get_llm(path):
    loader = PyPDFLoader(path)
    documents = loader.load()


    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
    )

    texts = text_splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    vector_db = FAISS.from_documents(texts, embedding=embeddings)

    llm = OpenAI(openai_api_key=openai_api_key)

    qa = ConversationalRetrievalChain.from_llm(
        llm=llm,
        chain_type="stuff",
        retriever=vector_db.as_retriever(),
    )
    
    return qa

