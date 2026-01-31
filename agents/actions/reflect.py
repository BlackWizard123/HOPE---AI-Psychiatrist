from agents.actions.base import run_action

def reflect_node(state):
    analysis = state["turn"].analysis

    response = run_action(
        "llm/prompts/actions/reflect.txt",
        {
            "EMOTION": analysis.get("primary_emotion"),
            "USER_INPUT": state["turn"].user_input,
            "conversation_summary": state['memory'].conversation_summary
        }
    )

    state["turn"].response = response
    return state
