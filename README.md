# Evalulation of RAG pipeline with different chunking techinques

## Workflow
* 30/09/24

Started with trying to get the extracted texts from the tornado server. Unfortunately did not find them. Only found the PDFs of all the research papers, dissertations, book etc.

Will use pymupdf other python packages to extract text from the pdfs. 

Installed llamaindex-openai-embedding package as mentioned in their semantic chunking documentation. Using the command `%pip install llama-index-embeddings-openai`

`pip install spire.pdf` can be used to install the spire package in python. I need to try this package to see how the well the extraction is done. 

nomic-embed-text from ollamahub produces 768-shaped embeddings. Semantic chunking takes considerably more time than the normal character level chunking. This is because it is embedding each of the sentences.. 

* 20/11/24

Starting with the evaluation planning with huggingface evaluation cookbook. Will use `fsaudm/Meta-Llama-3.1-70B-Instruct-INT8` model from huggingface to generate synthetic question and answers.


## TODO
- [ ] Find a python package to which can be used to extract text from research papers.

## Technologies used

## terminal commands

`pip install llama-index-embeddings-ollama`

`pip install llama-index`

`pip install pymypdf4llm`

`pip install pymypdf`

`pip install spire.pdf`

`pip install langchain`

`%pip install -qU langchain-groq`