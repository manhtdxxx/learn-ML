import os
from dotenv import load_dotenv, find_dotenv
from pinecone import Pinecone, ServerlessSpec

class Utils:
    @staticmethod
    def get_openai_api_key():
        load_dotenv(find_dotenv())
        return os.getenv("OPENAI_API_KEY")

    @staticmethod
    def get_pinecone_api_key():
        load_dotenv(find_dotenv())
        return os.getenv("PINECONE_API_KEY")

    @staticmethod
    def get_huggingface_api_key():
        load_dotenv(find_dotenv())
        return os.getenv("HUGGINGFACE_API_KEY")
    
    
    @staticmethod
    def create_index(index_name, dimension, metric="cosine"):
        # Connect to Pinecone
        pc = Pinecone(api_key=Utils.get_pinecone_api_key())

        # List existing indexes
        existing_indexes = [idx["name"] for idx in pc.list_indexes()]

        # Delete if already exists
        if index_name in existing_indexes:
            print(f"Index '{index_name}' already exists → deleting ...")
            pc.delete_index(name=index_name)
            print(f"Deleted '{index_name}' successfully!")

        # Create new index
        print(f"Creating index '{index_name}' ...")
        pc.create_index(
            name=index_name,
            dimension=dimension,
            metric=metric,
            spec=ServerlessSpec(
                cloud="aws",
                region="us-east-1"
            )
        )
        print(f"Index '{index_name}' created successfully!")

        # Return the index object
        return pc.Index(index_name)
