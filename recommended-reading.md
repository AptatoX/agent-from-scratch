# Recommended Reading

这份清单只放值得读的官方材料。

你不用一上来全读完。正确方式是：学到对应阶段，再读对应材料。

## 现在先读

- Anthropic: [Building Effective AI Agents](https://www.anthropic.com/engineering/building-effective-agents)
  为什么现在读：这篇很适合帮你建立对 `Agent` 的第一层直觉。
  重点看什么：`Agent` 不一定要很复杂，很多有效系统其实来自简单、清晰、可组合的模式。
  建议程度：必读

- Jeff Su: [AI Agents, Clearly Explained](https://www.youtube.com/watch?v=FwOTs4UxQS4)
  为什么现在看：按可获取摘要，这个视频面向非技术背景用户，适合在一开始快速建立 `LLM -> workflow -> agent` 的层次感。
  重点看什么：普通 `LLM`、固定 `workflow`、以及能自主决策的 `agent` 之间到底差在哪。
  建议程度：推荐

## 学到 `Tool Calling` 时再读

- OpenAI: [Function calling](https://platform.openai.com/docs/guides/function-calling)
  为什么这时读：你会开始理解模型如何“决定调用工具”，这篇会和你手里的小项目直接对应起来。
  重点看什么：工具定义、参数、模型返回的工具调用意图。
  建议程度：必读

- OpenAI: [Tools](https://platform.openai.com/docs/guides/tools?api-mode=responses)
  为什么这时读：它能帮你把 `tools` 作为一个统一概念来看，而不是碎片化记忆。
  重点看什么：不同工具能力的角色，以及工具为什么让模型“能做事”。
  建议程度：推荐

## 做完第一个小项目后再读

- OpenAI: [Agents SDK](https://platform.openai.com/docs/guides/agents-sdk/)
  为什么做完再读：如果现在读，你会觉得很抽象；做完本地小项目后再看，会立刻看懂很多设计。
  重点看什么：官方 SDK 怎么把 `Agent`、`Tools`、执行流组织起来。
  建议程度：推荐

- Anthropic: [Tool use overview](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview)
  为什么做完再读：这篇会帮你用另一家官方视角再理解一遍工具调用。
  重点看什么：模型、工具、执行结果之间如何来回传递。
  建议程度：推荐

## 以后扩展再读

- Anthropic: [Resources overview](https://docs.anthropic.com/en/resources/overview)
  为什么以后读：这里更适合作为进阶导航，不适合零基础一开始就扎进去。
  重点看什么：你真正需要的 cookbook、prompt guide、进阶文档。
  建议程度：可选

## 读的时候记住

- 不是每篇都要逐字读完
- 优先抓住概念，不追求一遍全懂
- 读完后回到你自己的小项目上验证理解
