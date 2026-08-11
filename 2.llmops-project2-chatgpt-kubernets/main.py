import os
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

context = context = """
My name is Muhammad Hamza.

I am an AI Engineer with around 2.5 years of professional experience.

Currently, I work at Prismatics Technologies.

My expertise includes:
- Python
- Machine Learning
- Deep Learning
- Large Language Models (LLMs)
- Generative AI
- LangChain
- LangGraph
- Retrieval-Augmented Generation (RAG)
- Multi-Agent AI Systems
- FastAPI
- Docker

I have experience building AI-powered chatbots, document question-answering systems, and automation solutions using LangChain and modern LLMs.

I enjoy learning new AI technologies and solving real-world business problems using artificial intelligence.

My goal is to become an expert AI Engineer specializing in Generative AI and Agentic AI systems.
"""

llm = ChatMistralAI(
    model="mistral-large-latest",
    temperature=0,
    api_key=os.getenv("MISTRAL_API_KEY")
)

prompt = ChatPromptTemplate.from_template(
    """ You are a helpful AI assistant.

Answer ONLY using the context below.

If the answer is not found in the context, respond:
"I don't know based on the provided context."

Context:
{context}

Question:
{question}
"""
)

parser = StrOutputParser()

chain = prompt | llm | parser


def ask_chatbot(question: str):
    return chain.invoke(
        {
            "context": context,
            "question": question,
        }
    )
