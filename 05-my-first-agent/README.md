# 05-my-first-agent

## 这一章学什么

这一章开始真正做项目。

你会把前面学到的东西拼起来，完成一个本地命令行 `Agent`。

## 学完后你会得到什么

完成后，你应该能：

- 在终端运行自己的 `Agent`
- 让它调用简单工具
- 保存和读取本地笔记

## 先说清楚：这是不是“真正的 Agent”

它是一个真正的最小 `Agent` 结构演示，但还不是现在最常见的那种 `LLM-based agent`。

为什么这样说：

- 它已经有输入、决策、行动、观察、回复
- 但“决策”这一步目前是规则写死的
- 还不是由 `LLM` 来判断工具选择

所以这一章的项目更准确地说，是：

- `rule-based agent`
- 或者 `minimal agent loop demo`

它的教学价值在于先让你看清结构。

等你把这一版跑通后，下一步就可以把规则判断升级成：

- `LLM` 读入用户输入
- `LLM` 决定调用哪个工具
- 工具返回结果
- `LLM` 再基于结果生成最终回复

## 建议阅读顺序

1. `my-first-agent/README.md`
2. `my-first-agent/tools.py`
3. `my-first-agent/app.py`

## 本章建议阅读

- OpenAI: [Function calling](https://platform.openai.com/docs/guides/function-calling)
  这时再看，你会更容易把官方表达和自己的项目结构对应起来。
