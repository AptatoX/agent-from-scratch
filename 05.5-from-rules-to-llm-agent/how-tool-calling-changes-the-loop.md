# How Tool Calling Changes The Loop

你已经知道最小循环可以写成：

`input -> decide -> act -> observe -> reply`

当规则型 agent 升级成 `LLM-based agent` 时，这个循环没有消失，只是“decide”这一步换了地方。

## 先看规则型版本

```text
user input
-> program rules decide
-> call tool
-> get tool result
-> print response
```

在这个版本里，程序自己判断要不要调用工具，也自己决定用哪个工具。模型还没有真正参与决策。

## 再看 tool calling 版本

```text
user input + history + available tools
-> program sends them to the model
-> model decides: answer now or request a tool
-> if tool is needed, program executes it
-> program sends tool_result back to the model
-> model reads the result and continues
-> model returns the final answer
```

这里最重要的变化是：

- 程序不再只把一句用户输入丢给模型
- 程序会把消息历史、可用工具，一起发给模型
- 模型先判断自己是直接回答，还是先请求一个工具
- 如果模型请求工具，程序负责真正执行
- 执行完以后，程序把 `tool_result` 再送回模型
- 模型读到结果后，继续组织下一步，直到给出最终回答

## 这意味着什么

`tool calling` 不是“模型自己跑去执行代码”。

更准确地说，是：

1. 模型负责决定
2. 程序负责执行
3. 结果再回到模型继续推理

所以你可以把它理解成一种分工：

- 模型像“会思考的调度者”
- 程序像“真正干活的执行者”

## 为什么这一步很关键

一旦进入这种循环，很多以前只能靠硬编码处理的事，就可以让模型参与了。

比如：

- 什么时候该查时间
- 什么时候该读笔记
- 什么时候该把用户的话整理成结构化参数

你不用把所有规则都写死，程序也不必只会固定模板。
模型可以先看上下文，再决定下一步该不该调用工具。

## 一句话记忆

`tool calling` 的核心不是“模型替你执行工具”。

核心是：

**程序把上下文和工具交给模型，模型决定要不要用工具；如果要用，程序执行，然后把结果再交回模型继续。**
