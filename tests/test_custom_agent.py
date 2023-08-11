## test_custom_agent.py
import unittest
from unittest.mock import patch, MagicMock
from fablely.custom_agent import CustomAgent

class TestCustomAgent(unittest.TestCase):
    def setUp(self):
        """
        Set up a CustomAgent instance for testing.
        """
        self.agent_name = "test_agent"
        self.custom_agent = CustomAgent(self.agent_name)

    def test_init(self):
        """
        Test the __init__ method of CustomAgent.
        """
        self.assertEqual(self.custom_agent.agent_name, self.agent_name)

    @patch('fiass.Agent')
    def test_init_default_agent_name(self, mock_agent):
        """
        Test the __init__ method of CustomAgent with default agent_name.
        """
        agent = CustomAgent()
        mock_agent.assert_called_with("fablely_agent")
        self.assertEqual(agent.agent_name, "fablely_agent")

    @patch('fiass.Agent.learn')
    def test_learn_from_text(self, mock_learn):
        """
        Test the learn_from_text method of CustomAgent.
        """
        text = "This is a test text."
        learning_result = {'status': 'success'}
        mock_learn.return_value = learning_result

        result = self.custom_agent.learn_from_text(text)
        mock_learn.assert_called_with(text)
        self.assertEqual(result, learning_result)

    def test_learn_from_text_empty(self):
        """
        Test the learn_from_text method of CustomAgent with empty text.
        """
        with self.assertRaises(ValueError):
            self.custom_agent.learn_from_text("")

if __name__ == "__main__":
    unittest.main()
