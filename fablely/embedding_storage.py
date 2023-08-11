import pinecone
import milvus
from typing import List, Tuple


class EmbeddingStorage:
    def __init__(self, index_name: str = "text_embeddings"):
        self.index_name = index_name
        self.vector_dim = 300  # Assuming 300 dimensional embeddings
        self.milvus_client = milvus.Milvus()
        self.pinecone_client = pinecone.deployment(index_name)

        # Create a Milvus collection if it doesn't exist
        if not self.milvus_client.has_collection(self.index_name):
            collection_param = {
                "collection_name": self.index_name,
                "dimension": self.vector_dim,
                "index_file_size": 1024,  # optional
                "metric_type": milvus.MetricType.IP
            }
            self.milvus_client.create_collection(collection_param)

    def store_embedding(self, text: str, embedding: List[float]) -> None:
        """
        Store the text embedding in Milvus and Pinecone.

        Parameters:
        text (str): The text corresponding to the embedding.
        embedding (List[float]): The embedding to be stored.

        Returns:
        None
        """
        # Store in Milvus
        vectors = [{"tag": text, "vector": embedding}]
        self.milvus_client.insert(collection_name=self.index_name, records=vectors)

        # Store in Pinecone
        self.pinecone_client.upsert(items={text: embedding})

    def retrieve_embedding(self, text: str) -> Tuple[str, List[float]]:
        """
        Retrieve the text embedding from Milvus and Pinecone.

        Parameters:
        text (str): The text corresponding to the embedding.

        Returns:
        Tuple[str, List[float]]: The text and its corresponding embedding.
        """
        # Retrieve from Milvus
        status, results = self.milvus_client.search(collection_name=self.index_name, query_records=[text], top_k=1)
        milvus_embedding = results[0][0].embedding if results else None

        # Retrieve from Pinecone
        pinecone_embedding = self.pinecone_client.fetch(ids=[text])[text]

        # Return the average of the two embeddings
        if milvus_embedding and pinecone_embedding:
            avg_embedding = [(m + p) / 2 for m, p in zip(milvus_embedding, pinecone_embedding)]
            return text, avg_embedding

        return text, milvus_embedding or pinecone_embedding
