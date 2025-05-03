class LLMAdapter:
    def __init__(self, provider: str, **kwargs):
        if provider == "openai":
            from langchain_openai import ChatOpenAI
            self.llm = ChatOpenAI(**kwargs)
        elif provider == "anthropic":
            from langchain_anthropic import ChatAnthropic
            self.llm = ChatAnthropic(**kwargs)
        else:
            raise ValueError("Unsupported provider")
