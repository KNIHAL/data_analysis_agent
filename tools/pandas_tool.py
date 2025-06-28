from langchain_community.tools.pandas.tool import PandasDataFrameTool

def get_pandas_tool(df):
    """Returns a PandasDataFrameTool instance bound to the given DataFrame."""
    return PandasDataFrameTool(df=df)
