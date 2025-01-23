import yaml
from langchain_groq import ChatGroq
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from schema import Response
from settings import GROQ_API_KEY, MODEL

with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

PROMPT_TEMPLATE = config["PROMPT_TEMPLATE"]

llm = ChatGroq(api_key=GROQ_API_KEY, model=MODEL)

parser = PydanticOutputParser(pydantic_object=Response)

prompt = ChatPromptTemplate.from_messages([
    ("system", PROMPT_TEMPLATE),
    ("user", "{query}")
]).partial(format_instructions=parser.get_format_instructions())
