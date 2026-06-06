#!/usr/bin/env python3
"""Reddit商机雷达 - 开源版"""
import json, sys, argparse
import urllib.request, urllib.error

def fetch_subreddit(name, limit=25):
    """获取subreddit热门帖子"""
    url = f"https://www.reddit.com/r/{name}/hot.json?limit={limit}"
    req = urllib.request.Request(url, headers={"User-Agent": "OpportunityScanner/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            data = json.load(r)
        posts = []
        for p in data["data"]["children"]:
            d = p["data"]
            posts.append({
                "title": d["title"],
                "selftext": d.get("selftext", "")[:500],
                "score": d["score"],
                "num_comments": d["num_comments"],
                "url": f"https://reddit.com{d['permalink']}",
                "subreddit": d["subreddit"]
            })
        return posts
    except Exception as e:
        print(f"获取失败: {e}", file=sys.stderr)
        return []

# 商机关键词模式
OPPORTUNITY_PATTERNS = [
    ("抱怨/痛点", ["looking for", "need help", "anyone else", "hate", "frustrated", "sucks", "recommend", "alternative to", "any tool", "how do you"]),
    ("愿意付费", ["pay", "buy", "purchase", "subscription", "worth it", "best.*for", "is it worth"]),
    ("求助/需求", ["please help", "how can i", "where can i", "any way to", "does anyone know"]),
    ("商业想法", ["idea", "side hustle", "passive income", "startup", "saas", "business"]),
]

def analyze_opportunity(post):
    """用关键词分析商机信号"""
    text = (post["title"] + " " + post["selftext"]).lower()
    signals = []
    for category, keywords in OPPORTUNITY_PATTERNS:
        matched = [kw for kw in keywords if kw in text]
        if matched:
            signals.append(category)
    return signals

def scan(subreddit, limit=25):
    posts = fetch_subreddit(subreddit, limit)
    if not posts:
        print("❌ 无法获取数据")
        return
    
    opportunities = []
    for post in posts:
        signals = analyze_opportunity(post)
        if signals:
            opportunities.append((post, signals))
    
    print(f"\n{'='*60}")
    print(f"📊 r/{subreddit} 商机扫描报告")
    print(f"{'='*60}")
    print(f"扫描帖子: {len(posts)} | 发现机会: {len(opportunities)}")
    print(f"{'='*60}\n")
    
    for post, signals in sorted(opportunities, key=lambda x: x[0]["score"], reverse=True)[:15]:
        print(f"🔥 [{post['score']}↑ | 💬{post['num_comments']}] {post['title'][:80]}")
        print(f"   信号: {', '.join(signals)}")
        print(f"   链接: {post['url']}")
        print()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Reddit商机雷达")
    parser.add_argument("--subreddit", default="beermoney", help="要扫描的subreddit")
    parser.add_argument("--limit", type=int, default=25, help="帖子数量")
    args = parser.parse_args()
    scan(args.subreddit, args.limit)
