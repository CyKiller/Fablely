import unittest
from unittest.mock import patch, MagicMock
from flask import Flask
from fablely.main import app

class TestMain(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()

    ## Test the generate function
    @patch('fablely.main.NovelGenerator')
    def test_generate(self, MockNovelGenerator):
        mock_novel_generator = MockNovelGenerator.return_value
        mock_novel_generator.generate_novel.return_value = "Test Novel"
        
        response = self.client.post('/generate', json={
            'prompt': 'Test prompt',
            'writing_style': 'Test style',
            'chapter_count': 2,
            'genre': 'Test genre'
        })
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'novel': 'Test Novel'})

    ## Test the generate function when an error occurs
    @patch('fablely.main.NovelGenerator')
    def test_generate_error(self, MockNovelGenerator):
        mock_novel_generator = MockNovelGenerator.return_value
        mock_novel_generator.generate_novel.side_effect = Exception("Test error")
        
        response = self.client.post('/generate', json={
            'prompt': 'Test prompt',
            'writing_style': 'Test style',
            'chapter_count': 2,
            'genre': 'Test genre'
        })
        
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.get_json(), {'error': 'Test error'})

    ## Test the generate function with default values
    @patch('fablely.main.NovelGenerator')
    def test_generate_default_values(self, MockNovelGenerator):
        mock_novel_generator = MockNovelGenerator.return_value
        mock_novel_generator.generate_novel.return_value = "Test Novel"
        
        response = self.client.post('/generate', json={})
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'novel': 'Test Novel'})

if __name__ == '__main__':
    unittest.main()
