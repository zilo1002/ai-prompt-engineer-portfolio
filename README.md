# Universal AI Prompt Service

[![FastAPI](https://img.shields.io/badge/FastAPI-0.95.2-blue)]()
[![Python](https://img.shields.io/badge/Python-3.11-green)]()

---

## 项目概览

这是一个 **通用 AI Prompt + API 框架**，可以快速将任意领域的 Prompt 封装成可调用的服务接口。  
无论是客服、内容生成、教学、科研，还是创意类应用，都可以直接复用。

### 核心特色

- **Prompt 版本管理**  
  - 支持多版本 Prompt（v1 / v2 / v3）  
  - 可在运行时切换不同版本  
- **API 服务化**  
  - FastAPI 封装 `/reply` 接口  
  - 支持前端、脚本、系统调用  
- **评测与优化**  
  - 内置 eval 模块（Rouge-L / 人工打分）  
  - 可快速对比不同 Prompt 的效果  
- **轻量可扩展**  
  - 新领域只需添加新 Prompt  
  - Eval 可扩展为任意指标（准确度、情绪、合规性等）

---

## 文件结构
. ├── README.md ├── app.py ├── prompts/ │   ├── 
v1_shot0_temp0.7.json │   ├── v2_shot3_temp0.3.json │   └── v3_cot_temp0.3.json └── eval/ ├── eval.py ├── eval_set.jsonl └── requirements.txt
---

## 快速开始

### 1. 安装依赖

```bash
pip install fastapi uvicorn pydantic
2. 运行 API 服务
uvicorn app:app --reload
访问：
http://127.0.0.1:8000
GET / → 健康检查
POST /reply → 发送用户输入，返回 AI 回复

示例（JSON POST）：
{
  "user_input": "请帮我生成一段产品文案。"
}

返回：
{
  "input": "请帮我生成一段产品文案。",
  "reply": "[MOCK RESPONSE] 请帮我生成一段产品文案。",
  "prompt_version": "v3_cot_temp0.3.json"
}

如何扩展到其他领域
在 prompts/ 添加新 Prompt JSON
修改 PROMPT_PATH 或改造 app.py 支持动态切换
可通过 eval/ 对不同 Prompt 进行离线或在线评测
