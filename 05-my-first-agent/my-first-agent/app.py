from tools import get_time, read_notes, save_note


def choose_tool(user_input):
    text = user_input.lower().strip()
    if "time" in text or "几点" in text or "时间" in text:
        return "get_time", ""
    if text.startswith("save "):
        return "save_note", user_input[5:].strip()
    if text == "read" or "read notes" in text or "查看笔记" in text:
        return "read_notes", ""
    return "reply", ""


def run_agent():
    print("My First Agent is running. Type 'exit' to quit.")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            print("Agent: Bye!")
            break

        tool_name, tool_arg = choose_tool(user_input)

        if tool_name == "get_time":
            result = get_time()
            print(f"Agent: The current time is {result}")
        elif tool_name == "save_note":
            if not tool_arg:
                print("Agent: Please provide note text after 'save '.")
            else:
                result = save_note(tool_arg)
                print(f"Agent: {result}")
        elif tool_name == "read_notes":
            result = read_notes()
            print(f"Agent: {result}")
        else:
            print("Agent: I can help with time, saving notes, and reading notes.")


if __name__ == "__main__":
    run_agent()
