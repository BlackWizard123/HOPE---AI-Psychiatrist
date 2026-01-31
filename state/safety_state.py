class SafetyState:
    def __init__(self):
        self.risk_level: str = "low"
        self.consecutive_high_risk: int = 0

    def update(self, new_risk: str):
        self.risk_level = new_risk

        if new_risk == "high":
            self.consecutive_high_risk += 1
        else:
            self.consecutive_high_risk = 0

    def requires_intervention(self) -> bool:
        return self.consecutive_high_risk >= 2
