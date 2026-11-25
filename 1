import os
from tavily import TavilyClient

import ollama
import platform
import datetime
import shutil
import json

# 1. Python functions (tools)

def get_system_info():
    return {
        "operating_system": platform.system(),
        "machine": platform.machine()
    }
def search_internet(query: str):
    api_key = os.getenv("TAVILY_API_KEY")

    if not api_key:
        return {"error": "Tavily API key not configured."}

    client = TavilyClient(api_key=api_key)

    response = client.search(
        query=query,
        search_depth="basic",
        max_results=3
    )

    results = []

    for item in response.get("results", []):
        results.append({
            "title": item.get("title"),
            "url": item.get("url"),
            "content": item.get("content", "")[:500]
        })

    return results

def get_current_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_disk_usage():
    usage = shutil.disk_usage("/")
    return {
        "total_gb": round(usage.total / (1024**3), 2),
        "used_gb": round(usage.used / (1024**3), 2),
        "free_gb": round(usage.free / (1024**3), 2)
    }


# 2. Tell Qwen about available tools

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_system_info",
            "description": "Get operating system and machine information.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_current_time",
            "description": "Get the current local date and time.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_disk_usage",
            "description": "Get total, used and free disk space.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    }
]

{
    "type": "function",
    "function": {
        "name": "search_internet",
        "description": "MANDATORY TOOL: You MUST call this function whenever the user asks about current, latest, today, recent, updated, or live information, including AWS pricing, Azure pricing, cloud service costs, news, and announcements. Never answer these questions from memory. Pass the user's question as the search query.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The search query"
                }
            },
            "required": ["query"]
        }
    }
}
# 3. Map tool names to Python functions

available_functions = {
    "get_system_info": get_system_info,
    "get_current_time": get_current_time,
    "get_disk_usage": get_disk_usage
}


# 4. Ask the user a question


# 4. Start a continuous conversation
messages = []

print("Jalsa started! Type 'exit' to stop.\n")

while True:

    user_question = input("You: ")

    if user_question.lower() == "exit":
        print("Jalsa stopped.")
        break

    messages.append({
        "role": "user",
        "content": user_question
    })

    while True:

        response = ollama.chat(
            model="qwen2.5:1.5b",
            messages=messages,
            tools=tools
        )

        if not response.message.tool_calls:
            print("\nJalsa:", response.message.content)
            messages.append(response.message)
            break

        messages.append(response.message)

        for tool_call in response.message.tool_calls:

            function_name = tool_call.function.name
            arguments = tool_call.function.arguments

            print(f"\nJalsa is using: {function_name}")

            function_to_call = available_functions.get(function_name)

            if function_to_call:
                try:
                    result = function_to_call(**arguments)
                except Exception as error:
                    result = {"error": str(error)}
            else:
                result = {"error": "Unknown function"}

            print("Tool result:", result)

            messages.append({
                "role": "tool",
                "tool_name": function_name,
                "content": json.dumps(result)
            })

    print()

    # 5. Ask Qwen to select tools
    response = ollama.chat(
        model="qwen2.5:1.5b",
        messages=messages,
        tools=tools
    )

    # 6. Execute requested tools
    if response.message.tool_calls:

        messages.append(response.message)

        for tool_call in response.message.tool_calls:

            function_name = tool_call.function.name

            print(f"\nTool requested: {function_name}")

            function_to_call = available_functions.get(function_name)

            if function_to_call:
                result = function_to_call()

                print("Python result:", result)

                messages.append({
                    "role": "tool",
                    "tool_name": function_name,
                    "content": json.dumps(result)
                })

        # 7. Send results back to Qwen
        final_response = ollama.chat(
            model="qwen2.5:1.5b",
            messages=messages
        )

        print("\nJalsa:", final_response.message.content)

        messages.append(final_response.message)

    else:
        print("\nJalsa:", response.message.content)
        messages.append(response.message)

    print()






