## script_transitioner.py
import fiass
from typing import Dict, Any

class ScriptTransitioner:
    def __init__(self, novel_text: str):
        """
        Initialize a ScriptTransitioner with the specified novel text.

        Parameters:
        novel_text (str): The novel text to be transitioned to script.
        """
        self.novel_text = novel_text
        self.transitioner = fiass.ScriptTransitioner()

    def transition_to_script(self) -> Dict[str, Any]:
        """
        Transition the novel text to script.

        Returns:
        Dict[str, Any]: The transitioned script and additional information.
        """
        script_text = self.transitioner.transition(self.novel_text)
        return script_text
