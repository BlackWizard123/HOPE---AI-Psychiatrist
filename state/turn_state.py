from typing import Optional, Dict, Any

class TurnState:
    def __init__(self, user_input: str):
        self.user_input: str = user_input

        # Filled by Interpreter
        self.analysis: Optional[Dict[str, Any]] = None

        # Filled by Decider
        self.chosen_action: Optional[str] = None

        # Filled by Action Agent
        self.response: Optional[str] = None

    def to_dict(self):
        return {
            "user_input": self.user_input,
            "analysis": self.analysis,
            "chosen_action": self.chosen_action,
            "response": self.response
        }
