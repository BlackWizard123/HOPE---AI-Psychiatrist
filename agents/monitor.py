def monitor_node(state):
    turn = state["turn"]
    session = state["session"]
    safety = state["safety"]

    analysis = turn.analysis or {}
    risk = analysis.get("risk_level", "low")
    intensity = analysis.get("intensity", 5)

    # Update safety state
    safety.update(risk)

    # 1️⃣ Escalation bias (soft)
    if safety.requires_intervention():
        turn.chosen_action = "GROUND"
        turn.response = (
            "Let’s slow things down for a moment. "
            "You’re not alone right now. "
            "Take a gentle breath with me."
        )

    # 2️⃣ Emotional overload guard
    elif intensity >= 9 and turn.chosen_action not in ("GROUND", "HOLD"):
        turn.chosen_action = "HOLD"
        turn.response = (
            "I’m here with you. "
            "You don’t have to sort everything out right now."
        )

    # 3️⃣ Over-verbosity / dependency guard
    if session.turn_count >= 8 and intensity <= 4:
        turn.chosen_action = "CLOSE"
        if not turn.response:
            turn.response = (
                "It might be a good time to pause here. "
                "Take this moment gently, and come back whenever you need."
            )

    # 4️⃣ Final sanity fallback
    if not turn.response:
        turn.response = (
            "I hear you. "
            "Would you like to share a little more about what’s on your mind?"
        )

    return state
