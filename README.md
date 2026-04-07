# agent-from-scratch

Learn how to build an `Agent` from scratch in `Python`, starting with a minimal rule-based version and gradually evolving toward an `LLM-based agent`.

这是一个面向初学者的学习型项目仓库。它不是一上来就把你丢进复杂框架，而是先带你看懂最小 `Agent loop`，再一步步理解 `tool calling`、`workflow`、`LLM-based agent` 这些真正关键的概念。

## Who This Is For

这个仓库特别适合：

- 想从零开始理解 `Agent`
- 会一点点终端操作，但还不熟悉 `Python`
- 不想一开始就被框架和 API 细节淹没
- 想先看懂结构，再逐步升级成更真实的 `AI Agent`

## What You Will Build

你会先完成一个最小可运行的命令行 `Agent`。

第一版项目包含 3 个工具：

- `get_time`
- `save_note`
- `read_notes`

它展示的是一个最小但完整的 `Agent loop`：

`input -> decide -> act -> observe -> reply`

然后你会继续学习：

- `rule-based agent` 和 `LLM-based agent` 的区别
- 为什么 `tool calling` 是现代 `AI Agent` 的核心能力之一
- 如何从规则驱动版本自然升级到模型驱动版本

## Learning Path

建议按这个顺序学习：

1. [00-setup](./00-setup/README.md)
2. [01-what-is-agent](./01-what-is-agent/README.md)
3. [02-python-for-agent](./02-python-for-agent/README.md)
4. [03-agent-core](./03-agent-core/README.md)
5. [04-exercises](./04-exercises/README.md)
6. [05-my-first-agent](./05-my-first-agent/README.md)
7. [05.5-from-rules-to-llm-agent](./05.5-from-rules-to-llm-agent/README.md)
8. [06-glossary](./06-glossary/README.md)
9. [07-next-steps](./07-next-steps/README.md)

## Project Structure

```text
agent-from-scratch/
├─ 00-setup/
├─ 01-what-is-agent/
├─ 02-python-for-agent/
├─ 03-agent-core/
├─ 04-exercises/
├─ 05-my-first-agent/
├─ 05.5-from-rules-to-llm-agent/
├─ 06-glossary/
├─ 07-next-steps/
├─ recommended-reading.md
└─ README.md
```

## Quick Start

如果你只是想先跑起来，按下面这几步来：

1. 创建环境

```powershell
conda create -n myagent python=3.11 -y
conda activate myagent
```

2. 打开项目

用 `VS Code` 打开当前仓库，然后安装：

- `Python` by Microsoft
- `Pylance` by Microsoft

3. 跑第一个文件

```powershell
cd .\00-setup
python hello.py
```

4. 跑最小 Agent

```powershell
cd ..\05-my-first-agent\my-first-agent
python app.py
```

你可以试试这些输入：

- `time`
- `save 今天开始学习 Agent`
- `read notes`

## Recommended Reading

根目录有一份 [recommended-reading.md](./recommended-reading.md)。

它按学习阶段整理了官方文档和补充视频，适合边学边看，而不是一口气全读完。

## Current Scope

当前仓库里的主项目还是教学版：

- 它已经是一个最小 `Agent` 结构演示
- 但决策层目前还是规则驱动
- 还没有把工具选择交给 `LLM`

这不是缺点，而是刻意设计的学习路径。

先把结构看懂，再接 `LLM`，你会更稳。

## Extra Reading

如果你学到 `05.5` 或 `06` 时，想看一篇更连续、更完整的讲解，可以继续读：

- [从 Tool Calling 到 LLM Agent](./docs/from-tool-calling-to-llm-agent.md)

## Next Step

如果你是第一次打开这个仓库，直接从 [00-setup](./00-setup/README.md) 开始。
