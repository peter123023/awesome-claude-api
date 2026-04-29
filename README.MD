# Awesome Claude API 中转资源汇总

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![GitHub Stars](https://img.shields.io/github/stars/your-repo/awesome-claude-api)
![GitHub License](https://img.shields.io/github/license/peter123023/awesome-claude-api?color=blue)
![Last Updated](https://img.shields.io/badge/last%20updated-2026--04--29-brightgreen)

精心收集和整理的可靠Claude中转API资源列表，帮助开发者快速找到稳定、高性价比的Claude API服务。所有信息均来自官方网站，确保时效性和准确性。

## 📋 目录

- [项目介绍](#项目介绍)
- [使用说明](#使用说明)
- [API列表](#api列表)
- [检测工具](#检测工具)
- [贡献指南](#贡献指南)
- [免责声明](#免责声明)

## 🚀 项目介绍

本项目致力于收集全球范围内稳定可靠的Claude中转API服务，为开发者提供一个权威、更新及时的资源参考。所有收录的API服务均经过初步筛选，确保具备基本的可用性和稳定性。

## 📝 使用说明

1. 所有服务均为第三方提供，使用前请仔细阅读各服务商的官方文档和服务条款
2. 建议先试用免费额度或小额套餐，确认服务符合需求后再进行长期付费
3. 价格和政策可能会有变动，请以服务商官方网站最新信息为准

## 🔌 API列表

| 服务商 | 网站地址 | 费用结构 | 综合评价 | 标签 |
|--------|----------|----------|----------|------|
| OpenRouter | [https://openrouter.ai/](https://openrouter.ai/) | • 无订阅制，按量付费，统一信用点抵扣所有模型费用<br>• 价格公开透明，不同Claude版本定价不同<br>• 新用户注册可获得免费试用额度 | • 全球最大的LLM聚合平台，500万+用户，月处理70T Tokens<br>• 全面支持Claude全系列模型（包含最新Claude Opus 4.7）<br>• 多上游自动故障转移，服务可用性高<br>• 完全兼容OpenAI SDK格式，几乎零代码适配<br>• 支持边缘节点加速、精细数据隐私控制、团队管理等功能 | `全球知名` `全Claude版本支持` `高可靠` `SDK兼容好` |
| YesCode | [https://co.yes.vg/](https://co.yes.vg/) | • 免费额度：每月1M tokens<br>• 付费套餐：具体价格见官方定价页面<br>• 统一账单管理，支持多平台计费 | • 性能优异，平均延迟仅38ms<br>• 自动故障转移功能，服务稳定性高<br>• 支持Claude Code、Codex、Gemini等多模型路由<br>• 提供团队密钥管理和实时消费统计<br>• SOC 2 Type II认证，安全性高 | `高稳定` `低延迟` `多模型支持` `团队友好` |
| AIGoCode | [https://www.aigocode.com/](https://www.aigocode.com/) | • 订阅套餐：<br>&nbsp;&nbsp;- Standard：¥399/4周，周额度$110，9折优惠<br>&nbsp;&nbsp;- Premium：¥899/4周，周额度$260，86折优惠<br>&nbsp;&nbsp;- Professional：¥1799/4周，周额度$530，84折优惠<br>&nbsp;&nbsp;- 企业方案：¥9999/4周，定制化服务<br>• 灵活额度：¥50购$50，永久有效，按量扣费<br>• 优先消耗订阅额度，不足自动切换灵活额度 | • 服务稳定性达99.9%，已处理500万+任务<br>• 支持1v1专属工程师服务，问题响应及时<br>• 提供团队协作功能，支持额度共享和权限管理<br>• 适合个人开发者和企业团队使用<br>• 计费透明，无隐藏费用 | `高可用` `团队协作` `多套餐选择` `客服支持好` |
| IKunCode | [https://api.ikuncode.cc/](https://api.ikuncode.cc/) | • 价格信息请访问官方模型广场页面查看<br>• 支持多种模型计费方式 | • 提供完善的API文档支持<br>• 控制台功能齐全，使用管理方便<br>• 适合有一定技术基础的开发者使用 | `文档完善` `易管理` |
| Unity2.Ai | [https://unity2.ai/](https://unity2.ai/) | • 按量计费模式（Pay As You Go）<br>• 支持配额限制设置<br>• 提供团队消费统计功能<br>• 具体定价可在订阅后查看 | • 单API密钥即可调用所有支持的AI模型，无需单独申请<br>• 多上游账号智能路由，自动故障转移，服务可靠性高<br>• 支持Claude、GPT、Gemini等多种主流模型<br>• 提供会话持久化功能<br>• 账单透明，支持团队消费可视化 | `多模型支持` `高可靠` `按量计费` `团队友好` |
| AICoding | [https://aicoding.sh/](https://aicoding.sh/) | • 新用户福利：加入社区立得$5免费额度<br>• 具体定价方案可在登录后查看 | • 支持OpenClaw、VSCode等主流IDE无缝集成<br>• 高质量账号池动态调度，智能切换避免封号<br>• 一键安装无需配置，即开即用<br>• 已有10000+团队使用，服务稳定可靠 | `IDE集成友好` `防封号` `易部署` `新用户福利` |

## 🛠️ 检测工具

| 工具名称 | 地址 | 功能说明 | 特点 |
|---------|------|----------|------|
| Claude照妖镜 | [https://iffs.cn/](https://iffs.cn/) | 专门用于检测Claude模型真实性和功能完整性的测试工具，可验证中转API提供的是否为满血官方模型 | • 测试准确率超过99%<br>• 包含7个维度综合测试（智力准确性、知识库、思维链、Base64能力等）<br>• 评分≥70分即为满血模型，≥90分为官方API超级满血珍品<br>• 支持Claude Opus 4.6、4.7等最新版本测试 |
| CCTest | [https://cctest.ai/zh](https://cctest.ai/zh) | 业界专业的Claude API检测平台，可检测模型真实性和Token消费合理性，被数十家头部中转服务商信赖 | • 黑盒检测模式，不会存储用户API Key，安全可靠<br>• 支持Claude Sonnet 4.6、Opus 4.6、Opus 4.7等主流版本<br>• 11轮专业测试，可检测Token使用倍率是否异常、消费是否合理<br>• 测试成本透明，单次检测预计消耗约$0.3 |

## 🤝 贡献指南

欢迎提交PR补充更多优质的Claude中转API资源，提交时请确保：

1. 提供的信息真实准确，来自官方渠道
2. 包含完整的网站地址、费用结构和客观评价
3. 服务确实提供Claude API中转能力
4. 不包含任何广告或推广性质的不实描述

提交前请先检查是否已有相同的服务商收录，避免重复提交。

## ⚠️ 免责声明

本项目仅做资源收集和整理，不对任何第三方服务的质量、安全性、可用性做任何担保。使用第三方服务时请自行承担风险，本项目维护者不承担任何使用相关的责任。

---

⭐ 如果这个项目对你有帮助，欢迎Star支持！