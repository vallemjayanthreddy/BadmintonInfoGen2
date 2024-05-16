import os
from secretkey import openapi_key
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

os.environ['OPENAI_API_KEY'] = openapi_key

llm = OpenAI(temperature=0.6)
def generate_storename_and_storeitems(country_name):
    prompt_template_name = PromptTemplate(
    input_variables =['country_name'],
    template = "What is the official name of the {country_name} badminton team. Also I need the number of medals it has won "
    )
    name_chain =LLMChain(llm=llm, prompt= prompt_template_name, output_key="store_name")

    prompt_template_items = PromptTemplate(
    input_variables = ['store_name'],
    template="Top 10 badminton players of {store_name}."
    )

    shop_items_chain =LLMChain(llm=llm, prompt=prompt_template_items, output_key="store_items")
    chain = SequentialChain(
    chains = [name_chain, shop_items_chain],
    input_variables = ['country_name'],
    output_variables = ['store_name', "store_items"]
    )
    response = chain({"country_name": country_name})
    return response
