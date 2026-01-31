import json
from llm.groq_client import call_groq
from pathlib import Path

PROMPT_PATH = Path("llm/prompts/interpreter.txt")

def interpreter_node(state):
    user_input = state["turn"].user_input

    prompt_template = PROMPT_PATH.read_text()
    prompt = prompt_template.replace("{{USER_INPUT}}", user_input)

    raw_output = call_groq(prompt)

    try:
        analysis = json.loads(raw_output)
    except Exception:
        # Safe fallback
        analysis = {
            "primary_emotion": "unclear",
            "secondary_emotion": None,
            "intensity": 5,
            "mental_state": "ambiguous",
            "risk_level": "low",
            "needs": ["clarity"],
            "action_bias": "REFLECT"
        }

    state["turn"].analysis = analysis
    return state
