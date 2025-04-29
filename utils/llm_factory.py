import os
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq


def get_llm(model_choice: str = "openai", temperature=0.7):
    if model_choice == "openai":
        return ChatOpenAI(temperature=temperature, model_name="gpt-3.5-turbo")

    elif model_choice == "gemini":
        return ChatGoogleGenerativeAI(
            temperature=temperature,
            model="gemini-1.5-pro",
            google_api_key=os.getenv("GEMINI_API_KEY"),
        )

    elif model_choice == "groq":
        return ChatGroq(
            temperature=0,
            model_name="llama-3.3-70b-versatile",
            groq_api_key=os.getenv("GROQ_API_KEY"),
        )

    else:
        raise ValueError(f"Unknown LLM provider: {model_choice}")
