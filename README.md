# 机器人装配工程级云端跨平台知识库（1985–2025）

本知识库整合了两部横跨 40 年的机器人装配核心著作：
- **Book2025**：*Robotic Intelligent Assembly*（Jing Xu, Hao Su, Rui Chen, Zhimin Hou，Springer 2025，11 章）
- **Book1985**：*Robotic Assembly*（Keith Rathmill 主编，IFS / Springer-Verlag 1985，6 篇 27 篇论文）

内置 **开放数据层（Markdown + Parent-Child JSONL + SQLite 混合检索库）+ 云端双协议服务（FastAPI OpenAPI + 远程 MCP Streamable HTTP + Bearer API Key 鉴权）**，一次部署即可在 **Gemini、Claude、ChatGPT、Cursor、Windsurf、Dify、RAGFlow、LangChain、CrewAI** 全平台通用。

---

## 一、云端一键部署（5 分钟上线公网 HTTPS）

### 方案 A：Render（免绑卡，最省事）
1. 将解压后的 `robotic_assembly_kb/` 文件夹推送到你的 GitHub 仓库（支持私有仓库）。
2. 登录 [Render](https://render.com/) → **New +** → **Blueprint**，选择该仓库。
3. Render 会自动读取 `render.yaml`，在新加坡节点构建 Docker 容器并**自动生成强随机 `KB_API_KEY`**。
4. 部署完成后，在 Render 控制台的 **Environment** 页复制自动生成的 `KB_API_KEY`，以及顶部生成的公网 URL（如 `https://robotic-assembly-kb.onrender.com`）。

### 方案 B：Google Cloud Run（低延迟、近乎无冷启动，推荐正式使用）
无需在本地安装 Docker，直接在浏览器打开 [Google Cloud Shell](https://shell.cloud.google.com/)，上传并解压本压缩包后执行：

```bash
cd robotic_assembly_kb
export KB_API_KEY="$(python3 -c 'import secrets; print(secrets.token_urlsafe(24))')"
echo "请妥善保存你的 API Key: $KB_API_KEY"

bash deploy/deploy_cloud_run.sh robotic-assembly-kb asia-southeast1
```

部署完成后会返回永久公网 HTTPS 地址（如 `https://robotic-assembly-kb-xxxx-as.a.run.app`）。

---

## 二、全平台 AI 与 Agent 接入方式

假设你的云端地址为 `https://YOUR-CLOUD-URL`，密钥为 `YOUR_KB_API_KEY`：

1. **Claude / Cursor / Windsurf / Gemini CLI（远程 MCP）**
   将 `configs/mcp_client_configs.json` 中的 `cloud_remote_mcp_http`（或 `gemini_cli_remote_mcp`）填入客户端 MCP 配置，指向 `https://YOUR-CLOUD-URL/mcp`，Header 带 `Authorization: Bearer YOUR_KB_API_KEY`。
2. **ChatGPT Custom GPT / Dify / Coze（OpenAPI Actions）**
   - Schema URL 填：`https://YOUR-CLOUD-URL/openapi.json`
   - 鉴权方式选：**API Key → Bearer**，填入 `YOUR_KB_API_KEY`
   - 系统提示词直接复制 `configs/system_prompt_rag.md`
3. **Gemini Gem / NotebookLM / Claude Project（零代码文件导入）**
   直接上传 `kb/` 下的 4 个 `.md` 文件即可。
4. **本地零依赖 Stdio MCP（无需云端）**
   直接运行 `python3 servers/mcp_server.py`（仅用 Python 3 标准库）。

---

## 三、接口速查与冒烟测试

```bash
# 1. 健康检查（无需鉴权）
curl https://YOUR-CLOUD-URL/health

# 2. 混合检索（需 Bearer Token）
curl -X POST https://YOUR-CLOUD-URL/search \
  -H "Authorization: Bearer YOUR_KB_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "对比 1985 RCC 与 2025 HC-CPS 柔顺控制", "top_k": 3}'

# 3. 远程 MCP tools/list 测试
curl -X POST https://YOUR-CLOUD-URL/mcp \
  -H "Authorization: Bearer YOUR_KB_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc": "2.0", "id": 1, "method": "tools/list", "params": {}}'
```

---

## 四、本地扩展至两本 PDF 完整 636 页逐页全文

如需把两本原书的全部 246 + 390 = 636 页逐页原文与扫描表格并入知识库，在本地有原 PDF 的机器上运行：

```bash
pip install -r configs/requirements.txt
python3 etl/pdf_dual_track_etl.py \
  --book2025 "/path/to/Robotic Intelligent Assembly (2025).pdf" \
  --book1985 "/path/to/Robotic assembly (1985).pdf" \
  --vlm-provider none
```
执行完成后会自动更新 `kb/robotic_assembly_kb.db`，重新推送部署一次即可全平台生效。
