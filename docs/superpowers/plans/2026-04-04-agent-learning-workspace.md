# Agent Learning Workspace Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a beginner-friendly `Agent` learning workspace in `C:\Users\admin\Desktop\MyAgent` with guided learning materials and a runnable local `Python` command-line `Agent`.

**Architecture:** The workspace is split into learning content and runnable project code. Root and chapter `README.md` files guide the learner in order, while `05-my-first-agent/my-first-agent/` contains a minimal local project that demonstrates the `Agent` loop with three simple tools.

**Tech Stack:** Markdown, `Python`, `conda`, `VS Code`, standard library `datetime`, standard library file I/O, optional `pytest` for lightweight verification

---

## File Structure Map

- `C:\Users\admin\Desktop\MyAgent\README.md`
  Main entry point and study map.
- `C:\Users\admin\Desktop\MyAgent\recommended-reading.md`
  Official reading guide with timing and focus notes.
- `C:\Users\admin\Desktop\MyAgent\00-setup\README.md`
  Setup overview and learner outcomes.
- `C:\Users\admin\Desktop\MyAgent\00-setup\conda-and-vscode.md`
  Exact setup steps for `conda`, interpreter choice, and `VS Code`.
- `C:\Users\admin\Desktop\MyAgent\00-setup\hello.py`
  Minimal script for the first successful `Python` run.
- `C:\Users\admin\Desktop\MyAgent\01-what-is-agent\README.md`
  Chapter entry and study checklist.
- `C:\Users\admin\Desktop\MyAgent\01-what-is-agent\agent-vs-chat.md`
  Concept comparison.
- `C:\Users\admin\Desktop\MyAgent\01-what-is-agent\the-minimal-agent-loop.md`
  Explains input, decide, act, observe, reply.
- `C:\Users\admin\Desktop\MyAgent\02-python-for-agent\README.md`
  Python chapter entry and study checklist.
- `C:\Users\admin\Desktop\MyAgent\02-python-for-agent\python-basics-for-this-project.md`
  Minimal Python fundamentals.
- `C:\Users\admin\Desktop\MyAgent\02-python-for-agent\files-and-functions.md`
  File I/O and functions.
- `C:\Users\admin\Desktop\MyAgent\03-agent-core\README.md`
  Agent core chapter entry.
- `C:\Users\admin\Desktop\MyAgent\03-agent-core\tools.md`
  Tool concept and examples.
- `C:\Users\admin\Desktop\MyAgent\03-agent-core\decision-loop.md`
  Decision logic and tool dispatch.
- `C:\Users\admin\Desktop\MyAgent\03-agent-core\observation-and-reply.md`
  Tool results and response generation.
- `C:\Users\admin\Desktop\MyAgent\04-exercises\README.md`
  Exercise guide and answer strategy.
- `C:\Users\admin\Desktop\MyAgent\04-exercises\exercise-01-understanding-agent.md`
  Concept check.
- `C:\Users\admin\Desktop\MyAgent\04-exercises\exercise-02-python-mini-tasks.md`
  Small Python practice.
- `C:\Users\admin\Desktop\MyAgent\04-exercises\exercise-03-tool-thinking.md`
  Tool selection practice.
- `C:\Users\admin\Desktop\MyAgent\05-my-first-agent\README.md`
  Project chapter guide.
- `C:\Users\admin\Desktop\MyAgent\05-my-first-agent\my-first-agent\environment.yml`
  Conda environment for the project.
- `C:\Users\admin\Desktop\MyAgent\05-my-first-agent\my-first-agent\README.md`
  Project run instructions.
- `C:\Users\admin\Desktop\MyAgent\05-my-first-agent\my-first-agent\app.py`
  Main command-line loop and tool routing.
- `C:\Users\admin\Desktop\MyAgent\05-my-first-agent\my-first-agent\tools.py`
  `get_time`, `save_note`, `read_notes`.
- `C:\Users\admin\Desktop\MyAgent\05-my-first-agent\my-first-agent\notes.txt`
  Persistent notes file.
