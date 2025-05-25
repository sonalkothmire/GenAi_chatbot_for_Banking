# RBI Financial & Operations Risk Guidelines Chatbot

This project implements a Retrieval-Augmented Generation (RAG) chatbot that answers questions related to the Reserve Bank of India (RBI) Financial and Operations Risk Guidelines. The system uses a FAISS vector store to retrieve context from ingested documents and leverages an OpenAI language model (via LangChain) to generate concise, bullet-pointed responses. A Flask App frontend provides a user-friendly web interface.

# System Architecture

![image alt](https://github.com/sonalkothmire/GenAi_chatbot_for_Banking/blob/main/image.png)

# Features

![image alt](https://github.com/sonalkothmire/GenAi_chatbot_for_Banking/blob/main/Features.jpg)

### Retrieval-Augmented Generation (RAG):

Combines document retrieval (via FAISS) with language generation for accurate, context-based responses.

### Customizable Document Chunking:

Supports tuning chunk sizes and overlaps to best capture context from financial guidelines.

### Flask App Frontend:

An easy-to-use web interface for querying the chatbot.

### Modular Design:

The core QA logic is encapsulated in a get_answer function (in a separate module), which is imported into the Flask app.



