# Awesome Claude API 中转资源汇总

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![GitHub Stars](https://img.shields.io/github/stars/peter123023/awesome-claude-api)
![GitHub License](https://img.shields.io/github/license/peter123023/awesome-claude-api?color=blue)
![Last Updated](https://img.shields.io/badge/last%20updated-2026--05--01-brightgreen)

精心收集和整理的可靠Claude中转API资源列表，帮助开发者快速找到稳定、高性价比的Claude API服务。所有信息均来自官方网站，确保时效性和准确性。

## 📋 目录

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
4. 月访问量数据来自第三方流量统计平台（autotdk.com 与 traffic.cv，数据源为 SimilarWeb 估算），仅供参考，非官方精确统计，实际访问量请以各服务商官方数据为准

## 🔌 API列表 <a id="api-list"></a>

| 服务商 | 网站地址 | 费用结构 | 综合评价 | 标签 |
|-------|---------|---------|----------|------|
| OpenRouter<br>月访问量: 19.2M (2026-07)     | [openrouter.ai](https://openrouter.ai/) | • 无订阅制，按量付费，统一信用点抵扣所有模型费用<br>• 价格公开透明，不同Claude版本定价不同<br>• 新用户注册可获得免费试用额度 | • 全球最大的LLM聚合平台，500万+用户，月处理70T Tokens<br>• 全面支持Claude全系列模型（包含最新Claude Opus 4.7）<br>• 多上游自动故障转移，服务可用性高<br>• 完全兼容OpenAI SDK格式，几乎零代码适配<br>• 支持边缘节点加速、精细数据隐私控制、团队管理等功能 | `全球知名` `全Claude版本支持` `高可靠` `SDK兼容好` |
| AIHubMix<br>月访问量: 163.8K (2026-07)     | [aihubmix.com](https://aihubmix.com/) | • 按量付费无强制订阅，价格与官方基本同步<br>• 新用户及合作伙伴可享10%长期折扣<br>• 账单透明可查，支持多种支付方式 | • 全球主流LLM聚合平台，全面支持Claude全系列模型（含最新Opus 4.7、Sonnet 4.6）<br>• 月处理超千亿Tokens，海量企业开发者使用，服务稳定性极高<br>• 边缘节点自动路由，全球访问速度快，并发支持强<br>• 完全兼容OpenAI、Anthropic官方API协议，零代码适配<br>• 支持联网搜索、多模态、视频生成等高级特性，模型更新速度极快 | `多模型支持` `高稳定` `低延迟` `SDK兼容好` `模型更新快` |
| ZenMux<br>月访问量: 1.5M (2026-07)     | [zenmux.ai](https://zenmux.ai/) | • 支持按量付费（PAYG）和订阅套餐两种模式<br>• 完全兼容OpenAI、Anthropic官方协议，无额外适配成本<br>• 公开透明计费，详细消耗可查，无隐藏费用<br>• 创新AI异常补偿机制，输出不理想自动赔付 | • 全球顶级模型聚合平台，仅提供官方/授权渠道的原版模型，无降配/残次<br>• 多提供商自动故障切换，Cloudflare全球边缘加速，服务稳定性极高<br>• 内置模型智能路由，自动匹配性价比最高的模型<br>• 多维度消费统计看板，方便成本优化<br>• 全球大量企业和开发者使用，支持个人/团队/企业级需求 | `国际知名` `高稳定` `多模型支持` `异常赔付` `企业级` |
| IKunCode<br>月访问量: 123.0K (2026-07)     | [api.ikuncode.cc](https://api.ikuncode.cc/) | • 价格信息请访问官方模型广场页面查看<br>• 支持多种模型计费方式 | • 提供完善的API文档支持<br>• 控制台功能齐全，使用管理方便<br>• 适合有一定技术基础的开发者使用 | `文档完善` `易管理` |
| Unity2.Ai<br>月访问量: 90.2K (2026-07)     | [unity2.ai](https://unity2.ai/) | • 按量计费模式（Pay As You Go）<br>• 支持配额限制设置<br>• 提供团队消费统计功能<br>• 具体定价可在订阅后查看 | • 单API密钥即可调用所有支持的AI模型，无需单独申请<br>• 多上游账号智能路由，自动故障转移，服务可靠性高<br>• 支持Claude、GPT、Gemini等多种主流模型<br>• 提供会话持久化功能<br>• 账单透明，支持团队消费可视化 | `多模型支持` `高可靠` `按量计费` `团队友好` |
| AIGoCode<br>月访问量: 61.9K (2026-07)     | [aigocode.com](https://www.aigocode.com/) | • 订阅套餐：<br>&nbsp;&nbsp;- Standard：¥399/4周，周额度$110，9折优惠<br>&nbsp;&nbsp;- Premium：¥899/4周，周额度$260，86折优惠<br>&nbsp;&nbsp;- Professional：¥1799/4周，周额度$530，84折优惠<br>&nbsp;&nbsp;- 企业方案：¥9999/4周，定制化服务<br>• 灵活额度：¥50购$50，永久有效，按量扣费<br>• 优先消耗订阅额度，不足自动切换灵活额度 | • 服务稳定性达99.9%，已处理500万+任务<br>• 支持1v1专属工程师服务，问题响应及时<br>• 提供团队协作功能，支持额度共享和权限管理<br>• 适合个人开发者和企业团队使用<br>• 计费透明，无隐藏费用 | `高可用` `团队协作` `多套餐选择` `客服支持好` |
| YesCode<br>月访问量: 21.1K (2026-07)     | [co.yes.vg](https://co.yes.vg/) | • 免费额度：每月1M tokens<br>• 付费套餐：具体价格见官方定价页面<br>• 统一账单管理，支持多平台计费 | • 性能优异，平均延迟仅38ms<br>• 自动故障转移功能，服务稳定性高<br>• 支持Claude Code、Codex、Gemini等多模型路由<br>• 提供团队密钥管理和实时消费统计<br>• SOC 2 Type II认证，安全性高 | `高稳定` `低延迟` `多模型支持` `团队友好` |
| AICoding<br>月访问量: 2.3K (2026-07)     | [aicoding.sh](https://aicoding.sh/) | • 新用户福利：加入社区立得$5免费额度<br>• 具体定价方案可在登录后查看 | • 支持OpenClaw、VSCode等主流IDE无缝集成<br>• 高质量账号池动态调度，智能切换避免封号<br>• 一键安装无需配置，即开即用<br>• 已有10000+团队使用，服务稳定可靠 | `IDE集成友好` `防封号` `易部署` `新用户福利` |
| EasyRouter<br>月访问量: 11.6K (2026-07)     | [easyrouter.io](https://easyrouter.io/) | • 无订阅制，额度抵扣算力，用多少扣多少<br>• 五月全场Token消耗8.5折，DeepSeek-v4-Pro享2.5折特惠<br>• 多档额度套餐可选：$20/$100/$500/$1500 | • 傅盛团队出品，背景实力雄厚<br>• 统一OpenAI兼容接口，一行代码切换，零迁移成本<br>• 支持40+顶级大模型，全面覆盖Claude全系列模型<br>• 全球多节点部署，智能路由，P99延迟低于200ms<br>• 99.9%可用性SLA保障，自动故障转移与负载均衡 | `全模型支持` `低延迟` `高稳定` `大厂背景` `SDK兼容好` `新用户优惠` |
| B.AI<br>月访问量: 341.3K (2026-07)     | [b.ai](https://b.ai/) | • 一个 API Key 即可调用 Claude + GPT + Gemini + 国产大模型全系列<br>• 支持区块链地址登录，纯匿名支付（兼容邮箱/Visa/Master/Apple Pay）<br>• 官方 API 直连，零篡改，价格全网最低 | • 孙宇晨（Justin Sun）团队推出的AI模型聚合平台<br>• 官方公告：[孙哥Twitter](https://x.com/justinsuntron/status/2050104947342299208)<br>• BAIClaw 上线"孙哥大脑"功能，支持用孙哥思维交易加密货币 | `新上线` `孙宇晨团队` `全模型支持` `匿名支付` `加密友好` |
| OfoxAI<br>月访问量: 205.0K (2026-07)     | [ofox.ai](https://ofox.ai/) | • 无订阅制，按量付费，统一信用点抵扣所有模型费用<br>• 价格公开透明，不同模型定价不同<br>• 新用户注册可获得免费试用额度<br>• 支持微信、支付宝、信用卡付款 | • 一个 API Key 调用 100+ 大模型（GPT-5.4、Claude Opus 4.6、Gemini 3.1 等）<br>• 原生支持 OpenAI、Anthropic、Gemini 三种 SDK 协议，零代码适配<br>• 香港直连线路，国内访问延迟 100-300ms，无需代理<br>• 多上游智能路由，99.9% 可用性 SLA<br>• 支持团队协作、共享账单、API 用量管理等功能 | `国内直连` `多模型支持` `低延迟` `SDK兼容好` `团队友好` |
| CoderPlan<br>月访问量: 0 (2026-07)     | [coderplan.ai](https://coderplan.ai) | • 按量付费，无月度绑定，充值档位：¥30/¥100/¥300/¥500（大额赠余额）<br>• Claude Opus 4.7 约1.2折（省88%），GPT系列约0.7折（省93%）<br>• 新用户注册赠送免费体验余额<br>• 支持支付宝、微信等国内常用支付方式 | • 支持Claude全系列（Opus 4.7/4.6、Sonnet 4.6），以及GPT、Gemini等主流模型<br>• 深度集成Claude Code、Cursor、Codex CLI、Gemini CLI等AI编程工具<br>• 智能缓存复用机制，显著降低重复调用成本<br>• 透明计费，每次调用详细记录模型、Token、缓存节省及消耗金额<br>• 兼容OpenAI API格式，零代码适配<br>• 提供系统运行状态页，服务稳定性可观测 | `价格优惠` `国内支付` `SDK兼容好` `多模型支持` `缓存省钱` |
| FerryAPI<br>月访问量: 0 (2026-07)     | [ferryapi.io](https://www.ferryapi.io/) | • 预付费 USD 余额，按实际调用量扣费，无固定月费或订阅<br>• 新用户注册赠送 **$5 体验金**<br>• 邀请首笔付费用户可获 **1:1 同额赠送**<br>• 具体模型定价见[官方定价页](https://www.ferryapi.io/pricing) | • 低成本 OpenAI 兼容型 AI API 网关，一行代码迁移现有 OpenAI SDK 应用<br>• 聚合 9 大模型厂商：Claude、OpenAI、Gemini、DeepSeek、Qwen、Zhipu AI（智谱）、Kimi、MiMo、Doubao（豆包），一个 API Key 全部接入<br>• 提供商账户池机制，多上游自动调度<br>• 适用于客服、翻译、内容生成、摘要、分类和自动化等场景<br>• 官方文档完善：[ferryapi.io/docs](https://www.ferryapi.io/docs) | `Claude支持` `多模型聚合` `低成本` `新用户福利` `邀请返利` |
| TeamoRouter<br>月访问量: 83.9K (2026-07)     | [teamorouter.com](https://teamorouter.com/zh) | • 官转不降智，浮动费率低至官价 1-2 折（用量越大越省）<br>• 支付宝直充，按量计费，用多少充多少，无需海外银行卡<br>• 失败请求不扣费，起充无门槛 | • 支持 Anthropic（Claude Mythos 5 / Opus 4.8 / Opus 4.7 / Sonnet 4.6）、OpenAI GPT 系列（Codex / Responses 兼容），以及 Gemini、DeepSeek 等主流模型<br>• Prompt Cache 完整透传：cache read 0.1× / write 1.25× 计费，比例与 Anthropic 官方一致，命中率 >99%，对 Claude Code、Codex 等高频长上下文场景成本差距明显<br>• 双协议兼容：Anthropic Messages（Claude Code）+ OpenAI /v1/responses（Codex），一个 API Key 通吃，改 base_url 现有代码即刻运行<br>• 国内直连：无需科学上网，多线路备份稳定不掉线<br>• 客户端一键接入：免手动配 API Key / Base URL / 代理，自动完成 Claude Code / Codex 配置<br>• 文档教程：[teamorouter.com/zh/blogs](https://teamorouter.com/zh/blogs) | `多模型聚合` `双协议兼容` `低至1-2折` `缓存透传` `国内直连` `按量付费` `Claude Code支持` `Codex支持` `一键接入` |

## 🛠️ 检测工具 <a id="tools"></a>

| 工具名称 | 地址 | 功能说明 | 特点 |
|---------|------|----------|------|
| CCTest<br>月访问量: 38.8K (2026-07)   | [cctest.ai/zh](https://cctest.ai/zh) | 业界专业的Claude API检测平台，可检测模型真实性和Token消费合理性，被数十家头部中转服务商信赖 | • 黑盒检测模式，不会存储用户API Key，安全可靠<br>• 支持Claude Sonnet 4.6、Opus 4.6、Opus 4.7等主流版本<br>• 11轮专业测试，可检测Token使用倍率是否异常、消费是否合理<br>• 测试成本透明，单次检测预计消耗约$0.3 |
| Ofox模型验真<br>月访问量: 205.0K (2026-07)  | [ofox.ai/verify](https://ofox.ai/verify/) | Ofox旗下模型验真工具，输入API接口15秒验证中转站模型是否真实 | • 研究显示45.83%的中转站存在模型替换<br>• 输入API接口，15秒验明模型真身<br>• 由OfoxAI团队提供，香港直连线路 |
| LLM大模型照妖镜<br>月访问量: 11.3K (2026-07)  | [llmtest.cn](https://llmtest.cn/) | 从多个技术维度一键检测API中转站的Claude Opus/Sonnet/GPT/Gemini等高级模型是否真实，拒绝套壳骗局 | • 基于GitHub开源项目创建，纯前端处理逻辑<br>• 零日志隐私承诺，API Key测完即焚，服务器不留存<br>• 多维交叉验证：返回协议、响应结构、知识问答、身份一致性、思维链痕迹、签名指纹<br>• 真实率评分：80%+高可信 / 50-79%存疑 / 50%以下高风险<br>• 国内可直连，无需科学上网 |

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