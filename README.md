# ai-doc-assistant
My first AI project using LangChain
# AI 文档智能总结助手 (AI Document Assistant)

## 📖 项目简介
这是一个基于 Python 和 LangChain 框架开发的 AI 文档总结工具。通过调用 DeepSeek 大语言模型 API，能够读取本地文本文件，并自动提取、总结核心要点。

## 🛠️ 技术栈
- **语言**: Python 3.13
- **框架**: LangChain (LCEL 表达式、ChatPromptTemplate)
- **模型**: DeepSeek API (兼容 OpenAI 接口)
- **工具**: TextLoader 文档加载器

## ⚙️ 核心功能
1. 使用 `TextLoader` 读取本地 `.txt` 文件并转化为标准文档对象。
2. 使用 `ChatPromptTemplate` 构建系统级提示词，设定 AI 为总结助手角色。
3. 通过 LCEL 管道符 `|` 将 Prompt 与 LLM 串联成流水线。
4. 调用大模型完成长文本的要点提炼。

## 🚀 如何运行
1. 安装依赖：`pip install langchain langchain-openai langchain-community`
2. 在代码中填入你自己的 API Key。
3. 运行 `rag_demo.py` 即可。
