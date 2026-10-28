# 试讲备选材料（待整理）

> 尚未并入 [trial-lesson.md](trial-lesson.md) 的时间线，最后统一整理。

## 一、备选要点一：被记录——什么是数据（10 分钟，可替换 trial-lesson.md 的要点一）

> 状态：讨论中，尚未并入时间线。若采用，三道工序改为"被记录 → 没被记录 → 被用来做决定"，删去分母切换器和改写命题的活动。

### 讲授（5 分钟）

**数据不只是统计表里的数字**

| 类型 | 例子 | 能从中提取什么 |
|---|---|---|
| 数值 / 表格 | 教育统计公报、问卷 | 分布、比例 |
| 行为日志 | 点击、停留、滑走、搜索 | 习惯、兴趣、作息 |
| 文本 | 评论、搜索词、视频标题和字幕、和 AI 的对话 | 话题、情绪、立场、身份线索；可以大规模、自动地提取模式 |
| 图像和声音 | 头像、视频画面、语音 | 地点、外貌、年龄段 |
| 元数据 | IP 地址、设备型号、时区、语言设置、时间戳 | 你在哪、用什么、什么时候 |

**一次假想的抖音访问会留下什么**（虚构用户，不让学员打开自己的账号）

> 晚上 11:40，小周躺在宿舍床上打开抖音，刷了 15 分钟：划过 40 条视频，看完其中 6 条，给 2 条点赞，在 1 条下面评论了一句，搜索了一次"考研 二战"。

| 层次 | 系统记下了什么 | 说明 |
|---|---|---|
| **原始事件**（被观察到的） | IP 地址、设备型号、系统版本、网络类型；打开时间；每条视频的 ID、开始播放和划走的时间戳；点赞的视频 ID；评论文本；搜索词 | 依据讲师从业经验，这类原始事件在内容平台中通常都会被记录；我们看不到抖音的后台系统，具体字段以其现行隐私政策列出的类别为公开佐证（课前核对） |
| **派生指标**（被计算出来的） | 完播率、单条停留时长、本次使用时长、深夜使用频率 | 系统记的是"第几秒开始、第几秒划走"，**完播率是事后算出来的**：算什么、怎么算，是平台的选择 |
| **推断**（被猜出来的） | "备考人群""作息不规律""可能焦虑"之类的兴趣或人群标签 | 小周从没告诉过平台这些，下载个人数据时通常也拿不到（接引子二"你能带走什么"） |

- 理论：Gitelman，没有"原始"的数据：记录什么、怎么切分时间，都是设计出来的；Cheney-Lippold, *We Are Data*：平台给你的"可测量类型"不等于你是谁。
- 学员自己写的那句评论和那次搜索，是**最能暴露身份的数据**：文本里的地名、学校、身份，是大规模提取的对象。

### 佐证：使用 AI 时，服务方能看到什么

