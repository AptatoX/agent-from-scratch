# Files And Functions

你的第一个 `Agent` 不只是打印文本，它还会真的操作文件。

所以这一节你重点看两件事：

- 如何写函数
- 如何读写文件

## 一个保存笔记的函数

```python
def save_note(text):
    with open("notes.txt", "a", encoding="utf-8") as f:
        f.write(text + "\n")
```

你可以先把它读成人话：

- 定义一个叫 `save_note` 的函数
- 它接收一个参数 `text`
- 以追加模式打开 `notes.txt`
- 把这段文字写进去，再换一行

这里最值得你记住的是 `"a"`：

- `"a"` 表示 append，也就是追加
- 不会清空原内容

## 一个读取笔记的函数

```python
def read_notes():
    with open("notes.txt", "r", encoding="utf-8") as f:
        return f.read()
```

这段代码的意思是：

- 以读取模式打开 `notes.txt`
- 把文件内容全部读出来
- 返回给调用它的地方

这里的 `"r"` 表示 read。

## 为什么函数很适合拿来做 `Tool`

你可以把一个 `Tool` 先理解成：

“程序可以调用的一段明确动作”

而函数本来就是“明确动作”的天然表达形式。

比如：

- `get_time()` 是一个动作
- `save_note(text)` 是一个动作
- `read_notes()` 是一个动作

所以在你的第一个项目里，`Tool` 基本就会以函数的形式出现。

## 这一节你应该带走什么

先不用死记语法细节。

你只需要先建立这层理解：

- 函数负责封装动作
- 文件读写让 `Agent` 能和本地世界发生联系
- `Tool` 往往就可以先由一个函数来实现
