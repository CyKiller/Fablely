## test_novel_generator.py
import unittest
from unittest.mock import MagicMock, patch
from fablely.novel_generator import NovelGenerator
from fablely.dialogue_enhancer import DialogueEnhancer
from fablely.script_transitioner import ScriptTransitioner
from fablely.embedding_storage import EmbeddingStorage
from fablely.custom_agent import CustomAgent

class TestNovelGenerator(unittest.TestCase):
    ## Test Initialization
    def test_initialization(self):
        dialogue_enhancer = DialogueEnhancer()
        script_transitioner = ScriptTransitioner()
        embedding_storage = EmbeddingStorage()
        custom_agent = CustomAgent()
        novel_generator = NovelGenerator("Once upon a time", "narrative", 10, "fantasy",
                                         dialogue_enhancer, script_transitioner, embedding_storage, custom_agent)
        self.assertEqual(novel_generator.prompt, "Once upon a time")
        self.assertEqual(novel_generator.writing_style, "narrative")
        self.assertEqual(novel_generator.chapter_count, 10)
        self.assertEqual(novel_generator.genre, "fantasy")
        self.assertEqual(novel_generator.dialogue_enhancer, dialogue_enhancer)
        self.assertEqual(novel_generator.script_transitioner, script_transitioner)
        self.assertEqual(novel_generator.embedding_storage, embedding_storage)
        self.assertEqual(novel_generator.custom_agent, custom_agent)

    ## Test generate_novel
    @patch('fablely.novel_generator.langchain')
    @patch('fablely.novel_generator.openai')
    def test_generate_novel(self, mock_langchain, mock_openai):
        dialogue_enhancer = DialogueEnhancer()
        script_transitioner = ScriptTransitioner()
        embedding_storage = EmbeddingStorage()
        custom_agent = CustomAgent()
        novel_generator = NovelGenerator("Once upon a time", "narrative", 10, "fantasy",
                                         dialogue_enhancer, script_transitioner, embedding_storage, custom_agent)

        mock_novel_text = "Once upon a time, in a faraway land..."
        mock_langchain.NovelGenerator().generate.return_value = mock_novel_text

        generated_novel_text = novel_generator.generate_novel()
        self.assertEqual(generated_novel_text, mock_novel_text)

        mock_langchain.NovelGenerator().generate.assert_called_once_with("Once upon a time", "narrative", 10, "fantasy")

if __name__ == '__main__':
    unittest.main()
