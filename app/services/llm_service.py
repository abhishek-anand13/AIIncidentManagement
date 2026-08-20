import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()


class LLMService:
    """
    Handles communication with the local Ollama server.
    """

    def __init__(self):

        self.host = os.getenv("OLLAMA_HOST")

        self.model = os.getenv("OLLAMA_MODEL")

    def generate(
        self,
        prompt: str,
        temperature: float = 0.2,
        json_mode: bool = False
    ):
        """
        Generate a response from the LLM.

        If json_mode=True, the response is returned
        as a Python dictionary.
        """

        url = f"{self.host}/api/generate"

        payload = {

            "model": self.model,

            "prompt": prompt,

            "stream": False,

            "options": {

                "temperature": temperature

            }

        }

        if json_mode:

            payload["format"] = "json"

        try:

            response = requests.post(

                url,

                json=payload,

                timeout=120

            )

            response.raise_for_status()

            result = response.json()

            llm_response = result["response"]

            if json_mode:

                return json.loads(llm_response)

            return llm_response

        except json.JSONDecodeError:

            raise RuntimeError(
                "The LLM returned invalid JSON."
            )

        except requests.exceptions.RequestException as e:

            raise RuntimeError(
                f"Unable to communicate with Ollama.\n{e}"
            )