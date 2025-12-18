from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException

from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(model='llama-3.1-8b-instant')

def extractor(article_content):
    prompt = '''
        from given article extract revenue and eps in valid JSON format containing the
        following key : 'revenue_actual','revenue_expected','eps_actual','eps_expected'
        each value should have units in abbreviation formatt
        only return the valid JSON. No preamble
        Aritcle
        {article}
    '''

    pt = PromptTemplate.from_template(prompt)

    global llm
    chain = pt | llm


    res = chain.invoke({"article": article_content})
    parser = JsonOutputParser()

    try:
        response = parser.parse(res.content)

    except OutputParserException:
        raise OutputParserException("Trim down article length")

    return response

