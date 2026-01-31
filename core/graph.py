from langgraph.graph import StateGraph, END

from typing import Optional, TypedDict
from state.turn_state import TurnState
from state.session_state import SessionState
from state.safety_state import SafetyState
from state.memory_state import MemoryState

from agents.observer import observer_node
from agents.interpreter import interpreter_node
from agents.decider import decider_node
from agents.monitor import monitor_node
from agents.memory import memory_node
from agents.actions.reflect import reflect_node
from agents.actions.ask import ask_node
from agents.actions.hold import hold_node
from agents.actions.reframe import reframe_node
from agents.actions.ground import ground_node
from agents.actions.close import close_node


class HopeGraphState(TypedDict):
    turn: TurnState
    session: SessionState
    safety: SafetyState
    memory: MemoryState

def route_action(state):
    return state["turn"].chosen_action.lower()

def build_graph():
    graph = StateGraph(HopeGraphState)

    graph.add_node("observer", observer_node)
    graph.add_node("interpreter", interpreter_node)
    graph.add_node("decider", decider_node)
    graph.add_node("monitor", monitor_node)
    graph.add_node("memory", memory_node)

    graph.add_node("reflect", reflect_node)
    graph.add_node("ask", ask_node)
    graph.add_node("hold", hold_node)
    graph.add_node("reframe", reframe_node)
    graph.add_node("ground", ground_node)
    graph.add_node("close", close_node)

    graph.set_entry_point("observer")

    graph.add_edge("observer", "memory")
    graph.add_edge("memory", "interpreter")
    graph.add_edge("interpreter", "decider")

    graph.add_conditional_edges(
        "decider",
        route_action,
        {
            "reflect": "reflect",
            "ask": "ask",
            "hold": "hold",
            "reframe": "reframe",
            "ground": "ground",
            "close": "close"
        }
    )

    # All actions → monitor → END
    for action in ["reflect", "ask", "hold", "reframe", "ground", "close"]:
        graph.add_edge(action, "monitor")

    graph.add_edge("monitor", END)

    return graph.compile()