# Python Basics For This Project

这里只讲你做第一个 `Agent` 真正会用到的内容。

这不是完整 Python 教程。

## 1. variable

`variable` 就是给一个值起名字。

```python
tool_name = "get_time"
```

这里的意思是：把字符串 `"get_time"` 存进变量 `tool_name`。

## 2. string

`string` 就是一段文本。

```python
user_input = "save learn Agent"
```

你后面会经常处理用户输入，所以 `string` 很重要。

## 3. function

`function` 可以理解为“一个可重复使用的小动作”。

```python
def say_hello():
    print("hello")
```

后面你会写出这样的函数：

- `get_time()`
- `save_note(text)`
- `read_notes()`

## 4. if

`if` 用来做判断。

```python
if "time" in user_input:
    print("Call get_time")
```

你的第一个 `Agent` 会大量依赖这种最简单的判断逻辑。

## 5. import

当一个文件里写好了函数，另一个文件可以把它拿过来用。

```python
from tools import get_time
```

这句的意思是：

从 `tools.py` 里导入 `get_time` 这个函数。

## 6. 先不学什么

你现在不用着急学这些：

- class
- decorator
- async
- framework

不是它们不重要，而是你现在还没到需要它们的时候。

先把最小项目跑通，才是最划算的学习路径。
