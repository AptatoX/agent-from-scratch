# My First Agent

这是你的第一个本地命令行 `Agent` 项目。

## 这个项目有什么能力

- `get_time`
- `save_note`
- `read_notes`

## 你会看到什么

这个项目会向你展示一个最小 `Agent` 的完整闭环：

- 接收用户输入
- 判断该调用哪个工具
- 执行工具
- 读取工具结果
- 返回回复

## 创建环境

```powershell
conda env create -f environment.yml
conda activate myagent
```

如果你已经有同名环境，也可以直接使用已有的 `myagent`。

## 运行项目

```powershell
python app.py
```

## 你可以试试这些输入

- `time`
- `现在几点了`
- `save 今天开始学习 Agent`
- `read notes`
- `查看笔记`

## 你应该重点看哪两个文件

- `tools.py`
- `app.py`

先看 `tools.py`，再看 `app.py`，会更容易理解。
