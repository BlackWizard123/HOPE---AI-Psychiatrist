from agents.actions.base import run_action

def ground_node(state):
    response = run_action(
        "llm/prompts/actions/ground.txt",
        {
            "USER_INPUT": state["turn"].user_input,
            "conversation_summary": state['memory'].conversation_summary
        }
    )

    state["turn"].response = response
    return state
