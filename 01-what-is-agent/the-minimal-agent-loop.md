# The Minimal Agent Loop

你可以把一个最小 `Agent` 理解成下面这个循环：

1. receive input
2. decide
3. act
4. observe
5. reply

这 5 步非常重要，因为你后面写的第一个 `Agent`，本质上就是它的最小实现。

## 1. receive input

先接收用户输入。

比如你输入：

`time`

或者：

`save learn Agent`

## 2. decide

程序先做一个判断：

- 这句话只是普通聊天吗？
- 还是说应该调用某个工具？

这个判断过程就是最简单的 `decision`。

## 3. act

如果判断需要行动，`Agent` 就会调用一个工具。

比如：

- `get_time`
- `save_note`
- `read_notes`

这一步就是 `act`。

## 4. observe

工具执行完之后，`Agent` 不会凭空继续说，而是先读取工具的结果。

比如：

- 时间工具返回了当前时间
- 保存笔记工具返回了“保存成功”
- 读取笔记工具返回了已有笔记内容

这一步就是 `observe`。

## 5. reply

最后，`Agent` 根据拿到的结果给用户一个可理解的回复。

比如：

- `The current time is ...`
- `Saved note: ...`
- `Here are your notes: ...`

## 为什么这个循环重要

因为它帮你把 `Agent` 从“一个模糊概念”变成“一个可实现结构”。

以后你学更复杂的系统，比如：

- `Memory`
- `Planning`
- `RAG`
- `Multi-Agent`

本质上也还是在这个最小循环上继续扩展。