Anthropic《威胁情报报告》（2026 年 9 月，[原文](https://www.anthropic.com/threat-intelligence-report-september-2026)）讲的是公司如何发现和封禁滥用其模型的账号。报告为了说明"我们怎样认出这些人"，披露了服务方能看到的信号（✅ 以下引文已对照原文）：

| 数据类型 | 报告中的原话（节选） |
|---|---|
| 设备与语言设置 | "device timezone UTC+8 regardless of the exit node"（换了 VPN 出口，设备时区仍暴露位置）；"prompts in simplified Chinese; zh-CN locale" |
| 使用时间 | "activity during business hours in China" |
| 账号与网络 | "account telemetry"（账号遥测数据）；"operator logins traced to proxies shared with a banned account farm"；"We use metadata and look for signals of irregular activity" |
| 注册与支付方式 | "residential proxies, disposable emails, and virtual-card payments"；"created from a randomly generated email address shortly before use" |
| 账号之间的关联 | "two linked account groups assessed as one actor (high confidence) through shared infrastructure" |
| 对话内容本身 | 伊朗相关案例中，使用者用 VPN 和外国手机号注册，"Nevertheless, in conversation, they repeatedly named their locations, institutions, and roles"：**技术上藏住了，自己在对话里说出来了** |
| 使用量 | "Over a 10-day period in June, we counted 770,609 exchanges" |
| 数据保留 | 报告称识别滥用依赖"the rudimentary observability provided by data retention"；反过来，使用"零数据保留（ZDR）"服务时，内容就看不到了 |

**课上可以说的话**：你在使用 AI 时，服务方至少能看到你的账号、网络、设备设置、使用时间和对话内容；一家公司在公开报告里就列出了这些信号。哪怕你隐藏了 IP，时区、语言和你自己说出的话仍然能认出你。这和 Day 2 的再识别是同一个道理。

**另一个更直接的例子**：报告称，一些模型公司把**自己用户的对话**转发给 Claude 来生成训练数据，"Those sessions contained names, email addresses, company data, and other sensitive data of hundreds of end users"。用户以为只是在和一个编程助手对话，内容却流到了第三家公司。这是 Nissenbaum 情境完整性的现成例子。

**使用时要注意**
1. **语境**：这份报告讲的是追查恶意使用者，不是说公司在逐个监看普通用户。课上要讲的是"能被看到什么"，不是"一定被看了什么"。同一份数据，用于安全审查和用于广告推荐是两种情境（Nissenbaum）。
2. **立场**：报告是一家公司对竞争对手的单方面指控，被点名的公司未必认可。课上说"Anthropic 的报告称"，不说成已证实的事实。
3. **与本课的关系**：报告点名的公司里包括 DeepSeek，而本课正式上课时用的是 DeepSeek API。这正好说明课程规则为什么写着"大模型实验不输入任何真实个人信息"（[course-plan 6.5 节](course-plan.md)），但是否在课上点名具体公司，**需先与组委确认**。
4. 报告涉及伊朗、俄罗斯等国家背景的案例，试讲只引用数据类型，不展开政治内容。

### 活动（4 分钟，聊天区）

- 读出小周的 15 分钟，请学员在聊天区列出"系统可能记下了什么"，越多越好。
- 讲师把答案拖进三栏：**你提供的 / 被观察到的 / 被推断的**。通常学员只想到第一栏，后两栏要讲师补。
- 追问一句："这三栏里，哪一栏你能要求平台给你一份副本？"

### 过渡到要点二（1 分钟）

"小周的一举一动被记到了每一秒。但接下来我们会看到，有些人想被看见，却根本不在数据里。*Data Feminism* 第 4 章讨论的正是这个悖论：**有些人被过度记录，有些人没被计数，而且往往是同一些人：在想被看见的地方看不见，在不想被看见的地方被盯着。**"


## 二、备选：删除与排序——平台的两种权力

> 状态：素材整理，尚未决定放进哪个要点。可接在"被记录"之后，或作为要点二"三种看不见"的一个延伸。

### 一体两面

- **平台必须审核。** 色情、赌博、毒品、诈骗、针对儿童的伤害，不删就会伤人，很多也是法律要求。Gillespie 在 *Custodians of the Internet*（2018）里的核心论点是：审核不是平台的附加功能，**审核就是平台在做的事**。
- **但能删就意味着有权力。** 同一套系统决定了**什么能让你看**（删除、限流、加警示），推荐算法还决定了**你先看什么**（排序、推上首页）。前者让一些内容看不见，后者让另一些内容被放大。
- **规模为什么很难推断**：被删掉的内容不在任何公开数据里。这本身就是一个缺失数据问题，而且是**非随机缺失**：缺的恰恰是平台认为最"有问题"的那部分（接要点二）。研究者只能换着法子去测，每种方法回答的问题不同：

| 方法 | 怎么做 | 能回答什么 | 局限 |
|---|---|---|---|
| 抢在删除前收集、再回头检查 | 发帖后立刻抓取，隔一段时间再看还在不在 | 删除率、删除速度、哪些话题更容易被删 | 看不到"根本没发出去"的内容；样本偏向被追踪的账号 |
| 随机实验 | 自己注册账号，随机发布不同内容，看哪些被删 | 因果：内容本身是否导致删除 | 只能测研究者发的内容；有伦理争议 |
| 配对比较 | 同一个人写的帖子里，比较被删和没被删的 | 哪些词与删除相关，排除个人因素 | 只能找到相关，不能还原规则 |
| 访谈创作者 | 问被限流、被删的人经历了什么、怎么应对 | 审核如何被感知、人们如何自我审查 | 不能估计规模 |

### 高被引的同行评审研究

> 被引次数取自 OpenAlex（2026-10-26 查询），通常低于 Google Scholar，仅用于比较量级。✅ 表示发现已对照摘要；🔎 表示摘要里没有，引用前查正文。

| 研究 | 发表处 | 被引 | 方法 | 主要发现 |
|---|---|---|---|---|
| King, Pan & Roberts (2013), "How Censorship in China Allows Government Criticism but Silences Collective Expression" | *American Political Science Review* | 2,408 | 抢在删除前收集：近 1,400 个社交媒体服务的数百万条帖子，85 个话题 | ✅ 批评政府、领导人和政策的帖子**并不更容易**被删；被删的是有**集体行动**可能的内容，无论立场如何。（常被引用的"约 13% 的帖子被删"🔎 需查正文） |
| King, Pan & Roberts (2014), "Reverse-engineering censorship in China" | *Science* | 421 | 随机实验 + 自建社交网站、购买审查软件、访谈 | ✅ 用实验验证了上一篇的结论；同时**拆解了审查软件本身怎么运作** |
| Roberts (2018), *Censored: Distraction and Diversion Inside China's Great Firewall* | Princeton University Press（专著） | 500 | 综合多项研究 | 🔎 审查不必滴水不漏：增加获取信息的"摩擦"，就足以改变大多数人看到什么 |
| Bamman, O'Connor & Smith (2012), "Censorship and deletion practices in Chinese social media" | *First Monday* | 288 | 抢在删除前收集：5,600 万条微博 | ✅ 抽查的 130 万条中 **16% 以上**被删；含特定敏感词的帖子删除率异常高；删除率**各地不同**，西藏、青海远高于北京 |
| Zhu et al. (2013), "The Velocity of Censorship" | USENIX Security（会议） | 81 | 反复访问账号，精确到分钟 | ✅ 原创帖的删除**近 30% 发生在发帖后 5–30 分钟内**，近 90% 在 24 小时内 |
| Fu, Chan & Chau (2013), "Assessing Censorship on Microblogs in China" | *IEEE Internet Computing* | 234 | 配对比较：1.11 亿条微博 | ✅ 找出区分被删与未删的词，包括网民为绕过审查造的谐音和双关；**实名制**之后，一些人不再写社会和政治话题（寒蝉效应） |
| Gorwa, Binns & Katzenbach (2020), "Algorithmic content moderation" | *Big Data & Society* | 1,091 | 综述 | ✅ 自动审核（哈希匹配、机器学习分类）规模化之后，会**更不透明**、更难处理公平问题，并让言论决定的政治性被"技术"掩盖 |
| Gillespie (2018), *Custodians of the Internet* | Yale University Press（专著） | 1,595 | 平台政策与案例研究 | 审核是平台的核心，平台无法"中立" |
| Gillespie (2020), "Content moderation, AI, and the question of scale" | *Big Data & Society* | 442 | 论述 | ✅ 规模常被用来证明 AI 审核"不可避免"；但即使能自动化，**也不清楚是否应该** |
| Huszár et al. (2022), "Algorithmic amplification of politics on Twitter" | *PNAS* | 65 | 随机实验：近 200 万日活账号被长期分到"按时间排序、无个性化"的对照组 | ✅ 7 国中有 6 国，主流右翼政治人物的推文被算法**放大得更多**；没有发现算法更放大极端派 |

**与抖音直接相关、可备用**（🔎 搜索得到，尚未读原文）
- He & Tian (2023), *International Journal of Communication*：抖音用卡通形象"美楼风"以短视频讲解审核规则，作者认为这提升了"可问责"的形象，但没有真正增加透明度。[ijoc.org](https://ijoc.org/index.php/ijoc/article/download/20974/4322)
- Shen & Haimson (CHI 2025), "The Virtual Jail"：访谈 21 位抖音酷儿创作者和观众，记录他们为避免被删、被限流而采取的策略。适合接 Data Feminism 与"被计错类别"。[Deep Blue](https://deepblue.lib.umich.edu/handle/2027.42/196552)

### 推荐算法怎么算：X 的开源代码

X 在 GitHub 公开了 For You 信息流的代码（[xai-org/x-algorithm](https://github.com/xai-org/x-algorithm)，2026 年 1 月起公开、定期更新；以下依据 2026-10-26 的 main 分支，✅ 已读 README 和参数文件）。

**核心公式**：模型先预测**你**对每条帖子做出各种动作的概率，再加权求和。

```
最终得分 = Σ（权重 × 你做出这个动作的预测概率）
```

**部分权重**（[`home-mixer/params/param.rs`](https://github.com/xai-org/x-algorithm/blob/main/home-mixer/params/param.rs)）

| 动作 | 权重 | | 动作 | 权重 |
|---|---|---|---|---|
| 点赞 | 0.66 | | 不感兴趣 | −52.272 |
| 转发 | 1.0 | | 拉黑作者 | −31.2 |
| 回复 | 5.0（互关时另加 15） | | 屏蔽作者 | −58.8 |
| 引用转发 | 5.0 | | 举报 | −234.0 |
| 私信分享 | 5.0 | | 停留过短 | −0.02 |
| 复制链接分享 | 20.0 | | | |
| 关注作者 | 4.0 | | | |
| 停留 | 0.05 | | | |

**可以讲的几点**
1. **权重乘的是概率，不是次数。** README 特意澄清：不能说"一次举报抵消 468 个赞"。举报的基础概率比点赞低一千多倍，所以权重要大，预测才能影响排序。这是一个读数字时"定义"问题的好例子。
2. **你的行为决定你的概率。** 模型的主要输入是"你最近的互动序列"，也就是备选要点一里小周留下的那些足迹。被记录和被推荐是同一条流水线。
3. **权重是平台选的，而且会改。** 2023 年 Twitter 公开的旧版（[the-algorithm-ml](https://github.com/twitter/the-algorithm-ml/blob/main/projects/home/recap/README.md)，2023-04-05）里，"回复且被作者回应"权重高达 75，举报 −369；README 写明权重会"periodically adjusted ... to optimize for platform metrics"。**优化的是平台指标，不是你的福祉。**
4. **一体两面就写在代码里。** 排序之后还有一层可见性过滤（`visibility-filtering/`），决定一条帖子是显示、删除还是加警示（代码见下一小节）。2026 年 9 月起，透明度工具"Under the Hood"会告诉用户自己的帖子是否因为法律要求而在某国被隐藏。
5. **开源也有边界。** README 承认部分规则（一些 botmaker 规则、Grox 的大模型提示词）没有公开，理由是防止被钻空子。"公开了多少"本身也是平台决定的。

### 可见性过滤：代码原文

> 依据 [xai-org/x-algorithm](https://github.com/xai-org/x-algorithm) commit `6258a15`（2026-10-24），✅ 以下代码均从该版本逐字复制，只删了 `use` 导入和测试。`visibility-filtering/` 整个目录有 145 个文件、约 5.2 万行 Rust，这里只选出**决定"显示、删除还是加警示"的那几段**。

**第一步：每条帖子对每个看的人，只会得到四种答案之一**（README 原图）

```
ALLOW          show the post normally
NOTICE         show the post with a notice attached to it
INTERSTITIAL   show it behind an interstitial the viewer can tap
               through, e.g. for adult or graphic media
DROP           do not show it
```

**第二步：判决的数据结构**（[`visibility-filtering/models/verdict.rs`](https://github.com/xai-org/x-algorithm/blob/6258a1549ef808be88fba83d3b2d58364b587ee0/visibility-filtering/models/verdict.rs)，节选前 30 行）

```rust
pub enum Verdict {
    Withheld(Decided<Withholding>),          // 不给看
    Shown {                                  // 给看，但可能附带三样东西
        notice: Option<Decided<Notice>>,                 // 警示文字
        media: Option<Decided<MediaRestriction>>,        // 图片/视频打码
        engagement: Option<Decided<LimitedEngagement>>,  // 不能转发、回复等
    },
}

pub struct Decided<T> {
    pub value: T,
    pub(crate) id: RuleId,
    pub by: &'static str,                    // 记下是哪条规则做的决定
}

pub enum Withholding {
    Drop(DropReason),                        // 直接消失
    Tombstone(TombstoneReason),              // 留一块"墓碑"：此帖不可见
}

pub enum TombstoneReason {
    Bounced,
    SensitiveViewerAgeVerification,
    UpdateAppIos,
    UpdateAppAndroid,
    LocalRegulations,                        // 因当地法规
}
```

（中文注释是我们加的，原文没有注释。）

**第三步：规则长什么样**（[`visibility-filtering/rules/tweet_rules.rs`](https://github.com/xai-org/x-algorithm/blob/6258a1549ef808be88fba83d3b2d58364b587ee0/visibility-filtering/rules/tweet_rules.rs)）

每条规则只有四个字段：编号、**对谁生效**（`audience`）、**什么条件**（`when`）、**怎么处理**（`action`）。

同一条被标为"辱骂"的帖子，三条规则给出三种结果：

```rust
pub(super) const FOSNR_ABUSE_INSULTS_DROP_UNDESIRABLE: Rule = Rule {
    id: RuleId::FosnrAbuseInsults,
    audience: NonAuthors,
    when: all![TweetHasLabel(SafetyLabelType::FOSNR_ABUSE_INSULTS)],
    action: drop_post(DropAs::PossiblyUndesirable),
};

pub(super) const FOSNR_ABUSE_INSULTS_NON_FOLLOWER_DROP_UNDESIRABLE: Rule = Rule {
    id: RuleId::FosnrAbuseInsultsNonFollower,
    audience: NonFollowers,
    when: all![
        TweetHasLabel(SafetyLabelType::FOSNR_ABUSE_INSULTS),
        ClientHasFosnrRules
    ],
    action: drop_post(DropAs::PossiblyUndesirable),
};

pub(super) const FOSNR_ABUSE_INSULTS_FOLLOWER_SOFT_INTERVENTION_ABUSE: Rule = Rule {
    id: RuleId::FosnrAbuseInsultsFollower,
    audience: NonAuthors,
    when: all![
        TweetHasLabel(SafetyLabelType::FOSNR_ABUSE_INSULTS),
        ViewerFollowsAuthor,
        ClientHasFosnrRules
    ],
    action: soft_intervention(
        SafetyLabelType::FOSNR_ABUSE_INSULTS,
```

（第三条在原文中还有几行参数，此处截断。三条规则同时挂在哪个场景下，由 `rules/levels.rs` 决定。）

同一条帖子，看的人不同，结果也不同：作者自己能看到；关注者看到的是**加了警示**的版本；不关注的人在推荐里**根本看不到**。README 的原话是："Some rules drop a post only when it is a recommendation from an account the viewer does not follow ... The same post is allowed to a follower."

按国家处理的规则：

```rust
pub(super) const NSFW_HIGH_PRECISION_TOMBSTONE_LOCAL_REGULATIONS: Rule = Rule {
    id: RuleId::NsfwHighPrecision,
    audience: NonAuthors,
    when: all![
        TweetHasLabel(SafetyLabelType::NSFW_HIGH_PRECISION),
        RequestCountryIn(CountryList::LocalRegulations)
    ],
    action: tombstone(TombstoneReason::LocalRegulations),
};
```

`CountryList::LocalRegulations` 在 [`visibility-filtering/params.rs`](https://github.com/xai-org/x-algorithm/blob/6258a1549ef808be88fba83d3b2d58364b587ee0/visibility-filtering/params.rs) 里写的是 `&["in"]`，即印度：在印度看，这类帖子显示为"墓碑"；在别的国家，它由上面那条 `drop_post` 规则直接删除。

**第四步：排序之后真正删掉帖子的那一步**（[`home-mixer/filters/vf_filter.rs`](https://github.com/xai-org/x-algorithm/blob/6258a1549ef808be88fba83d3b2d58364b587ee0/home-mixer/filters/vf_filter.rs)）

```rust
pub struct VFFilter;

impl Filter<ScoredPostsQuery, PostCandidate> for VFFilter {
    fn filter(
        &self,
        _query: &ScoredPostsQuery,
        candidates: Vec<PostCandidate>,
    ) -> FilterResult<PostCandidate> {
        let (removed, kept): (Vec<_>, Vec<_>) = candidates
            .into_iter()
            .partition(|c| c.visibility_action.as_ref().is_some_and(should_drop_action));

        FilterResult { kept, removed }
    }
}

pub(crate) fn should_drop_action(action: &Action) -> bool {
    match action {
        Action::Allow | Action::Interstitial | Action::Avoid | Action::Downrank => false,
        Action::Drop(_) | Action::Tombstone | Action::NotEvaluated => true,
    }
}
```

值得指给学员看的一处：**`NotEvaluated`（没来得及评估）也会被删**，而且[`verdict.rs`](https://github.com/xai-org/x-algorithm/blob/6258a1549ef808be88fba83d3b2d58364b587ee0/visibility-filtering/models/verdict.rs) 里查不到数据（`not_found`）或查询失败（`lookup_failed`）时，判决同样是 `Drop`。系统拿不准的时候，默认是"不给看"。这是一个设计选择：宁可错删，不可错放（接 Day 4 的阈值讨论）。

**课堂活动（备选，3 分钟）**：给一条虚构帖子的预测概率（如点赞 10%、回复 2%、举报 0.1%、不感兴趣 3%），学员手算得分；再改一个概率，看排序怎么变。然后问："如果你是平台，你会给'停留时长'多大的权重？为什么抖音这类平台特别在意完播率？"

### 使用时要注意

1. **敏感程度**：中国审查研究涉及政治议题。课程计划里已经把 Citizen Lab 的微信研究列为"需与组委确认"，这批研究同理。可以考虑只讲**研究方法**（怎样测量看不见的东西），并以 X、Twitter 的公开代码和实验为主要例子。
2. **立场**：只讨论数据怎么被生产、怎么被测量，不评价政策（见课程计划开头的讲师声明）。
3. **时效**：King, Pan & Roberts、Bamman、Zhu、Fu 的数据都来自 2011–2013 年的微博，不能直接代表今天的抖音。

## 待核对

- [ ] 抖音现行隐私政策中列出的数据类别，整理成参考答案
- [ ] *Data Feminism* 第 4 章"暴露的悖论"（paradox of exposure）的原文表述
- [ ] 与组委确认：能否在课上引用 Anthropic 报告中点名 DeepSeek 等公司的部分
- [ ] King, Pan & Roberts (2013) 正文中"约 13% 的帖子被删"的说法
- [ ] Roberts (2018) 的"摩擦、恐惧、淹没"框架，对照原书表述
- [ ] He & Tian (2023)、Shen & Haimson (2025) 读原文，确认发表信息
- [ ] X 仓库权重：试讲前重新查看 main 分支（每四周更新，数字可能变）
- [ ] 与组委确认：课上能否讲中国社交媒体审查的研究