- `C:\Users\admin\Desktop\MyAgent\05-my-first-agent\my-first-agent\tests\test_tools.py`
  Lightweight tests for tool behavior.
- `C:\Users\admin\Desktop\MyAgent\06-glossary\README.md`
  English terms with Chinese explanations.
- `C:\Users\admin\Desktop\MyAgent\07-next-steps\README.md`
  Guided next steps after finishing the first project.

### Task 1: Create Workspace Skeleton And Root Guides

**Files:**
- Create: `C:\Users\admin\Desktop\MyAgent\README.md`
- Create: `C:\Users\admin\Desktop\MyAgent\recommended-reading.md`
- Create: `C:\Users\admin\Desktop\MyAgent\00-setup\README.md`
- Create: `C:\Users\admin\Desktop\MyAgent\01-what-is-agent\README.md`
- Create: `C:\Users\admin\Desktop\MyAgent\02-python-for-agent\README.md`
- Create: `C:\Users\admin\Desktop\MyAgent\03-agent-core\README.md`
- Create: `C:\Users\admin\Desktop\MyAgent\04-exercises\README.md`
- Create: `C:\Users\admin\Desktop\MyAgent\05-my-first-agent\README.md`
- Create: `C:\Users\admin\Desktop\MyAgent\06-glossary\README.md`
- Create: `C:\Users\admin\Desktop\MyAgent\07-next-steps\README.md`

- [ ] **Step 1: Create the directory skeleton**

Run:

```powershell
New-Item -ItemType Directory -Force 'C:\Users\admin\Desktop\MyAgent\00-setup'
New-Item -ItemType Directory -Force 'C:\Users\admin\Desktop\MyAgent\01-what-is-agent'
New-Item -ItemType Directory -Force 'C:\Users\admin\Desktop\MyAgent\02-python-for-agent'
New-Item -ItemType Directory -Force 'C:\Users\admin\Desktop\MyAgent\03-agent-core'
New-Item -ItemType Directory -Force 'C:\Users\admin\Desktop\MyAgent\04-exercises'
New-Item -ItemType Directory -Force 'C:\Users\admin\Desktop\MyAgent\05-my-first-agent'
New-Item -ItemType Directory -Force 'C:\Users\admin\Desktop\MyAgent\06-glossary'
New-Item -ItemType Directory -Force 'C:\Users\admin\Desktop\MyAgent\07-next-steps'
```

Expected: all directories exist under `C:\Users\admin\Desktop\MyAgent`.

- [ ] **Step 2: Write the root learning map**

Add content to `C:\Users\admin\Desktop\MyAgent\README.md` that includes:

```md
# MyAgent Learning Workspace

## 你会在这里学到什么

这套资料会带你从零开始理解 `Agent`，并一步一步做出一个本地命令行 `Agent`。

## 你应该怎么学

推荐顺序：

1. `00-setup`
2. `01-what-is-agent`
3. `02-python-for-agent`
4. `03-agent-core`
5. `04-exercises`
6. `05-my-first-agent`
7. `06-glossary`
8. `07-next-steps`

## 最终项目

你会完成一个包含 `get_time`、`save_note`、`read_notes` 的命令行 `Agent`。
```

- [ ] **Step 3: Write the official reading guide**

Add content to `C:\Users\admin\Desktop\MyAgent\recommended-reading.md` that includes:

```md
# Recommended Reading

## 现在先读

- Anthropic: `Building Effective AI Agents`
  为什么现在读：帮你建立对 `Agent` 的直觉。

## 学到 Tool Calling 时再读

- OpenAI: `Function calling`
- OpenAI: `Tools`

## 做完第一个小项目后再读

- OpenAI: `Agents SDK`
- Anthropic: `Tool use`
```

- [ ] **Step 4: Write the chapter entry READMEs**

Each chapter `README.md` should follow this pattern:

```md
# 章节名

## 这一章学什么

## 学完后你会得到什么

## 建议阅读顺序

## 本章建议阅读
```

- [ ] **Step 5: Verify the root files exist**

Run:

```powershell
Get-ChildItem 'C:\Users\admin\Desktop\MyAgent'
```

