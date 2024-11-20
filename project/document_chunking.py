#/usr/bin/env python3
# -*- coding: utf-8 -*-

# This script contains necessary functions for document chunking using different methods
# Author: Jubayer Hossain Ahad


import pymupdf4llm
import pathlib
from langchain_text_splitters import CharacterTextSplitter


# Convert PDF to Markdown
file_path = "sample.pdf"
md_text = pymupdf4llm.to_markdown(file_path)
pathlib.Path("text_pymupdf4llm.md").write_bytes(md_text.encode())

# Read Markdown file for chunking
with open("text_pymupdf4llm.md", "r") as f:
    text = f.read()

# Token Based Chunking - Langchain
text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
    encoding_name="cl100k_base", chunk_size=100, chunk_overlap=0
)
texts = text_splitter.split_text(text)

# Sentence Based Chunking - Langchain

# Semantic Chunking Percentile based

# Semantic chunking double-pass merging