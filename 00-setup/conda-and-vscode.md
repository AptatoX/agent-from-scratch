# conda And VS Code

## 目标

完成这一节后，你应该能在 `VS Code` 中打开 `MyAgent` 文件夹，并用独立的 `conda environment` 运行 `Python`。

## 为什么要用独立环境

你现在是零基础，所以最重要的是减少混乱。

独立的 `conda environment` 有几个好处：

- 不会污染系统里的其他 `Python`
- 这个项目需要什么，就只装什么
- 以后出问题也更容易排查

## 第一步：确认 `conda` 可用

在 `PowerShell` 里运行：

```powershell
conda --version
```

如果能看到版本号，说明 `conda` 已经可用。

## 第二步：创建环境

在终端里运行：

```powershell
conda create -n myagent python=3.11 -y
```

这条命令的意思是：

- 创建一个叫 `myagent` 的环境
- 里面安装 `Python 3.11`

## 第三步：激活环境

```powershell
conda activate myagent
```

激活后，你通常会看到命令行前面出现 `(myagent)`。

然后运行：

```powershell
python --version
```

如果显示的是 `Python 3.11.x`，就说明环境激活成功了。

## 第四步：用 VS Code 打开文件夹

打开 `VS Code`，选择：

`File -> Open Folder`

然后打开：

`C:\Users\admin\Desktop\MyAgent`

## 第五步：先安装 Python 扩展

这是很多零基础学习者最容易卡住的地方。

`VS Code` 刚安装好时，不一定自带 `Python` 开发能力。所以在选择解释器之前，你要先安装扩展。

按：

`Ctrl + Shift + X`

打开扩展页，然后搜索并安装：

- `Python`
  发布者是 `Microsoft`
- `Pylance`
  发布者是 `Microsoft`

安装完成后，建议执行一次：

`Ctrl + Shift + P`

输入：

`Developer: Reload Window`

这样可以让新装扩展马上生效。

## 第六步：在 VS Code 里选择解释器

按 `Ctrl + Shift + P`，输入：

`Python: Select Interpreter`

然后选择刚才创建的 `myagent` 环境。

如果你看到多个解释器，不要慌。只需要选择名字里带 `myagent` 的那个。

## 第七步：运行第一个 Python 文件

切到 `00-setup` 目录，运行：

```powershell
python hello.py
```

如果输出：

```text
Hello from MyAgent!
```

说明你的环境已经可以开始学习和做项目了。

## 常见问题

### `conda` 命令找不到

这通常说明 `Miniconda3` 没有正确加入终端环境。

先不要乱改配置，优先确认：

- `Miniconda3` 是否真的安装成功
- 你是不是开的新终端

### `conda activate myagent` 提示要先运行 `conda init`

如果你看到了：

```text
CondaError: Run 'conda init' before 'conda activate'
```

先运行：

```powershell
conda init
```

然后关闭当前 `PowerShell`，重新打开一个新终端，再执行：

```powershell
conda activate myagent
```

如果你发现运行了 `conda init` 还是不行，就要怀疑是 `PowerShell profile` 没加载对。

这个问题的本质通常不是环境没创建，而是当前终端没有正确加载 `conda` 的初始化脚本。

### `Python: Select Interpreter` 搜不到

这通常不是 `conda` 的问题，而是 `VS Code` 还没有安装 `Python` 扩展。

请先确认你已经安装：

- `Python` by Microsoft
- `Pylance` by Microsoft

安装后执行一次：

`Developer: Reload Window`

然后再搜索：

`Python: Select Interpreter`

### VS Code 运行时不是你创建的环境

这通常是解释器没选对。

重新执行：

`Python: Select Interpreter`

### 命令可以在终端运行，但 VS Code 里还是报错

大概率是：

- 终端环境对了
- 但编辑器的解释器没切过来

这两个是分开的，初学者很容易混淆。