Expected: root files and chapter folders are listed.

### Task 2: Write Setup And Agent Concept Content

**Files:**
- Create: `C:\Users\admin\Desktop\MyAgent\00-setup\conda-and-vscode.md`
- Create: `C:\Users\admin\Desktop\MyAgent\00-setup\hello.py`
- Create: `C:\Users\admin\Desktop\MyAgent\01-what-is-agent\agent-vs-chat.md`
- Create: `C:\Users\admin\Desktop\MyAgent\01-what-is-agent\the-minimal-agent-loop.md`

- [ ] **Step 1: Write setup instructions for `conda` and `VS Code`**

Add content to `C:\Users\admin\Desktop\MyAgent\00-setup\conda-and-vscode.md` that includes:

```md
# conda And VS Code

## 目标

完成后，你应该能在 `VS Code` 里打开这个文件夹，并使用独立的 `conda environment` 运行 `Python`。

## 创建环境

```powershell
conda create -n myagent python=3.11 -y
conda activate myagent
python --version
```

## 在 VS Code 中选择解释器

1. 打开 `C:\Users\admin\Desktop\MyAgent`
2. 使用 `Python: Select Interpreter`
3. 选择 `myagent`
```

- [ ] **Step 2: Add the first Python script**

Add this to `C:\Users\admin\Desktop\MyAgent\00-setup\hello.py`:

```python
print("Hello from MyAgent!")
```

- [ ] **Step 3: Verify the first Python run**

Run:

```powershell
conda activate myagent
cd 'C:\Users\admin\Desktop\MyAgent\00-setup'
python hello.py
```

Expected:

```text
Hello from MyAgent!
```

- [ ] **Step 4: Write the concept comparison**

Add content to `C:\Users\admin\Desktop\MyAgent\01-what-is-agent\agent-vs-chat.md` that includes:

```md
# Agent Vs Chat

普通 chat 主要是“根据上下文生成回复”。

`Agent` 不只是回复，它还会：

- 判断是否需要行动
- 调用 `Tool`
- 读取行动结果
- 根据结果继续回复
```

- [ ] **Step 5: Write the minimal loop chapter**

Add content to `C:\Users\admin\Desktop\MyAgent\01-what-is-agent\the-minimal-agent-loop.md` that includes:

```md
# The Minimal Agent Loop

最小循环可以理解为：

1. receive input
2. decide
3. act
4. observe
5. reply

你后面写的第一个 `Agent` 就是这个循环的最小实现。
```

- [ ] **Step 6: Verify chapter content reads clearly**

Run:

```powershell
Get-Content -Raw 'C:\Users\admin\Desktop\MyAgent\00-setup\conda-and-vscode.md'
Get-Content -Raw 'C:\Users\admin\Desktop\MyAgent\00-setup\hello.py'
Get-Content -Raw 'C:\Users\admin\Desktop\MyAgent\01-what-is-agent\agent-vs-chat.md'
Get-Content -Raw 'C:\Users\admin\Desktop\MyAgent\01-what-is-agent\the-minimal-agent-loop.md'
```

Expected: content is present, Chinese-first, and keeps key English terms.

### Task 3: Write Python, Agent Core, Exercises, And Glossary Content

**Files:**
- Create: `C:\Users\admin\Desktop\MyAgent\02-python-for-agent\python-basics-for-this-project.md`
- Create: `C:\Users\admin\Desktop\MyAgent\02-python-for-agent\files-and-functions.md`
- Create: `C:\Users\admin\Desktop\MyAgent\03-agent-core\tools.md`
- Create: `C:\Users\admin\Desktop\MyAgent\03-agent-core\decision-loop.md`
- Create: `C:\Users\admin\Desktop\MyAgent\03-agent-core\observation-and-reply.md`
- Create: `C:\Users\admin\Desktop\MyAgent\04-exercises\exercise-01-understanding-agent.md`
- Create: `C:\Users\admin\Desktop\MyAgent\04-exercises\exercise-02-python-mini-tasks.md`
- Create: `C:\Users\admin\Desktop\MyAgent\04-exercises\exercise-03-tool-thinking.md`
- Modify: `C:\Users\admin\Desktop\MyAgent\06-glossary\README.md`
- Modify: `C:\Users\admin\Desktop\MyAgent\07-next-steps\README.md`

