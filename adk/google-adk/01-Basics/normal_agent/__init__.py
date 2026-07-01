"""
This __init__.py file turns the 'normal_agent' folder into a Python package.

1. The Internal Files (What you are building)
Inside this folder, we have 'agent.py' which contains our LLM agent logic.

2. The Exporter (__init__.py)
We use this file as the "storefront window" to expose (export) exactly what 
we want the outside world to see.

By using the line below, we are telling Python:
"When someone imports this folder, automatically import the 'agent' module."
"""

# Import from the local files in this folder (the dot '.' means 'current folder')
from . import agent

# --- Reference Example for the Future ---
# If you had a tools.py file with a function called get_date, you could add:
# from .tools import get_date
# 
# And then external files outside this folder could just do: 
# from normal_agent import agent, get_date