# Awesome Claude API 中转资源汇总

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![GitHub Stars](https://img.shields.io/github/stars/peter123023/awesome-claude-api)
![GitHub License](https://img.shields.io/github/license/peter123023/awesome-claude-api?color=blue)
![Last Updated](https://img.shields.io/badge/last%20updated-2026--09-brightgreen)

中文 | [English](README_EN.MD)

精心收集和整理的可靠Claude中转API资源列表，帮助开发者快速找到稳定、高性价比的Claude API服务。所有信息均来自官方网站，确保时效性和准确性。

## 📊 月访问量数据情况（2026-09） <a id="traffic-note"></a>

本期对比 2026-08 与 2026-09 两个月访问量，共覆盖 22 个渠道（已移除停服的 Unity2.Ai，新增收录 LinkAGI、Kunavo、TokenDos、AI SaaS Go、API 快连 与 AnyAIGC）。

- **头部稳健**：OpenRouter 22.0M → 21.3M（-3.4%），仍是唯一千万级渠道，头部格局稳定。
- **涨幅偏大**：API 快连 +7785.8%、Kunavo +2778.2%、LLM 大模型照妖镜 +310.1%、B.AI +78.6%、AIHubMix +12.1%。前三者为低基数新站或工具站。
- **普遍回落**：AIGoCode -58.6%、EasyRouter -50.6%、ZenMux -43.9%、TokenDos -29.2%、YesCode -16.0%、IKunCode -15.3%、CCTest -14.5%、TeamoRouter -13.0%、LinkAGI -10.0%、OfoxAI / Ofox 模型验真 -3.8%。
- **基本持平与无数据**：CoderPlan、FerryAPI 两月估算均为 0；AICoding 9 月归零（8 月沿用旧平台数值，-100% 无法倒推基数）；AI SaaS Go、AnyAIGC 暂无第三方估算数据。
- **新收录**：API 快连 162 → 12.8K（+7785.8%），2026-06 上线的新站，9 月起量；LinkAGI 10.6K → 9.6K（-10.0%）、Kunavo 156 → 4.5K（大幅增长）、TokenDos 4.9K → 3.5K（-29.2%），三站均为 2026 年新上线；AnyAIGC 暂无第三方估算数据（品牌 2026-04 起步，2026-09 由 anyaigc.com 迁移至现域）。

## 📋 目录

[访问量数据情况](#traffic-note) | [项目介绍](#intro) | [使用说明](#usage) | [API列表](#api-list) | [检测工具](#tools) | [贡献指南](#contributing) | [免责声明](#disclaimer)

## 🚀 项目介绍 <a id="intro"></a>

本项目致力于收集全球范围内稳定可靠的Claude中转API服务，为开发者提供一个权威、更新及时的资源参考。所有收录的API服务均经过初步筛选，确保具备基本的可用性和稳定性。

## 📝 使用说明 <a id="usage"></a>

1. 所有服务均为第三方提供，使用前请仔细阅读各服务商的官方文档和服务条款
2. 建议先试用免费额度或小额套餐，确认服务符合需求后再进行长期付费
3. 价格和政策可能会有变动，请以服务商官方网站最新信息为准

## 🔌 API列表 <a id="api-list"></a>

| 服务商 | 费用结构 | 综合评价 | 标签 |
|-------|---------|----------|------|
| [OpenRouter](https://openrouter.ai/)<br><sub>openrouter.ai<br>月访问量: 22.0M (2026-08) → 21.3M (2026-09) ▼跌 3.4%</sub> | • 无订阅制，按量付费，统一信用点抵扣所有模型费用<br>• 价格公开透明，不同Claude版本定价不同<br>• 新用户注册可获得免费试用额度 | • 全球最大的LLM聚合平台，500万+用户，月处理70T Tokens<br>• 全面支持Claude全系列模型（包含最新Claude Opus 4.7）<br>• 多上游自动故障转移，服务可用性高<br>• 完全兼容OpenAI SDK格式，几乎零代码适配<br>• 支持边缘节点加速、精细数据隐私控制、团队管理等功能 | `全球知名` `全Claude版本支持` `高可靠` `SDK兼容好` |
| [AIHubMix](https://aihubmix.com/)<br><sub>aihubmix.com<br>月访问量: 253.6K (2026-08) → 284.3K (2026-09) ▲涨 12.1%</sub> | • 按量付费无强制订阅，价格与官方基本同步<br>• 新用户及合作伙伴可享10%长期折扣<br>• 账单透明可查，支持多种支付方式 | • 全球主流LLM聚合平台，全面支持Claude全系列模型（含最新Opus 4.7、Sonnet 4.6）<br>• 月处理超千亿Tokens，海量企业开发者使用，服务稳定性极高<br>• 边缘节点自动路由，全球访问速度快，并发支持强<br>• 完全兼容OpenAI、Anthropic官方API协议，零代码适配<br>• 支持联网搜索、多模态、视频生成等高级特性，模型更新速度极快 | `多模型支持` `高稳定` `低延迟` `SDK兼容好` `模型更新快` |
| [ZenMux](https://zenmux.ai/)<br><sub>zenmux.ai<br>月访问量: 678.4K (2026-08) → 380.9K (2026-09) ▼跌 43.9%</sub> | • 支持按量付费（PAYG）和订阅套餐两种模式<br>• 完全兼容OpenAI、Anthropic官方协议，无额外适配成本<br>• 公开透明计费，详细消耗可查，无隐藏费用<br>• 创新AI异常补偿机制，输出不理想自动赔付 | • 全球顶级模型聚合平台，仅提供官方/授权渠道的原版模型，无降配/残次<br>• 多提供商自动故障切换，Cloudflare全球边缘加速，服务稳定性极高<br>• 内置模型智能路由，自动匹配性价比最高的模型<br>• 多维度消费统计看板，方便成本优化<br>• 全球大量企业和开发者使用，支持个人/团队/企业级需求 | `国际知名` `高稳定` `多模型支持` `异常赔付` `企业级` |
| [IKunCode](https://api.ikuncode.cc/)<br><sub>api.ikuncode.cc<br>月访问量: 81.8K (2026-08) → 69.3K (2026-09) ▼跌 15.3%</sub> | • 价格信息请访问官方模型广场页面查看<br>• 支持多种模型计费方式 | • 提供完善的API文档支持<br>• 控制台功能齐全，使用管理方便<br>• 适合有一定技术基础的开发者使用 | `文档完善` `易管理` |
| [AIGoCode](https://www.aigocode.com/)<br><sub>www.aigocode.com<br>月访问量: 39.4K (2026-08) → 16.3K (2026-09) ▼跌 58.6%</sub> | • 订阅套餐：<br>&nbsp;&nbsp;- Standard：¥399/4周，周额度$110，9折优惠<br>&nbsp;&nbsp;- Premium：¥899/4周，周额度$260，86折优惠<br>&nbsp;&nbsp;- Professional：¥1799/4周，周额度$530，84折优惠<br>&nbsp;&nbsp;- 企业方案：¥9999/4周，定制化服务<br>• 灵活额度：¥50购$50，永久有效，按量扣费<br>• 优先消耗订阅额度，不足自动切换灵活额度 | • 服务稳定性达99.9%，已处理500万+任务<br>• 支持1v1专属工程师服务，问题响应及时<br>• 提供团队协作功能，支持额度共享和权限管理<br>• 适合个人开发者和企业团队使用<br>• 计费透明，无隐藏费用 | `高可用` `团队协作` `多套餐选择` `客服支持好` |
| [YesCode](https://co.yes.vg/)<br><sub>co.yes.vg<br>月访问量: 21.7K (2026-08) → 18.2K (2026-09) ▼跌 16.0%</sub> | • 免费额度：每月1M tokens<br>• 付费套餐：具体价格见官方定价页面<br>• 统一账单管理，支持多平台计费 | • 性能优异，平均延迟仅38ms<br>• 自动故障转移功能，服务稳定性高<br>• 支持Claude Code、Codex、Gemini等多模型路由<br>• 提供团队密钥管理和实时消费统计<br>• SOC 2 Type II认证，安全性高 | `高稳定` `低延迟` `多模型支持` `团队友好` |
| [AICoding](https://aicoding.sh/)<br><sub>aicoding.sh<br>月访问量: 2.3K (2026-08) → 0 (2026-09) ▼跌 100.0%</sub> | • 新用户福利：加入社区立得$5免费额度<br>• 具体定价方案可在登录后查看 | • 支持OpenClaw、VSCode等主流IDE无缝集成<br>• 高质量账号池动态调度，智能切换避免封号<br>• 一键安装无需配置，即开即用<br>• 已有10000+团队使用，服务稳定可靠 | `IDE集成友好` `防封号` `易部署` `新用户福利` |
| [EasyRouter](https://easyrouter.io/)<br><sub>easyrouter.io<br>月访问量: 9.2K (2026-08) → 4.6K (2026-09) ▼跌 50.6%</sub> | • 无订阅制，额度抵扣算力，用多少扣多少<br>• 五月全场Token消耗8.5折，DeepSeek-v4-Pro享2.5折特惠<br>• 多档额度套餐可选：$20/$100/$500/$1500 | • 傅盛团队出品，背景实力雄厚<br>• 统一OpenAI兼容接口，一行代码切换，零迁移成本<br>• 支持40+顶级大模型，全面覆盖Claude全系列模型<br>• 全球多节点部署，智能路由，P99延迟低于200ms<br>• 99.9%可用性SLA保障，自动故障转移与负载均衡 | `全模型支持` `低延迟` `高稳定` `大厂背景` `SDK兼容好` `新用户优惠` |
| [B.AI](https://b.ai/)<br><sub>b.ai<br>月访问量: 716.6K (2026-08) → 1.3M (2026-09) ▲涨 78.6%</sub> | • 一个 API Key 即可调用 Claude + GPT + Gemini + 国产大模型全系列<br>• 支持区块链地址登录，纯匿名支付（兼容邮箱/Visa/Master/Apple Pay）<br>• 官方 API 直连，零篡改，价格全网最低 | • 孙宇晨（Justin Sun）团队推出的AI模型聚合平台<br>• 官方公告：[孙哥Twitter](https://x.com/justinsuntron/status/2050104947342299208)<br>• BAIClaw 上线"孙哥大脑"功能，支持用孙哥思维交易加密货币 | `新上线` `孙宇晨团队` `全模型支持` `匿名支付` `加密友好` |
| [OfoxAI](https://ofox.ai/)<br><sub>ofox.ai<br>月访问量: 221.1K (2026-08) → 212.7K (2026-09) ▼跌 3.8%</sub> | • 无订阅制，按量付费，统一信用点抵扣所有模型费用<br>• 价格公开透明，不同模型定价不同<br>• 新用户注册可获得免费试用额度<br>• 支持微信、支付宝、信用卡付款 | • 一个 API Key 调用 100+ 大模型（GPT-5.4、Claude Opus 4.6、Gemini 3.1 等）<br>• 原生支持 OpenAI、Anthropic、Gemini 三种 SDK 协议，零代码适配<br>• 香港直连线路，国内访问延迟 100-300ms，无需代理<br>• 多上游智能路由，99.9% 可用性 SLA<br>• 支持团队协作、共享账单、API 用量管理等功能 | `国内直连` `多模型支持` `低延迟` `SDK兼容好` `团队友好` |
| [CoderPlan](https://coderplan.ai)<br><sub>coderplan.ai<br>月访问量: 0 (2026-08) → 0 (2026-09) 持平</sub> | • 按量付费，无月度绑定，充值档位：¥30/¥100/¥300/¥500（大额赠余额）<br>• Claude Opus 4.7 约1.2折（省88%），GPT系列约0.7折（省93%）<br>• 新用户注册赠送免费体验余额<br>• 支持支付宝、微信等国内常用支付方式 | • 支持Claude全系列（Opus 4.7/4.6、Sonnet 4.6），以及GPT、Gemini等主流模型<br>• 深度集成Claude Code、Cursor、Codex CLI、Gemini CLI等AI编程工具<br>• 智能缓存复用机制，显著降低重复调用成本<br>• 透明计费，每次调用详细记录模型、Token、缓存节省及消耗金额<br>• 兼容OpenAI API格式，零代码适配<br>• 提供系统运行状态页，服务稳定性可观测 | `价格优惠` `国内支付` `SDK兼容好` `多模型支持` `缓存省钱` |
| [FerryAPI](https://www.ferryapi.io/)<br><sub>www.ferryapi.io<br>月访问量: 0 (2026-08) → 0 (2026-09) 持平</sub> | • 预付费 USD 余额，按实际调用量扣费，无固定月费或订阅<br>• 新用户注册赠送 **$5 体验金**<br>• 邀请首笔付费用户可获 **1:1 同额赠送**<br>• 具体模型定价见[官方定价页](https://www.ferryapi.io/pricing) | • 低成本 OpenAI 兼容型 AI API 网关，一行代码迁移现有 OpenAI SDK 应用<br>• 聚合 9 大模型厂商：Claude、OpenAI、Gemini、DeepSeek、Qwen、Zhipu AI（智谱）、Kimi、MiMo、Doubao（豆包），一个 API Key 全部接入<br>• 提供商账户池机制，多上游自动调度<br>• 适用于客服、翻译、内容生成、摘要、分类和自动化等场景<br>• 官方文档完善：[ferryapi.io/docs](https://www.ferryapi.io/docs) | `Claude支持` `多模型聚合` `低成本` `新用户福利` `邀请返利` |
| [TeamoRouter](https://teamorouter.com/zh)<br><sub>teamorouter.com/zh<br>月访问量: 265.5K (2026-08) → 231.1K (2026-09) ▼跌 13.0%</sub> | • Claude 现价（每百万 token 输入/输出，以[官方模型页](https://teamorouter.com/zh/models)为准）：Opus 5.5 $1.144 / $5.72（约 2.9 折）、Sonnet 5.5 $0.568 / $2.84（2.8 折）、Fable 5.1 $3 / $15（3 折）、Haiku 5.5 $0.0286 / $0.143（2.9 折）<br>• 缓存按 Anthropic 官方比例计费，每条请求的 token 用量与扣费可在控制台逐条核对<br>• 支付宝直充，按量计费，用多少充多少，无需海外银行卡<br>• 失败请求不扣费，起充无门槛 | • Claude 在架型号：Opus 5.5 / Sonnet 5.5 / Fable 5.1 / Haiku 5.5 为现价主力，Opus 5、Sonnet 5、Opus 4.6 / 4.7 / 4.8、Sonnet 4.6、Haiku 4.5 等旧型号仍在架<br>• 双协议兼容：Anthropic Messages（Claude Code）+ OpenAI /v1/responses（Codex），一个 API Key 通吃，改 base_url 现有代码即刻运行<br>• 已内置于 CC Switch 与 Claude Code Router 预设，无需手填 API Key / Base URL<br>• 国内直连：无需科学上网，多线路备份<br>• 同时聚合 GPT 6.x / 5.x、Gemini、DeepSeek、GLM、Grok、Kimi 等共 59 个模型<br>• 官方模型页公开各模型的上下文长度、首字时延、输出速度与可用率 SLA（平台自报数据），可按需比对<br>• 文档教程：[teamorouter.com/zh/blogs](https://teamorouter.com/zh/blogs) | `多模型聚合` `双协议兼容` `2.8折起` `缓存官方比例` `国内直连` `按量付费` `Claude Code支持` `Codex支持` `一键接入` `CC Switch内置` `Claude Code Router预设` |
| [LinkAGI](https://api.linktoagi.com/)<br><sub>api.linktoagi.com<br>月访问量: 10.6K (2026-08) → 9.6K (2026-09) ▼跌 10.0%</sub> | • 人民币按量计费，无订阅制，用多少扣多少<br>• GPT-5.6 三档号池：Luna ¥0.15 / 百万输入 Token（输出约 ¥0.90）、Terra ¥0.375（输出约 ¥2.25）、Sol ¥0.75（输出约 ¥4.50）<br>• 新用户注册赠送 ¥0.2 试用额度<br>• 支持微信、支付宝付款，逐次调用可查 Token 与扣费 | • 为 Codex、Claude Code、Gemini CLI 与 OpenAI-compatible 客户端提供统一 API 接入<br>• 支持 OpenAI / Claude / Gemini 三类协议，Claude Code 用根地址、Codex 用 /v1，按客户端自动拼接<br>• 一手 GPT 号池，实时模型广场公开模型名、分组与价格<br>• 逐次调用日志记录模型、Token、响应状态与实际扣费<br>• 提供免费工具：地址诊断器、错误排查中心（401/403/404/429/504）、成本计算器、开源自检脚本<br>• 中文接入文档完善，国内直连，人工支持入口明确 | `人民币计费` `按量付费` `Claude Code支持` `Codex支持` `多协议兼容` `国内直连` `价格透明` |
| [Kunavo](https://kunavo.com/zh)<br><sub>kunavo.com/zh<br>月访问量: 156 (2026-08) → 4.5K (2026-09) ▲涨 2778.2%</sub> | • 预付钱包模式，$10 起充，无订阅、无月费、余额不过期<br>• Claude 价格（每百万 token 输入/输出）：Sonnet 5 $1.40/$7.00、Opus 5.5 $2.80/$14.00、Opus 5 $3.50/$17.50、Fable 5.1 $7.00/$35.00、Sonnet 4.6 $2.10/$10.50、Haiku 4.5 $0.70/$3.50<br>• 充值赠额：充 $100 送 $10、充 $1000 送 $200、充 $5000 送 $1250<br>• Stripe 原生计费：信用卡、Apple Pay、Google Pay、支付宝、微信 Pay，及巴西 Pix、韩国 KakaoPay、印度 UPI 等本地方式 | • OpenAI 兼容网关，聚合 OpenAI、Anthropic、Google 三家前沿模型，35 个在线模型，多数低于官方价、最高省 70%<br>• 改一行 base_url 即可迁移，OpenAI SDK drop-in 替代，streaming / function calling / tool use / vision 全线协议兼容<br>• 自动故障转移：每个请求最多在三条上游通道间依次回退，近期失败的通道在请求发出前即被绕开<br>• 原生流式 SSE pass-through，首字 token 时间与上游官方一致，不缓冲、不批处理<br>• Prompt 缓存命中按 10% 输入价计费（Claude Opus 5.5 为 5%、Fable 5.1 为 2.5%），最高省 90%<br>• 精细化用量：按模型 / API key / IP 维度分析，Webhook 推送，CSV 导出，支持按 key 设月度上限与 IP 白名单<br>• 53 个客户端集成（Claude Code、Cline、OpenClaw、n8n 等），每页对照官方文档核实并注明日期<br>• 透明定价，无隐藏乘数，失败请求不计费；美东 Anycast 边缘接入 | `OpenAI兼容` `多模型聚合` `最高省70%` `自动故障转移` `Prompt缓存` `Stripe计费` `Claude全系列` |
| [TokenDos](https://www.tokendos.com/tokendos)<br><sub>www.tokendos.com/tokendos<br>月访问量: 4.9K (2026-08) → 3.5K (2026-09) ▼跌 29.2%</sub> | • 实时按 token 付费，无订阅制<br>• 共享市场定价：聚合提供方闲置 API key，价格显著低于官方直连<br>• Claude Sonnet 5：$0.022 / 百万输入 token、$0.11 / 百万输出 token<br>• Prompt 缓存单独计价：Cache Read $0.0022、Cache Write $0.0275（每百万 token）<br>• GPT-6 Luna 低至 $0.000744 / 百万输入 token、$0.003722 / 百万输出 | • AI API 共享市场模式：连接闲置 API key 的提供方与需求方，把闲置算力变现，同时降低按需调用成本<br>• 双协议端点，可直接替换进现有代码<br>• 模型覆盖 GPT-6 系列（astra / sol / luna）、GPT-5.6（sol / terra）、GPT-5.5、Grok 4.6 / 4.7 及 Claude Sonnet 5<br>• 各模型 Prompt 缓存读 / 写分别计价，长上下文重复读取成本更低<br>• 新站（2026-06 上线），支付方式与团队功能等官方页面暂未公开 | `共享市场` `按量付费` `极低成本` `双协议` `Prompt缓存` `Claude支持` |
| [AI SaaS Go](https://aisaasgo.org/zh)<br><sub>aisaasgo.org/zh<br>月访问量: 暂无第三方估算数据</sub> | • 人民币按实付金额 1:1 到账（¥1 = $1 额度），¥5–¥1000 可充，无额外赠送<br>• Claude 价格（每百万 token 输入/输出）：Sonnet 5 / 4.6 / 4.5 均 $0.9/$4.5，Opus 5 $1.5/$7.5，Opus 5.5 $2/$10，Fable 5 / 5.1 $3/$15<br>• 输入、输出、缓存写入、缓存读取四列分别精确计量<br>• 支持银行卡与支付宝<br>• GPT 模型单次输入超 272K Token 触发长上下文计费（输入与缓存读取 2 倍、输出 1.5 倍）<br>• 视频 / 音频 / 图片模型独立计费，失败任务不扣费 | • 一个接口接入 OpenAI、Claude、Gemini、Grok、Kimi、DeepSeek 等模型<br>• Claude 覆盖 11 个型号：Fable 5 / 5.1、Opus 5.5 / 5 / 4.8 / 4.7 / 4.6 / 4.5、Sonnet 5 / 4.6 / 4.5<br>• 兼容 OpenAI Responses API（原生 SSE 流式），同时支持 Claude 原生接口（可用 x-api-key 鉴权）<br>• 多模态覆盖：文本、图片（GPT Image、Midjourney）、视频（Seedance）、音频（Suno、Doubao Seed Audio）<br>• 控制台可查 API Key、调用记录、Token 用量与实际消费<br>• 错误码文档完整（401/402/429/5xx 分别对应密钥、余额、限流、临时异常）<br>• 注意：第三方中转站评测曾记录其可用率偏低，生产使用建议先小额验证 | `Claude全系列` `多模态` `价格透明` `人民币充值` `双协议兼容` |
| [API 快连](https://apikl.ai/)<br><sub>apikl.ai<br>月访问量: 162 (2026-08) → 12.8K (2026-09) ▲涨 7785.8%</sub> | • 预付余额按量扣费，无月费，余额不过期；支付宝 / 微信 / 银行卡（Stripe）均可充值，可小额起充、可开票<br>• 定价口径：官方美元价按 ¥1 = $1 折算后再乘分组倍率，输入 / 输出 / 缓存写入 / 缓存读取四列分别计量<br>• Claude-Max（主推）0.8 倍：Sonnet 5 ¥1.6 / ¥8、Opus 5 ¥4 / ¥20、Fable 5 ¥8 / ¥40（每百万 token 输入/输出）<br>• Claude Code（AWS，官方渠道）3.8 倍：Sonnet 5 约 ¥7.6 / ¥38、Opus 5 约 ¥19 / ¥95<br>• 缓存读取 0.1× 输入价、缓存写入 1.25×、1 小时缓存写入 2× | • 41 个分组全部明码标价，渠道来源写在分组名里：Claude-Max 为 Claude Max 订阅号池、Claude-Plus 为 Kiro 渠道（非官方直连）、Claude Code（AWS）为 AWS 官方渠道，另有明确标注为「蒸馏」的降智分组——想用正版请选 AWS 组<br>• Claude 覆盖 14 个型号（19 个模型 ID，含日期后缀别名）：Fable 5 / 5.1、Opus 4.5 / 4.6 / 4.7 / 4.8 / 5 / 5.5、Sonnet 4.5 / 4.6 / 5 / 5.5、Haiku 4.5 / 5.5<br>• 三协议兼容：Anthropic `/v1/messages`、OpenAI 兼容、Gemini 原生，官方提供 Claude Code / Codex / CC Switch / Gemini CLI 教程，另有不走 CDN 的直连线路 `dc.apikl.ai`<br>• 第三方独立实测（Veridrop，2026-07 至 10 共 149 次）中位 95/100 判「优秀」，149 次无全站严重问题；但 OpenAI 侧 token 计费口径通过率仅 34%、Claude thinking signature 72.4%，成本敏感或强真伪要求场景需自测<br>• 2026-06 上线、域名 2026-07 注册；邮箱 + QQ + 微信 + Telegram 多渠道客服，退款规则与发票政策公开可查 | `多分组明码标价` `双协议兼容` `Claude Code支持` `第三方实测` `人民币充值` `官方渠道可选` `新站` |
| [AnyAIGC](https://anyaigc.ai/)<br><sub>anyaigc.ai<br>月访问量: 暂无第三方估算数据</sub> | • 按量付费，无订阅；定价接口 `/api/pricing` 公开可查（无需登录），333 个模型含 16 个 Claude 型号，各分组倍率全部列出<br>• Claude 现价（每百万 token 输入/输出，以[模型广场](https://anyaigc.ai/pricing)为准）：Claude-Code-1 组约 2.4 折——Sonnet 5.5 $0.476 / $2.38、Opus 5.5 $0.953 / $4.76、Fable 5.1 $2.38 / $11.9；Kiro-Claude-1 组约 1.2 折——Sonnet 5.5 $0.238 / $1.19<br>• 分组价差极大，选错反而吃亏：AWS-Bedrock-1 约 6 折、AWS-Bedrock-2 约 8 折，而 Anthropic-Claude-1 与 AWS-Claude-3 为 1.49 倍（比官方贵 49%）<br>• 缓存读取 0.05×（Sonnet / Opus）、0.025×（Fable）、0.1×（Haiku），缓存写入 5m 1.25×、1h 2×<br>• 微信、支付宝（两路）、信用卡均可充值，$1 起充，人民币按 6.718 汇率结算，可开票<br>• 无免费额度（签到关闭、无注册赠送），仅邀请返利 5% | • Claude 覆盖 16 个型号：Opus 5.5 / 5 / 4.8 / 4.7 / 4.6 / 4.5 / 4.1 / 4、Sonnet 5.5 / 5 / 4.6 / 4.5、Fable 5.1 / 5、Haiku 5.5 / 4.5<br>• 上游渠道写在分组名里：AWS Bedrock、AWS Claude、Anthropic、Azure、Vertex、Claude-Code、Kiro，均为官方或订阅渠道，未见「逆向 / 反代」分组<br>• Anthropic `/v1/messages` 与 OpenAI `/v1/chat/completions` 双协议，改 base_url 即可用；有 uptime 状态页与接入文档<br>• 品牌自 2026-04-22 连续运营：老站 anyaigc.com 于 2026-08-09 停止注册、2026-09-10 停止充值，官方公告引导用户迁至 anyaigc.ai，迁移原因为系统升级为美元计价体系（新站全部以美元标价，人民币按 6.718 汇率结算）<br>• 运营活跃：394 条站内公告（最近 2026-10-22），claude-opus-5-5 累计用量 224 亿 token<br>• 待核实项：运营主体未公开（whois 全隐私隐藏），暂无第三方实测评分（Veridrop 仅收录未出快照），成本敏感场景建议先小额实测 | `双协议兼容` `Claude全系列` `分组明码标价` `缓存计费` `微信支付宝` `1美元起充` `可开票` |

## 🛠️ 检测工具 <a id="tools"></a>

| 工具名称 | 功能说明 | 特点 |
|---------|----------|------|
| [CCTest](https://cctest.ai/zh)<br><sub>cctest.ai/zh<br>月访问量: 42.6K (2026-08) → 36.5K (2026-09) ▼跌 14.5%</sub> | 业界专业的Claude API检测平台，可检测模型真实性和Token消费合理性，被数十家头部中转服务商信赖 | • 黑盒检测模式，不会存储用户API Key，安全可靠<br>• 支持Claude Sonnet 4.6、Opus 4.6、Opus 4.7等主流版本<br>• 11轮专业测试，可检测Token使用倍率是否异常、消费是否合理<br>• 测试成本透明，单次检测预计消耗约$0.3 |
| [Ofox模型验真](https://ofox.ai/verify/)<br><sub>ofox.ai/verify<br>月访问量: 221.1K (2026-08) → 212.7K (2026-09) ▼跌 3.8%</sub> | Ofox旗下模型验真工具，输入API接口15秒验证中转站模型是否真实 | • 研究显示45.83%的中转站存在模型替换<br>• 输入API接口，15秒验明模型真身<br>• 由OfoxAI团队提供，香港直连线路 |
| [LLM大模型照妖镜](https://llmtest.cn/)<br><sub>llmtest.cn<br>月访问量: 834 (2026-08) → 3.4K (2026-09) ▲涨 310.1%</sub> | 从多个技术维度一键检测API中转站的Claude Opus/Sonnet/GPT/Gemini等高级模型是否真实，拒绝套壳骗局 | • 基于GitHub开源项目创建，纯前端处理逻辑<br>• 零日志隐私承诺，API Key测完即焚，服务器不留存<br>• 多维交叉验证：返回协议、响应结构、知识问答、身份一致性、思维链痕迹、签名指纹<br>• 真实率评分：80%+高可信 / 50-79%存疑 / 50%以下高风险<br>• 国内可直连，无需科学上网 |
| [awesome-claude-code-codex-relay](https://github.com/zhaoshengxiong/awesome-claude-code-codex-relay)<br><sub>github.com/zhaoshengxiong<br>月访问量: —（GitHub 仓库）</sub> | Claude Code / Codex 中转站导航，GitHub Actions 每 6 小时探测各家 API 端点可用性，原始数据公开在仓库内 | • 20 家中转站，每条标来源与核实日期<br>• 探测项：网关应答、端点有效、TTFB P50/P95<br>• 不打星、不排名、不比价<br>• 由 TeamoRouter 团队维护，README 开头有利益声明 |

## 🤝 贡献指南 <a id="contributing"></a>

欢迎提交PR补充更多优质的Claude中转API资源，提交时请确保：

1. 提供的信息真实准确，来自官方渠道
2. 包含官网链接、费用结构和客观评价，以及**月访问量**等数据
3. 服务确实提供Claude API中转能力
4. 不包含任何广告或推广性质的不实描述

提交前请先检查是否已有相同的服务商收录，避免重复提交。

## ⚠️ 免责声明 <a id="disclaimer"></a>

本项目仅做资源收集和整理，不对任何第三方服务的质量、安全性、可用性做任何担保。使用第三方服务时请自行承担风险，本项目维护者不承担任何使用相关的责任。

---

⭐ 如果这个项目对你有帮助，欢迎Star支持！

## ⭐ Star 历史

[![Star History Chart](https://api.star-history.com/svg?repos=peter123023/awesome-claude-api&type=Date)](https://star-history.com/#peter123023/awesome-claude-api&Date)