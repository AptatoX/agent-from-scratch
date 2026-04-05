# Glossary

这里不把术语硬翻成奇怪中文，而是保留英文术语，用中文解释它们的意思。

## Agent

一个不仅能 reply，还能 decide、act、observe 的系统。

## Prompt

给模型的输入说明。它会影响模型如何理解任务和如何输出结果。

## Tool

`Agent` 可以调用的一种动作能力。

## Tool Calling

模型或程序决定去调用某个工具的过程。

## Memory

系统把过去信息保存下来，并在后续任务中继续使用的能力。

## Planning

把一个目标拆成若干步骤，再按顺序执行或调整的过程。

## Observation

读取工具执行结果的过程。

## Loop

系统重复执行的一组流程，例如 `input -> decide -> act -> observe -> reply`。

## Context

当前可被系统看到和使用的信息范围。

## RAG

`Retrieval-Augmented Generation`。先检索相关信息，再结合检索结果生成回答。

## Workflow

按固定步骤执行的一条流程，通常比 `Agent` 更可预测。

## Multi-Agent

多个 `Agent` 分工协作完成任务。
