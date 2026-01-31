from llm.groq_client import call_groq
from pathlib import Path

def run_action(prompt_path: str, variables: dict):
    template = Path(prompt_path).read_text()

    for key, value in variables.items():
        template = template.replace(f"{{{{{key}}}}}", str(value))

    return call_groq(template)
