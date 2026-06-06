# 🔍 Reddit 商机雷达

> 自动扫描 Reddit 热帖，用关键词识别真实商业机会。**零 API 依赖，零配置，一条命令出商机报告。**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Stars](https://img.shields.io/github/stars/basakagy/reddit-opportunity-scanner?style=social)](https://github.com/basakagy/reddit-opportunity-scanner)

## 🤔 为什么你需要这个？

每天 Reddit 上有成千上万条帖子在**透露商机**：

- *"Looking for a tool that can..."* → 有人需要一个还不存在的工具
- *"Is it worth paying $50/month for..."* → 有人已经愿意付费
- *"I hate how [product] does..."* → 现有产品有痛点等着被解决
- *"Does anyone know how to..."* → 存在信息差可以填平

这些帖子你不可能每天手动翻几百个 subreddit 去看。**Reddit 商机雷达帮你自动扫描、自动标注。**

## 📊 运行效果

```bash
$ python scanner.py --subreddit beermoney --limit 50

============================================================
📊 r/beermoney 商机扫描报告
============================================================
扫描帖子: 50 | 发现机会: 12
============================================================

🔥 [287↑ | 💬93] Looking for a tool to automate my survey filling
   信号: 抱怨/痛点, 愿意付费
   链接: https://reddit.com/r/beermoney/comments/xxx

🔥 [156↑ | 💬47] Is there any alternative to Prolific that pays via PayPal?
   信号: 抱怨/痛点, 求助/需求
   链接: https://reddit.com/r/beermoney/comments/yyy

🔥 [89↑ | 💬23] I built a simple Chrome extension and made $300 last month
   信号: 商业想法, 愿意付费
   链接: https://reddit.com/r/beermoney/comments/zzz
```

## 🚀 快速开始

```bash
# 1. 克隆
git clone https://github.com/basakagy/reddit-opportunity-scanner.git
cd reddit-opportunity-scanner

# 2. 运行（零依赖，纯标准库）
python scanner.py --subreddit beermoney --limit 50
```

**无需 API Key、无需注册 Reddit App、不需要翻墙**（如果机器能直连 Reddit）。

## 🎯 推荐扫描的 Subreddit

| Subreddit | 适合找什么 |
|-----------|----------|
| `r/beermoney` | 副业需求、小工具付费意愿 |
| `r/SideProject` | 独立开发者产品、验证过的想法 |
| `r/Entrepreneur` | 创业点子、SaaS 需求 |
| `r/SaaS` | SaaS 竞品分析、用户痛点 |
| `r/freelance` | 自由职业需求、报价行情 |
| `r/smallbusiness` | 小企业主痛点（B2B 机会） |
| `r/AskReddit` | 广泛的需求信号 |

## 🔧 参数说明

```
python scanner.py --subreddit <名称> --limit <数量，默认25>
```

## 💰 开源版 vs 付费定制版

| 功能 | 开源版 | 付费定制版 |
|------|:---:|:---:|
| 单 subreddit 扫描 | ✅ | ✅ |
| 关键词商机识别 | ✅ | ✅ |
| **多 subreddit 批量扫描** | ❌ | ✅ |
| **DeepSeek AI 深度分析** | ❌ | ✅ |
| **邮件/飞书/微信日报推送** | ❌ | ✅ |
| **自定义关键词库** | ❌ | ✅ |
| **历史趋势追踪** | ❌ | ✅ |
| **X (Twitter) + Hacker News 多平台** | ❌ | ✅ |

## 📧 付费定制

需要定制版？给我发邮件，注明你的需求：

- **邮箱**: `406866748@qq.com`
- **GitHub Issues**: [点此提交需求](https://github.com/basakagy/reddit-opportunity-scanner/issues)

## ⭐ 支持项目

如果这个工具帮到了你，给个 Star ⭐ 让更多人看到。
