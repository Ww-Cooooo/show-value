# 片段匣：虚构的最小演示项目

这不是已发布产品。它专门用来演示如何从源码和开发背景整理介绍，所有示例资料与人物决定均为虚构，不含私人对话。

小程序将 JSON 里的摘录整理成 Markdown，可按标签筛选。每条摘录旁边保留标题和来源链接。它不抓网页，不自动同步，也不提供图形界面或 PDF 导出。

需要 Python 3.8 或更高版本，只用标准库。在本目录运行；UTF-8 模式用于兼容中文输入输出：

```text
python -X utf8 shelf.py clips.json
python -X utf8 shelf.py clips.json --tag 写作
```

结果显示在终端，不修改 clips.json，不自动创建输出文件。需要保存时自行复制输出或使用当前系统的输出重定向。

读者可以查 [实现](shelf.py)、[示例输入](clips.json)、[虚构开发记录](development-notes.md)，再回看上一级的完整示例。
