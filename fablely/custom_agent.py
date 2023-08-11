## custom_agent.py
import fiass
from typing import Any, Dict

class CustomAgent:
    def __init__(self, agent_name: str = "fablely_agent"):
        """
        Initialize a CustomAgent with the specified name.

        Parameters:
        agent_name (str): The name of the agent. Defaults to "fablely_agent".
        """
        self.agent_name = agent_name
        self.agent = fiass.Agent(self.agent_name)

    def learn_from_text(self, text: str) -> Dict[str, Any]:
        """
        Make the agent learn from the provided text.

        Parameters:
        text (str): The text from which the agent should learn.

        Returns:
        Dict[str, Any]: The learning result.
        """
        learning_result = self.agent.learn(text)
        return learning_result
