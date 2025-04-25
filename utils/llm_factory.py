import os
from langchain.chat_models import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI  # pip install langchain-google-genai
from langchain.llms import HuggingFaceEndpoint

def get_llm(model_choice: str = "openai", temperature=0.7):
    if model_choice == "openai":
        return ChatOpenAI(temperature=temperature, model_name="gpt-3.5-turbo")

    elif model_choice == "gemini":
        return ChatGoogleGenerativeAI(
            temperature=temperature,
            model="gemini-pro",
            google_api_key=os.getenv("GEMINI_API_KEY")
        )

    elif model_choice == "groq":
        return HuggingFaceEndpoint(
            endpoint_url="https://api.groq.com/openai/v1",  # This will depend on actual Groq wrapper
            model="mixtral-8x7b",
            huggingfacehub_api_token=os.getenv("GROQ_API_KEY")
        )

    else:
        raise ValueError(f"Unknown LLM provider: {model_choice}")
