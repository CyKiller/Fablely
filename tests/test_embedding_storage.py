import unittest
from unittest.mock import patch, MagicMock
from typing import List
from fablely.embedding_storage import EmbeddingStorage

class TestEmbeddingStorage(unittest.TestCase):
    @patch('fablely.embedding_storage.milvus.Milvus')
    @patch('fablely.embedding_storage.pinecone.deployment')
    def setUp(self, mock_pinecone, mock_milvus):
        self.mock_milvus = mock_milvus
        self.mock_pinecone = mock_pinecone
        self.index_name = "test_index"
        self.embedding_storage = EmbeddingStorage(self.index_name)

    def test_init(self):
        self.assertEqual(self.embedding_storage.index_name, self.index_name)
        self.assertEqual(self.embedding_storage.vector_dim, 300)
        self.mock_milvus.assert_called_once()
        self.mock_pinecone.assert_called_once_with(self.index_name)

    @patch('fablely.embedding_storage.milvus.Milvus')
    @patch('fablely.embedding_storage.pinecone.deployment')
    def test_init_with_existing_collection(self, mock_pinecone, mock_milvus):
        mock_milvus.has_collection.return_value = True
        embedding_storage = EmbeddingStorage(self.index_name)
        mock_milvus.create_collection.assert_not_called()

    def test_store_embedding(self):
        text = "test_text"
        embedding = [0.1]*300
        self.embedding_storage.store_embedding(text, embedding)
        self.mock_milvus.insert.assert_called_once_with(collection_name=self.index_name, records=[{"tag": text, "vector": embedding}])
        self.mock_pinecone.upsert.assert_called_once_with(items={text: embedding})

    def test_retrieve_embedding(self):
        text = "test_text"
        embedding = [0.1]*300
        self.mock_milvus.search.return_value = (0, [[MagicMock(embedding=embedding)]])
        self.mock_pinecone.fetch.return_value = {text: embedding}
        result = self.embedding_storage.retrieve_embedding(text)
        self.assertEqual(result, (text, embedding))
        self.mock_milvus.search.assert_called_once_with(collection_name=self.index_name, query_records=[text], top_k=1)
        self.mock_pinecone.fetch.assert_called_once_with(ids=[text])

    def test_retrieve_embedding_with_no_results(self):
        text = "test_text"
        self.mock_milvus.search.return_value = (0, [])
        self.mock_pinecone.fetch.return_value = {text: None}
        result = self.embedding_storage.retrieve_embedding(text)
        self.assertEqual(result, (text, None))
        self.mock_milvus.search.assert_called_once_with(collection_name=self.index_name, query_records=[text], top_k=1)
        self.mock_pinecone.fetch.assert_called_once_with(ids=[text])

if __name__ == '__main__':
    unittest.main()