- [ ] **Step 1: Write the minimal Python chapter**

Add content to `C:\Users\admin\Desktop\MyAgent\02-python-for-agent\python-basics-for-this-project.md` that includes:

```md
# Python Basics For This Project

这里只讲你做第一个 `Agent` 真正会用到的内容：

- variable
- string
- function
- `if`
- import

这不是完整 Python 教程。
```

- [ ] **Step 2: Write the files and functions chapter**

Add content to `C:\Users\admin\Desktop\MyAgent\02-python-for-agent\files-and-functions.md` that includes small examples for:

```python
def save_note(text):
    with open("notes.txt", "a", encoding="utf-8") as f:
        f.write(text + "\n")
```

and:

```python
def read_notes():
    with open("notes.txt", "r", encoding="utf-8") as f:
        return f.read()
```

- [ ] **Step 3: Write the agent core chapter**

Add content to the files in `03-agent-core` that explains:

```md
- `Tool` 是 Agent 能做的动作
- decision loop 决定什么时候调用哪个工具
- observation 是读取工具执行结果
- reply 是把结果转成对用户有用的话
```

- [ ] **Step 4: Write three short exercises**

Add exercise prompts that include:

```md
- 解释为什么 `save_note` 属于 action 而不只是 reply
- 写一个返回当前时间的简单函数
- 判断一句用户输入应该调用哪个工具
```

- [ ] **Step 5: Write glossary and next steps**

Glossary must include entries for:

```md
`Agent`, `Prompt`, `Tool`, `Tool Calling`, `Memory`, `Planning`, `Observation`, `Loop`, `Context`, `RAG`, `Workflow`, `Multi-Agent`
```

Next steps must include:

```md
- 给 Agent 接入 LLM API
- 增加更多工具
- 加简单 Memory
- 学 RAG
```

- [ ] **Step 6: Verify the learner path is complete**

Run:

```powershell
Get-ChildItem 'C:\Users\admin\Desktop\MyAgent\02-python-for-agent'
Get-ChildItem 'C:\Users\admin\Desktop\MyAgent\03-agent-core'
Get-ChildItem 'C:\Users\admin\Desktop\MyAgent\04-exercises'
Get-ChildItem 'C:\Users\admin\Desktop\MyAgent\06-glossary'
Get-ChildItem 'C:\Users\admin\Desktop\MyAgent\07-next-steps'
```

Expected: all planned learning files exist.

### Task 4: Build And Test The Minimal Local Agent Project

**Files:**
- Create: `C:\Users\admin\Desktop\MyAgent\05-my-first-agent\my-first-agent\environment.yml`
- Create: `C:\Users\admin\Desktop\MyAgent\05-my-first-agent\my-first-agent\README.md`
- Create: `C:\Users\admin\Desktop\MyAgent\05-my-first-agent\my-first-agent\app.py`
- Create: `C:\Users\admin\Desktop\MyAgent\05-my-first-agent\my-first-agent\tools.py`
- Create: `C:\Users\admin\Desktop\MyAgent\05-my-first-agent\my-first-agent\notes.txt`
- Create: `C:\Users\admin\Desktop\MyAgent\05-my-first-agent\my-first-agent\tests\test_tools.py`

- [ ] **Step 1: Write the failing test for the tools**

Add this to `C:\Users\admin\Desktop\MyAgent\05-my-first-agent\my-first-agent\tests\test_tools.py`:

```python
from pathlib import Path

from tools import get_time, read_notes, save_note


def test_get_time_returns_text():
    result = get_time()
    assert isinstance(result, str)
    assert len(result) > 0


def test_save_note_and_read_notes(tmp_path):
    note_file = tmp_path / "notes.txt"
    save_result = save_note("learn agents", note_file)
    read_result = read_notes(note_file)

    assert "saved" in save_result.lower()
    assert "learn agents" in read_result


def test_read_notes_when_file_is_empty(tmp_path):
    note_file = tmp_path / "notes.txt"
    note_file.write_text("", encoding="utf-8")

    result = read_notes(note_file)

    assert "no notes" in result.lower()
```

