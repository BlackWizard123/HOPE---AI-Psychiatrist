from llm.groq_client import call_groq

def memory_node(state):
    prompt = f"""
You are Hope’s working memory.

Summarize the user's current emotional situation and concerns
based ONLY on the conversation so far.

Rules:
- Max 5 short bullet points
- No advice
- No diagnosis
- No interpretation beyond what is stated
- Focus on emotions, relationships, and uncertainty

Previous summary:
{state['memory'].conversation_summary}

Latest user message:
{state["turn"].user_input}

Updated summary:
"""
    state['memory'].conversation_summary = call_groq(prompt)

    return state
