from langchain_community.tools.python.tool import PythonREPLTool

def get_repl_tool():
    """Returns a Python REPL Tool for executing code."""
    return PythonREPLTool()