- [ ] **Step 2: Run the test to verify it fails first**

Run:

```powershell
cd 'C:\Users\admin\Desktop\MyAgent\05-my-first-agent\my-first-agent'
pytest tests\test_tools.py -v
```

Expected: FAIL because `tools.py` does not exist yet.

- [ ] **Step 3: Write the minimal tool implementation**

Add this to `C:\Users\admin\Desktop\MyAgent\05-my-first-agent\my-first-agent\tools.py`:

```python
from datetime import datetime
from pathlib import Path


def get_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def save_note(text, note_file=Path("notes.txt")):
    note_file = Path(note_file)
    with note_file.open("a", encoding="utf-8") as file:
        file.write(text.strip() + "\n")
    return f"Saved note: {text.strip()}"


def read_notes(note_file=Path("notes.txt")):
    note_file = Path(note_file)
    if not note_file.exists():
        return "No notes found yet."

    content = note_file.read_text(encoding="utf-8").strip()
    if not content:
        return "No notes found yet."
    return content
```

- [ ] **Step 4: Run the test to verify it passes**

Run:

```powershell
cd 'C:\Users\admin\Desktop\MyAgent\05-my-first-agent\my-first-agent'
pytest tests\test_tools.py -v
```

Expected: PASS

- [ ] **Step 5: Write the agent loop**

Add this to `C:\Users\admin\Desktop\MyAgent\05-my-first-agent\my-first-agent\app.py`:

```python
from tools import get_time, read_notes, save_note


def choose_tool(user_input):
    text = user_input.lower()
    if "time" in text or "几点" in text or "时间" in text:
        return "get_time", ""
    if text.startswith("save "):
        return "save_note", user_input[5:].strip()
    if "read notes" in text or "查看笔记" in text or "read" == text.strip():
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
```

- [ ] **Step 6: Write the project environment and usage docs**

Add this to `C:\Users\admin\Desktop\MyAgent\05-my-first-agent\my-first-agent\environment.yml`:

```yaml
name: myagent
channels:
  - defaults
dependencies:
  - python=3.11
  - pip
  - pip:
      - pytest
```

Add this to `C:\Users\admin\Desktop\MyAgent\05-my-first-agent\my-first-agent\README.md`:

```md
# My First Agent

## 能力

- `get_time`
- `save_note`
- `read_notes`

## 运行方式

```powershell
conda env create -f environment.yml
conda activate myagent
python app.py
```

## 试试看

- `time`
- `save learn Agent`
- `read notes`
```

Create an empty `notes.txt`.

- [ ] **Step 7: Verify project behavior**

Run:

```powershell
cd 'C:\Users\admin\Desktop\MyAgent\05-my-first-agent\my-first-agent'
python app.py
```

Expected interaction:

```text
You: time
Agent: The current time is ...
You: save learn Agent
Agent: Saved note: learn Agent
You: read notes
Agent: learn Agent
```

### Task 5: Final Workspace Verification And Handoff

**Files:**
- Verify only

- [ ] **Step 1: List the final workspace tree**

Run:

```powershell
Get-ChildItem 'C:\Users\admin\Desktop\MyAgent' -Recurse
```

Expected: all planned learning folders and the runnable project are present.

- [ ] **Step 2: Check the key entry points**

Run:

```powershell
Get-Content -Raw 'C:\Users\admin\Desktop\MyAgent\README.md'
Get-Content -Raw 'C:\Users\admin\Desktop\MyAgent\05-my-first-agent\my-first-agent\README.md'
```

Expected: the learner can understand where to start and how to run the project.

- [ ] **Step 3: Prepare the user-facing summary**

The final summary should include:

```md
- what files were created
- where to start reading
- how to create the `conda environment`
- how to run the first local `Agent`
```
