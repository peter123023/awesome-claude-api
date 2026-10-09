# Awesome Claude API 中转资源汇总

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![GitHub Stars](https://img.shields.io/github/stars/peter123023/awesome-claude-api)
![GitHub License](https://img.shields.io/github/license/peter123023/awesome-claude-api?color=blue)
![Last Updated](https://img.shields.io/badge/last%20updated-2026--09-brightgreen)

精心收集和整理的可靠Claude中转API资源列表，帮助开发者快速找到稳定、高性价比的Claude API服务。所有信息均来自官方网站，确保时效性和准确性。

## 📊 月访问量数据情况（2026-09） <a id="traffic-note"></a>

本期对比 2026-08 与 2026-09 两个月访问量，共覆盖 19 个渠道（已移除停服的 Unity2.Ai，新增收录 LinkAGI、Kunavo 与 TokenDos）。数据来自第三方流量平台估算。

- **头部稳健**：OpenRouter 19.2M → 21.3M（+10.8%），头部格局基本稳定。
- **涨幅偏大**：B.AI +275%、TeamoRouter +175%、AIHubMix +73.6%。
- **普遍回落**：ZenMux -74.6%、AIGoCode -73.7%、LLM 大模型照妖镜 -69.7%、EasyRouter -60.6%、IKunCode -43.6%、YesCode -13.6%、CCTest -6.1%。
- **基本持平**：OfoxAI / Ofox 模型验真 +3.7%；AICoding 9 月归零；CoderPlan、FerryAPI 持续无数据。
- **新收录**：LinkAGI 10.6K → 9.6K（-10.0%）、Kunavo 156 → 4.5K（大幅增长）、TokenDos 4.9K → 3.5K（-29.2%）。三站均为 2026 年新上线，8 月已有访问量。

## 📋 目录

- [访问量数据情况](#traffic-note)

- [项目介绍](#intro)
- [使用说明](#usage)
- [API列表](#api-list)
- [检测工具](#tools)
- [贡献指南](#contributing)
- [免责声明](#disclaimer)

## 🚀 项目介绍 <a id="intro"></a>

本项目致力于收集全球范围内稳定可靠的Claude中转API服务，为开发者提供一个权威、更新及时的资源参考。所有收录的API服务均经过初步筛选，确保具备基本的可用性和稳定性。

## 📝 使用说明 <a id="usage"></a>

1. 所有服务均为第三方提供，使用前请仔细阅读各服务商的官方文档和服务条款
2. 建议先试用免费额度或小额套餐，确认服务符合需求后再进行长期付费
3. 价格和政策可能会有变动，请以服务商官方网站最新信息为准

## 🔌 API列表 <a id="api-list"></a>

| 服务商 | 网站地址 | 费用结构 | 综合评价 | 标签 |
|-------|---------|---------|----------|------|
| OpenRouter<br><sub>月访问量: 19.2M (2026-08) → 21.3M (2026-09) <span style="color:#c0392b">↑+10.8%</span></sub>         | [openrouter.ai](https://openrouter.ai/) | • 无订阅制，按量付费，统一信用点抵扣所有模型费用<br>• 价格公开透明，不同Claude版本定价不同<br>• 新用户注册可获得免费试用额度 | • 全球最大的LLM聚合平台，500万+用户，月处理70T Tokens<br>• 全面支持Claude全系列模型（包含最新Claude Opus 4.7）<br>• 多上游自动故障转移，服务可用性高<br>• 完全兼容OpenAI SDK格式，几乎零代码适配<br>• 支持边缘节点加速、精细数据隐私控制、团队管理等功能 | `全球知名` `全Claude版本支持` `高可靠` `SDK兼容好` |
| AIHubMix<br><sub>月访问量: 163.8K (2026-08) → 284.3K (2026-09) <span style="color:#c0392b">↑+73.6%</span></sub>         | [aihubmix.com](https://aihubmix.com/) | • 按量付费无强制订阅，价格与官方基本同步<br>• 新用户及合作伙伴可享10%长期折扣<br>• 账单透明可查，支持多种支付方式 | • 全球主流LLM聚合平台，全面支持Claude全系列模型（含最新Opus 4.7、Sonnet 4.6）<br>• 月处理超千亿Tokens，海量企业开发者使用，服务稳定性极高<br>• 边缘节点自动路由，全球访问速度快，并发支持强<br>• 完全兼容OpenAI、Anthropic官方API协议，零代码适配<br>• 支持联网搜索、多模态、视频生成等高级特性，模型更新速度极快 | `多模型支持` `高稳定` `低延迟` `SDK兼容好` `模型更新快` |
| ZenMux<br><sub>月访问量: 1.5M (2026-08) → 380.9K (2026-09) <span style="color:#27ae60">↓-74.6%</span></sub>         | [zenmux.ai](https://zenmux.ai/) | • 支持按量付费（PAYG）和订阅套餐两种模式<br>• 完全兼容OpenAI、Anthropic官方协议，无额外适配成本<br>• 公开透明计费，详细消耗可查，无隐藏费用<br>• 创新AI异常补偿机制，输出不理想自动赔付 | • 全球顶级模型聚合平台，仅提供官方/授权渠道的原版模型，无降配/残次<br>• 多提供商自动故障切换，Cloudflare全球边缘加速，服务稳定性极高<br>• 内置模型智能路由，自动匹配性价比最高的模型<br>• 多维度消费统计看板，方便成本优化<br>• 全球大量企业和开发者使用，支持个人/团队/企业级需求 | `国际知名` `高稳定` `多模型支持` `异常赔付` `企业级` |
| IKunCode<br><sub>月访问量: 123.0K (2026-08) → 69.3K (2026-09) <span style="color:#27ae60">↓-43.6%</span></sub>         | [api.ikuncode.cc](https://api.ikuncode.cc/) | • 价格信息请访问官方模型广场页面查看<br>• 支持多种模型计费方式 | • 提供完善的API文档支持<br>• 控制台功能齐全，使用管理方便<br>• 适合有一定技术基础的开发者使用 | `文档完善` `易管理` |
| AIGoCode<br><sub>月访问量: 61.9K (2026-08) → 16.3K (2026-09) <span style="color:#27ae60">↓-73.7%</span></sub>         | [aigocode.com](https://www.aigocode.com/) | • 订阅套餐：<br>&nbsp;&nbsp;- Standard：¥399/4周，周额度$110，9折优惠<br>&nbsp;&nbsp;- Premium：¥899/4周，周额度$260，86折优惠<br>&nbsp;&nbsp;- Professional：¥1799/4周，周额度$530，84折优惠<br>&nbsp;&nbsp;- 企业方案：¥9999/4周，定制化服务<br>• 灵活额度：¥50购$50，永久有效，按量扣费<br>• 优先消耗订阅额度，不足自动切换灵活额度 | • 服务稳定性达99.9%，已处理500万+任务<br>• 支持1v1专属工程师服务，问题响应及时<br>• 提供团队协作功能，支持额度共享和权限管理<br>• 适合个人开发者和企业团队使用<br>• 计费透明，无隐藏费用 | `高可用` `团队协作` `多套餐选择` `客服支持好` |
| YesCode<br><sub>月访问量: 21.1K (2026-08) → 18.2K (2026-09) <span style="color:#27ae60">↓-13.6%</span></sub>         | [co.yes.vg](https://co.yes.vg/) | • 免费额度：每月1M tokens<br>• 付费套餐：具体价格见官方定价页面<br>• 统一账单管理，支持多平台计费 | • 性能优异，平均延迟仅38ms<br>• 自动故障转移功能，服务稳定性高<br>• 支持Claude Code、Codex、Gemini等多模型路由<br>• 提供团队密钥管理和实时消费统计<br>• SOC 2 Type II认证，安全性高 | `高稳定` `低延迟` `多模型支持` `团队友好` |
| AICoding<br><sub>月访问量: 2.3K (2026-08) → 0 (2026-09) <span style="color:#27ae60">↓-100.0%</span></sub>         | [aicoding.sh](https://aicoding.sh/) | • 新用户福利：加入社区立得$5免费额度<br>• 具体定价方案可在登录后查看 | • 支持OpenClaw、VSCode等主流IDE无缝集成<br>• 高质量账号池动态调度，智能切换避免封号<br>• 一键安装无需配置，即开即用<br>• 已有10000+团队使用，服务稳定可靠 | `IDE集成友好` `防封号` `易部署` `新用户福利` |
| EasyRouter<br><sub>月访问量: 11.6K (2026-08) → 4.6K (2026-09) <span style="color:#27ae60">↓-60.6%</span></sub>         | [easyrouter.io](https://easyrouter.io/) | • 无订阅制，额度抵扣算力，用多少扣多少<br>• 五月全场Token消耗8.5折，DeepSeek-v4-Pro享2.5折特惠<br>• 多档额度套餐可选：$20/$100/$500/$1500 | • 傅盛团队出品，背景实力雄厚<br>• 统一OpenAI兼容接口，一行代码切换，零迁移成本<br>• 支持40+顶级大模型，全面覆盖Claude全系列模型<br>• 全球多节点部署，智能路由，P99延迟低于200ms<br>• 99.9%可用性SLA保障，自动故障转移与负载均衡 | `全模型支持` `低延迟` `高稳定` `大厂背景` `SDK兼容好` `新用户优惠` |
| B.AI<br><sub>月访问量: 341.3K (2026-08) → 1.3M (2026-09) <span style="color:#c0392b">↑+275.0%</span></sub>         | [b.ai](https://b.ai/) | • 一个 API Key 即可调用 Claude + GPT + Gemini + 国产大模型全系列<br>• 支持区块链地址登录，纯匿名支付（兼容邮箱/Visa/Master/Apple Pay）<br>• 官方 API 直连，零篡改，价格全网最低 | • 孙宇晨（Justin Sun）团队推出的AI模型聚合平台<br>• 官方公告：[孙哥Twitter](https://x.com/justinsuntron/status/2050104947342299208)<br>• BAIClaw 上线"孙哥大脑"功能，支持用孙哥思维交易加密货币 | `新上线` `孙宇晨团队` `全模型支持` `匿名支付` `加密友好` |
| OfoxAI<br><sub>月访问量: 205.0K (2026-08) → 212.7K (2026-09) <span style="color:#c0392b">↑+3.7%</span></sub>         | [ofox.ai](https://ofox.ai/) | • 无订阅制，按量付费，统一信用点抵扣所有模型费用<br>• 价格公开透明，不同模型定价不同<br>• 新用户注册可获得免费试用额度<br>• 支持微信、支付宝、信用卡付款 | • 一个 API Key 调用 100+ 大模型（GPT-5.4、Claude Opus 4.6、Gemini 3.1 等）<br>• 原生支持 OpenAI、Anthropic、Gemini 三种 SDK 协议，零代码适配<br>• 香港直连线路，国内访问延迟 100-300ms，无需代理<br>• 多上游智能路由，99.9% 可用性 SLA<br>• 支持团队协作、共享账单、API 用量管理等功能 | `国内直连` `多模型支持` `低延迟` `SDK兼容好` `团队友好` |
| CoderPlan<br><sub>月访问量: 0 (2026-08) → 0 (2026-09) 持平</sub>         | [coderplan.ai](https://coderplan.ai) | • 按量付费，无月度绑定，充值档位：¥30/¥100/¥300/¥500（大额赠余额）<br>• Claude Opus 4.7 约1.2折（省88%），GPT系列约0.7折（省93%）<br>• 新用户注册赠送免费体验余额<br>• 支持支付宝、微信等国内常用支付方式 | • 支持Claude全系列（Opus 4.7/4.6、Sonnet 4.6），以及GPT、Gemini等主流模型<br>• 深度集成Claude Code、Cursor、Codex CLI、Gemini CLI等AI编程工具<br>• 智能缓存复用机制，显著降低重复调用成本<br>• 透明计费，每次调用详细记录模型、Token、缓存节省及消耗金额<br>• 兼容OpenAI API格式，零代码适配<br>• 提供系统运行状态页，服务稳定性可观测 | `价格优惠` `国内支付` `SDK兼容好` `多模型支持` `缓存省钱` |
| FerryAPI<br><sub>月访问量: 0 (2026-08) → 0 (2026-09) 持平</sub>         | [ferryapi.io](https://www.ferryapi.io/) | • 预付费 USD 余额，按实际调用量扣费，无固定月费或订阅<br>• 新用户注册赠送 **$5 体验金**<br>• 邀请首笔付费用户可获 **1:1 同额赠送**<br>• 具体模型定价见[官方定价页](https://www.ferryapi.io/pricing) | • 低成本 OpenAI 兼容型 AI API 网关，一行代码迁移现有 OpenAI SDK 应用<br>• 聚合 9 大模型厂商：Claude、OpenAI、Gemini、DeepSeek、Qwen、Zhipu AI（智谱）、Kimi、MiMo、Doubao（豆包），一个 API Key 全部接入<br>• 提供商账户池机制，多上游自动调度<br>• 适用于客服、翻译、内容生成、摘要、分类和自动化等场景<br>• 官方文档完善：[ferryapi.io/docs](https://www.ferryapi.io/docs) | `Claude支持` `多模型聚合` `低成本` `新用户福利` `邀请返利` |
| TeamoRouter<br><sub>月访问量: 83.9K (2026-08) → 231.1K (2026-09) <span style="color:#c0392b">↑+175.4%</span></sub>         | [teamorouter.com](https://teamorouter.com/zh) | • 官转不降智，浮动费率低至官价 1-2 折（用量越大越省）<br>• 支付宝直充，按量计费，用多少充多少，无需海外银行卡<br>• 失败请求不扣费，起充无门槛 | • 支持 Anthropic（Claude Mythos 5 / Opus 4.8 / Opus 4.7 / Sonnet 4.6）、OpenAI GPT 系列（Codex / Responses 兼容），以及 Gemini、DeepSeek 等主流模型<br>• Prompt Cache 完整透传：cache read 0.1× / write 1.25× 计费，比例与 Anthropic 官方一致，命中率 >99%，对 Claude Code、Codex 等高频长上下文场景成本差距明显<br>• 双协议兼容：Anthropic Messages（Claude Code）+ OpenAI /v1/responses（Codex），一个 API Key 通吃，改 base_url 现有代码即刻运行<br>• 国内直连：无需科学上网，多线路备份稳定不掉线<br>• 客户端一键接入：免手动配 API Key / Base URL / 代理，自动完成 Claude Code / Codex 配置<br>• 文档教程：[teamorouter.com/zh/blogs](https://teamorouter.com/zh/blogs) | `多模型聚合` `双协议兼容` `低至1-2折` `缓存透传` `国内直连` `按量付费` `Claude Code支持` `Codex支持` `一键接入` |
| LinkAGI<br><sub>月访问量: 10.6K (2026-08) → 9.6K (2026-09) <span style="color:#27ae60">↓-10.0%</span></sub>         | [api.linktoagi.com](https://api.linktoagi.com/) | • 人民币按量计费，无订阅制，用多少扣多少<br>• GPT-5.6 三档号池：Luna ¥0.15 / 百万输入 Token（输出约 ¥0.90）、Terra ¥0.375（输出约 ¥2.25）、Sol ¥0.75（输出约 ¥4.50）<br>• 新用户注册赠送 ¥0.2 试用额度<br>• 支持微信、支付宝付款，逐次调用可查 Token 与扣费 | • 为 Codex、Claude Code、Gemini CLI 与 OpenAI-compatible 客户端提供统一 API 接入<br>• 支持 OpenAI / Claude / Gemini 三类协议，Claude Code 用根地址、Codex 用 /v1，按客户端自动拼接<br>• 一手 GPT 号池，实时模型广场公开模型名、分组与价格<br>• 逐次调用日志记录模型、Token、响应状态与实际扣费<br>• 提供免费工具：地址诊断器、错误排查中心（401/403/404/429/504）、成本计算器、开源自检脚本<br>• 中文接入文档完善，国内直连，人工支持入口明确 | `人民币计费` `按量付费` `Claude Code支持` `Codex支持` `多协议兼容` `国内直连` `价格透明` |
| Kunavo<br><sub>月访问量: 156 (2026-08) → 4.5K (2026-09) <span style="color:#c0392b">↑+2778.2%</span></sub>         | [kunavo.com/zh](https://kunavo.com/zh) | • 预付钱包模式，$10 起充，无订阅、无月费、余额不过期<br>• Claude 价格（每百万 token 输入/输出）：Sonnet 5 $1.40/$7.00、Opus 5.5 $2.80/$14.00、Opus 5 $3.50/$17.50、Fable 5.1 $7.00/$35.00、Sonnet 4.6 $2.10/$10.50、Haiku 4.5 $0.70/$3.50<br>• 充值赠额：充 $100 送 $10、充 $1000 送 $200、充 $5000 送 $1250<br>• Stripe 原生计费：信用卡、Apple Pay、Google Pay、支付宝、微信 Pay，及巴西 Pix、韩国 KakaoPay、印度 UPI 等本地方式 | • OpenAI 兼容网关，聚合 OpenAI、Anthropic、Google 三家前沿模型，35 个在线模型，多数低于官方价、最高省 70%<br>• 改一行 base_url 即可迁移，OpenAI SDK drop-in 替代，streaming / function calling / tool use / vision 全线协议兼容<br>• 自动故障转移：每个请求最多在三条上游通道间依次回退，近期失败的通道在请求发出前即被绕开<br>• 原生流式 SSE pass-through，首字 token 时间与上游官方一致，不缓冲、不批处理<br>• Prompt 缓存命中按 10% 输入价计费（Claude Opus 5.5 为 5%、Fable 5.1 为 2.5%），最高省 90%<br>• 精细化用量：按模型 / API key / IP 维度分析，Webhook 推送，CSV 导出，支持按 key 设月度上限与 IP 白名单<br>• 53 个客户端集成（Claude Code、Cline、OpenClaw、n8n 等），每页对照官方文档核实并注明日期<br>• 透明定价，无隐藏乘数，失败请求不计费；美东 Anycast 边缘接入 | `OpenAI兼容` `多模型聚合` `最高省70%` `自动故障转移` `Prompt缓存` `Stripe计费` `Claude全系列` |
| TokenDos<br><sub>月访问量: 4.9K (2026-08) → 3.5K (2026-09) <span style="color:#27ae60">↓-29.2%</span></sub>         | [tokendos.com/tokendos](https://www.tokendos.com/tokendos) | • 实时按 token 付费，无订阅制<br>• 共享市场定价：聚合提供方闲置 API key，价格显著低于官方直连<br>• Claude Sonnet 5：$0.022 / 百万输入 token、$0.11 / 百万输出 token<br>• Prompt 缓存单独计价：Cache Read $0.0022、Cache Write $0.0275（每百万 token）<br>• GPT-6 Luna 低至 $0.000744 / 百万输入 token、$0.003722 / 百万输出 | • AI API 共享市场模式：连接闲置 API key 的提供方与需求方，把闲置算力变现，同时降低按需调用成本<br>• 双协议端点，可直接替换进现有代码<br>• 模型覆盖 GPT-6 系列（astra / sol / luna）、GPT-5.6（sol / terra）、GPT-5.5、Grok 4.6 / 4.7 及 Claude Sonnet 5<br>• 各模型 Prompt 缓存读 / 写分别计价，长上下文重复读取成本更低<br>• 新站（2026-06 上线），支付方式与团队功能等官方页面暂未公开 | `共享市场` `按量付费` `极低成本` `双协议` `Prompt缓存` `Claude支持` |
| API 快连 (apikl)<br><sub>月访问量: 暂无第三方数据</sub> | [apikl.ai](https://apikl.ai/) | • 人民币按量计费，无订阅制<br>• 逐模型价格公开在[模型广场](https://apikl.ai/model-plaza)，同一模型按分组（渠道来源）分档定价<br>• 支持支付宝、微信付款，控制台逐条显示 Token 与扣费 | • 一个账号统一接入 Claude、GPT、Gemini、Grok、DeepSeek、Kimi、GLM、MiniMax，每把 Key 调用其所在分组的模型<br>• 支持 Anthropic 原生接口（Claude Code 填根地址、不带 /v1）、OpenAI 兼容与 Responses 接口（Codex）<br>• 模型广场按分组公开渠道来源（Anthropic 官方 Key 直连 / Claude Max 订阅号池 / Kiro 渠道等）<br>• 密钥可设额度、过期时间与 IP 白名单；主线路 + 不经 CDN 的直连线路<br>• 中文接入文档：[docs.apikl.ai](https://docs.apikl.ai) | `人民币计费` `按量付费` `Claude Code支持` `Codex支持` `渠道来源公开` `价格透明` |

## 🛠️ 检测工具 <a id="tools"></a>

| 工具名称 | 地址 | 功能说明 | 特点 |
|---------|------|----------|------|
| CCTest<br><sub>月访问量: 38.8K (2026-08) → 36.5K (2026-09) <span style="color:#27ae60">↓-6.1%</span></sub>       | [cctest.ai/zh](https://cctest.ai/zh) | 业界专业的Claude API检测平台，可检测模型真实性和Token消费合理性，被数十家头部中转服务商信赖 | • 黑盒检测模式，不会存储用户API Key，安全可靠<br>• 支持Claude Sonnet 4.6、Opus 4.6、Opus 4.7等主流版本<br>• 11轮专业测试，可检测Token使用倍率是否异常、消费是否合理<br>• 测试成本透明，单次检测预计消耗约$0.3 |
| Ofox模型验真<br><sub>月访问量: 205.0K (2026-08) → 212.7K (2026-09) <span style="color:#c0392b">↑+3.7%</span></sub>      | [ofox.ai/verify](https://ofox.ai/verify/) | Ofox旗下模型验真工具，输入API接口15秒验证中转站模型是否真实 | • 研究显示45.83%的中转站存在模型替换<br>• 输入API接口，15秒验明模型真身<br>• 由OfoxAI团队提供，香港直连线路 |
| LLM大模型照妖镜<br><sub>月访问量: 11.3K (2026-08) → 3.4K (2026-09) <span style="color:#27ae60">↓-69.7%</span></sub>      | [llmtest.cn](https://llmtest.cn/) | 从多个技术维度一键检测API中转站的Claude Opus/Sonnet/GPT/Gemini等高级模型是否真实，拒绝套壳骗局 | • 基于GitHub开源项目创建，纯前端处理逻辑<br>• 零日志隐私承诺，API Key测完即焚，服务器不留存<br>• 多维交叉验证：返回协议、响应结构、知识问答、身份一致性、思维链痕迹、签名指纹<br>• 真实率评分：80%+高可信 / 50-79%存疑 / 50%以下高风险<br>• 国内可直连，无需科学上网 |

## 🤝 贡献指南 <a id="contributing"></a>

欢迎提交PR补充更多优质的Claude中转API资源，提交时请确保：

1. 提供的信息真实准确，来自官方渠道
2. 包含完整的网站地址、费用结构和客观评价，以及**月访问量**等数据
3. 服务确实提供Claude API中转能力
4. 不包含任何广告或推广性质的不实描述

提交前请先检查是否已有相同的服务商收录，避免重复提交。

## ⚠️ 免责声明 <a id="disclaimer"></a>

本项目仅做资源收集和整理，不对任何第三方服务的质量、安全性、可用性做任何担保。使用第三方服务时请自行承担风险，本项目维护者不承担任何使用相关的责任。

---

⭐ 如果这个项目对你有帮助，欢迎Star支持！

## ⭐ Star 历史

[![Star History Chart](https://api.star-history.com/svg?repos=peter123023/awesome-claude-api&type=Date)](https://star-history.com/#peter123023/awesome-claude-api&Date)