# 05.5-from-rules-to-llm-agent

## 这一章学什么

这一章是桥接章。

它的作用不是立刻让你写一大堆新代码，而是帮你把一个关键问题彻底想明白：

“我现在这个规则型 `Agent`，怎么才算升级成真正的 `LLM-based agent`？”

## 学完后你会得到什么

完成后，你应该能清楚区分：

- `rule-based agent`
- `LLM-based agent`
- `workflow`
- `tool calling`

你也会知道，为什么很多人说的 `AI Agent`，核心其实不是“会聊天”，而是“模型参与决策并调用工具”。

## 建议阅读顺序

1. `rule-based-vs-llm-based.md`
2. `how-tool-calling-changes-the-loop.md`
3. `upgrade-path.md`

## 本章建议阅读

- OpenAI: [Function calling](https://platform.openai.com/docs/guides/function-calling)
  为什么现在读：你已经完成了规则型版本，现在正好适合理解“把工具选择交给模型”到底意味着什么。

- OpenAI: [Tools](https://platform.openai.com/docs/guides/tools?api-mode=responses)
  为什么现在读：这会帮助你把“工具调用”放到更完整的官方框架里理解。

- Anthropic: [Tool use overview](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview)
  为什么现在读：它能帮你从另一家官方视角再看一遍“模型如何与工具来回交互”。
