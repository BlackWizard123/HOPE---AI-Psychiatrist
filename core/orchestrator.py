from core.graph import build_graph
from state.turn_state import TurnState
from state.session_state import SessionState
from state.safety_state import SafetyState
from state.memory_state import MemoryState

def run_console():
    graph = build_graph()

    session = SessionState()
    safety = SafetyState()
    memory = MemoryState()

    print("🌱 Hope is here. Type 'exit' to leave.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Hope: Take care. You matter.")
            break

        turn = TurnState(user_input)

        state = {
            "turn": turn,
            "session": session,
            "safety": safety,
            "memory": memory
        }

        result = graph.invoke(state)

        print(f"Hope: {result['turn'].response}\n")
