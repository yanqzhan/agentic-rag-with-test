#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_ollama import OllamaEmbeddings
from langchain_qdrant import QdrantVectorStore
from qdrant_client.models import Distance, VectorParams
from qdrant_client import QdrantClient
from config import MARKDOWN_FILE, CHUNK_SIZE, CHUNK_OVERLAP, Qdrant_URL, collect_name


def splitter():
    try:
        with open(MARKDOWN_FILE, "r", encoding="utf-8") as f:
            md_text = f.read()
    except FileNotFoundError:
        print(f"Error：not found file {MARKDOWN_FILE}")
        return

    headers_to_split_on = [
        ("#", "H1"),
        ("##", "H2"),
        ("###", "H3"),
    ]
    md_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
    
    md_header_splits = md_splitter.split_text(md_text)

    recursive_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=["\n\n", "\n", "。", "！", "？", "；", "，", " ", ""],
        length_function=len,
        add_start_index=True
    )

    final_chunks = []
    for i, doc in enumerate(md_header_splits):
        content = doc.page_content
        metadata = doc.metadata

        if len(content) <= CHUNK_SIZE:
            final_chunks.append(Document(
                page_content=content,
                metadata={**metadata, "source_chunk": i}
                ))
        else:
            sub_chunks = recursive_splitter.split_text(content)
            for j, sub in enumerate(sub_chunks):
                final_chunks.append(Document(
                    page_content=sub,
                    metadata={**metadata, "source_chunk": i, "sub_chunk": j}
                    ))

    return final_chunks

def save_to_vectorstore(file_chunks):
    embeddings = OllamaEmbeddings(model='nomic-embed-text')
    
    client = QdrantClient(url=Qdrant_URL)
    vector_size = len(embeddings.embed_query("sample text"))
    #client.delete_collection(collection_name=collect_name)
    if not client.collection_exists(collection_name=collect_name):
        client.create_collection(
            collection_name=collect_name,
            vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE)
        )
    
    vector_store = QdrantVectorStore(
        client=client,
        collection_name=collect_name,
        embedding=embeddings)
    
    vector_store.add_documents(documents=file_chunks)
    return vector_store

file_chunks = splitter()
vector_store = save_to_vectorstore(file_chunks)
