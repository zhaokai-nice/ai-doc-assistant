from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import TextLoader
print('正在读取文件。。。')
loader=TextLoader('data.txt',encoding='utf-8')
docs=loader.load()
file_content=docs[0].page_content
llm=ChatOpenAI(
    api_key='sk-c7e265e5969c4fba8dcde57bb1463e3e',
    base_url='https://api.deepseek.com',
    model='deepseek-chat'
)
prompt=ChatPromptTemplate.from_messages([
    ('system','你是一个专业的文档总结助手，请用精炼的语言提取要点。'),
    ('user','请帮我总结以下这段文字的要点：\n\n{text}')
    ])
chain=prompt|llm
print('文件读取成功，正在呼叫ai总结。。。\n')
result=chain.invoke({'text':file_content})
print('ai总结结果：')
print(result.content)