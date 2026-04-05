# How Tool Calling Changes The Loop

你已经知道最小循环是：

`input -> decide -> act -> observe -> reply`

当你把规则型版本升级成 `LLM-based agent` 时，这个循环本身没有消失，但 `decide` 和 `reply` 两步会明显变化。

## 规则型版本的循环

```text
user input
-> program rules decide
-> call tool
-> get tool result
-> print response
```

这里的“脑子”主要是你写的 `if/else`。

## LLM 参与后的循环

```text
user input
-> LLM decides whether to call a tool
-> tool executes
-> tool result returns
-> LLM reads result
-> LLM writes final answer
```

这里的“脑子”开始变成：

- 一部分是程序
- 一部分是模型

## 真正变化最大的地方

### 1. 工具选择变灵活

你不用再把所有触发词都手写出来。

例如用户说：

- `现在几点`
- `帮我看下时间`
- `what time is it`

规则型程序可能要写很多判断。

但 `LLM` 通常能把这些都理解为“应该调用 `get_time`”。

### 2. 参数提取更自然

比如：

`帮我记一下，今天开始正式学 Agent`

规则型程序通常只能处理固定格式，比如：

`save 今天开始正式学 Agent`

但 `LLM` 可以更自然地提取出真正应该写入 `save_note` 的内容。

### 3. reply 也更像自然语言

规则型版本通常只能输出固定模板。

而 `LLM` 可以把工具结果整理成更自然、更贴近用户意图的回答。

## 你要记住的一点

`tool calling` 不是“模型自己真的去执行代码”。

更准确地说，是：

- 模型表达“我想调用哪个工具、参数是什么”
- 你的程序真正去执行工具
- 再把执行结果交还给模型或交还给程序继续处理

也就是说，真正执行工具的始终还是程序，不是模型本身。
