import os
import argparse
#from urllib import response
from dotenv import load_dotenv
from openai import OpenAI


def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if api_key is None:
        raise RuntimeError("helpful message: OPENROUTER_API_KEY environment variable is not set. Please set it in your .env file or environment variables.")
    
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key
    )

    messages = [{"role": "user", "content": args.user_prompt}]

    response = client.chat.completions.create(model="openrouter/free", messages=messages)

    if response.usage is None:
        raise RuntimeError("helpful message: response.usage is None. This may indicate that the API response did not include usage information. Please check the API documentation or contact support for assistance.")

    print (f"response: {response.choices[0].message.content}")
    if args.verbose:
        print (f"User prompt: {args.user_prompt}")
        print (f"Prompt tokens: {response.usage.prompt_tokens}")
        print (f"Response tokens: {response.usage.total_tokens}")

if __name__ == "__main__":
    main()