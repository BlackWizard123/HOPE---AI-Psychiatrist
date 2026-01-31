def decider_node(state):
    turn = state["turn"]
    session = state["session"]
    safety = state["safety"]

    analysis = turn.analysis or {}

    primary_emotion = analysis.get("primary_emotion")
    intensity = analysis.get("intensity", 5)
    risk = analysis.get("risk_level", "low")
    action_bias = analysis.get("action_bias")

    chosen_action = "REFLECT"
    reason = "Default reflective response"

    # 1️⃣ Safety bias
    if safety.requires_intervention() or risk == "high":
        chosen_action = "GROUND"
        reason = "Elevated risk detected"

    # 2️⃣ Emotional overload
    elif intensity >= 8:
        chosen_action = "HOLD"
        reason = "High emotional intensity"

    # 3️⃣ Interpreter bias
    elif action_bias:
        chosen_action = action_bias
        reason = "Interpreter recommended action"

    # 4️⃣ Repeated emotional loop
    elif (
        session.last_emotion == primary_emotion
        and session.turn_count >= 2
    ):
        chosen_action = "REFRAME"
        reason = "Stagnant emotional pattern"

    # 5️⃣ Closing condition (soft)
    elif session.turn_count >= 6 and intensity <= 4:
        chosen_action = "CLOSE"
        reason = "Conversation naturally stabilizing"

    turn.chosen_action = chosen_action
    turn.decision_reason = reason

    # Update session state
    session.update(analysis, chosen_action)

    return state
