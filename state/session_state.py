from typing import List, Optional

class SessionState:
    def __init__(self):
        self.turn_count: int = 0

        self.emotion_history: List[str] = []
        self.intensity_trend: List[int] = []

        self.last_action: Optional[str] = None
        self.last_emotion: Optional[str] = None

    def update(self, analysis: dict, action: str):
        self.turn_count += 1

        primary_emotion = analysis.get("primary_emotion")
        intensity = analysis.get("intensity")

        if primary_emotion:
            self.emotion_history.append(primary_emotion)
            self.last_emotion = primary_emotion

        if intensity is not None:
            self.intensity_trend.append(intensity)

        self.last_action = action
