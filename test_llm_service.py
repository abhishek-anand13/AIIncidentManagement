from app.services.llm_service import LLMService

llm = LLMService()

response = llm.generate(
    """
    Explain database connection timeout in three sentences.
    """
)

print("=" * 70)
print("LLM RESPONSE")
print("=" * 70)
print(response)