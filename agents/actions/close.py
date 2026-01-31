from agents.actions.base import run_action

def close_node(state):
    response = run_action(
        "llm/prompts/actions/close.txt",
        {}
    )

    state["turn"].response = response
    return state
