# 05.5-from-rules-to-llm-agent

## 这一章在讲什么

这一章是从 `rule-based agent` 走向 `LLM-based agent` 的桥梁。

它不要求你马上重写整套系统，而是先帮你看懂一件最关键的事：

当“决定怎么做”这件事从规则慢慢交给模型之后，程序的结构会怎么变。

## 学完之后你会得到什么

学完这一章，你应该能更清楚地分辨：

- `rule-based agent`
- `LLM-based agent`
- `workflow`
- `tool calling`

更重要的是，你会开始理解为什么很多人说 `AI Agent` 的核心不是“会聊天”，而是“模型参与决策，并配合工具完成任务”。

## 推荐阅读顺序

1. `rule-based-vs-llm-based.md`
2. `how-tool-calling-changes-the-loop.md`
3. `upgrade-path.md`

如果你想先看一篇更完整的长文，也可以选读：

- `../docs/from-tool-calling-to-llm-agent.md`

## 本章建议阅读

- OpenAI: [Function calling](https://platform.openai.com/docs/guides/function-calling)
  适合在你已经理解规则型版本之后，再看“把工具选择交给模型”到底是什么意思。

- OpenAI: [Tools](https://platform.openai.com/docs/guides/tools?api-mode=responses)
  适合把“工具调用”放进更完整的官方框架里理解。

- Anthropic: [Tool use overview](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview)
  适合从另一个官方视角再看一遍“模型如何和工具配合”。
