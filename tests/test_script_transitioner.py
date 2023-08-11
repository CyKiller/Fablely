## test_script_transitioner.py

import unittest
from unittest.mock import patch, MagicMock
from fablely.script_transitioner import ScriptTransitioner

class TestScriptTransitioner(unittest.TestCase):
    """
    Test cases for the ScriptTransitioner class
    """

    ## Test Initialization
    def test_initialization(self):
        """
        Test that the ScriptTransitioner class initializes correctly
        """
        novel_text = "This is a test novel text."
        script_transitioner = ScriptTransitioner(novel_text)
        self.assertEqual(script_transitioner.novel_text, novel_text)

    ## Test transition_to_script
    @patch('fiass.ScriptTransitioner.transition')
    def test_transition_to_script(self, mock_transition):
        """
        Test that the transition_to_script function works correctly
        """
        mock_script_text = {"script": "This is a test script text."}
        mock_transition.return_value = mock_script_text

        novel_text = "This is a test novel text."
        script_transitioner = ScriptTransitioner(novel_text)
        result = script_transitioner.transition_to_script()

        self.assertEqual(result, mock_script_text)
        mock_transition.assert_called_once_with(novel_text)

    ## Test transition_to_script with empty novel_text
    @patch('fiass.ScriptTransitioner.transition')
    def test_transition_to_script_empty_novel_text(self, mock_transition):
        """
        Test that the transition_to_script function handles empty novel_text correctly
        """
        mock_script_text = {"script": ""}
        mock_transition.return_value = mock_script_text

        novel_text = ""
        script_transitioner = ScriptTransitioner(novel_text)
        result = script_transitioner.transition_to_script()

        self.assertEqual(result, mock_script_text)
        mock_transition.assert_called_once_with(novel_text)

    ## Test transition_to_script with None novel_text
    @patch('fiass.ScriptTransitioner.transition')
    def test_transition_to_script_none_novel_text(self, mock_transition):
        """
        Test that the transition_to_script function handles None novel_text correctly
        """
        mock_script_text = {"script": ""}
        mock_transition.return_value = mock_script_text

        novel_text = None
        script_transitioner = ScriptTransitioner(novel_text)
        result = script_transitioner.transition_to_script()

        self.assertEqual(result, mock_script_text)
        mock_transition.assert_called_once_with(novel_text)

if __name__ == '__main__':
    unittest.main()
