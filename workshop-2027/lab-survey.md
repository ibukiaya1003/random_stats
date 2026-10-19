# 参考实验室调研：完整研究、可用数据与研究方向

> 用途：为「被计数的我们」工作坊寻找可借鉴的研究问题、方法和数据集。
> 访问日期：2026-10-15 / 16。项目、数据与成果的版权和署名归原机构及作者所有。

**分层标准**

- **A 层 · 完整研究**：有公开发表的论文、报告或报道，研究过程（问题、数据、方法）和结论都可查，且与本课主题（数据与身份、代表性不足、算法决策）直接相关。
- **B 层 · 可直接使用的数据库与工具**：公开、可下载或可在线使用。
- **C 层 · 仅有方向**：只有研究方向介绍、项目立项描述或非研究性产出（工具包、行动手册、倡导地图），或者结论没能核实。可以作为灵感，但不宜当作课堂上的证据案例。

**核实状态**

- ✅ 已读论文摘要或报道原文
- 🔎 原文页面无法访问，结论来自搜索到的摘要或二手报道，引用前需核对原文

---

## A 层 · 完整研究（10 项）

### 性别与身份的代表性

#### A1. Diversity of artists in major U.S. museums ✅

- **出处**：Topaz, Klingenberg, Turek, Heggeseth, Harris & Blackwood, *PLOS ONE*, 2019 · [QSIDE Institute](https://qsideinstitute.org/qside-datasets/)
- **问题**：美国大型博物馆馆藏中，艺术家的性别、族裔、地域和年代构成如何？
- **数据**：爬取 18 家美国大型博物馆的公开线上目录
- **方法**：抽样 10,000 条艺术家记录（9,000 多位不同艺术家）交给众包标注，分析 45,000 份回答，推断性别、族裔、地域来源和出生年代
- **结论**：
  - 总体上 85% 的艺术家是白人，87% 是男性
  - 识别出代表性显著偏高或偏低的离群博物馆
  - 博物馆收藏使命与艺术家多样性的关联很弱：想提高多样性的博物馆不必改变其时期或地域侧重
- **与本课的连接**：Day 2–3；数据可以直接用于性别组项目，也能与本期的艺术方向对话
- **链接**：[论文](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0212852) · [数据（QSIDE Datasets → OSF）](https://qsideinstitute.org/qside-datasets/)

#### A2. Race- and gender-based under-representation of creative contributors: art, fashion, film, and music ✅

- **出处**：Topaz, Higdon, Epps-Darling, Siau, Kerkhoff & Mendiratta, *Humanities and Social Sciences Communications*, 2022 · QSIDE
- **问题**：当代艺术、高级时装、票房电影、流行音乐四个领域中，有影响力的创作者的性别与种族/族裔构成如何？交叉身份的情况如何？
- **数据**：四个领域共约 4,700 名创作者；以美国社区调查（ACS）人口构成为基准
- **结论**：
  - 女性占美国人口 51%，但在当代艺术中占 28%，高级时装 45%，票房电影 27%，流行音乐 17%
  - 被边缘化的种族/族裔群体占人口 39%，但在当代艺术、高级时装、票房电影中只占约一半（22%、22%、19%）
  - 黑人音乐人的代表性较高（48%），但作者强调代表性高不等于公平与包容
  - 白人男性在四个领域都被过度代表，是其人口占比的 1.4–2 倍
  - 作者指出：缺乏自我报告的人口数据；ACS 没有无性别、性别不一致、非二元、跨性别等类别，这些群体在基准中被抹去
- **与本课的连接**：Day 2（分类即权力：基准人群本身就有缺失）、Day 3（代表性比值）
- **链接**：[论文](https://www.nature.com/articles/s41599-022-01239-9) · Tableau 可视化：[艺术](https://public.tableau.com/app/profile/institute.for.the.quantitative.study.of.inclusion.diversity.and./viz/QSIDELifeWTRProject-ArtREV/QSIDE-LifeWTRContemporaryArtStory) / [时装](https://public.tableau.com/app/profile/institute.for.the.quantitative.study.of.inclusion.diversity.and./viz/QSIDELifeWTRProject-FashionREV/QSIDE-LifeWTRFashionStory) / [电影](https://public.tableau.com/app/profile/institute.for.the.quantitative.study.of.inclusion.diversity.and./viz/QSIDELifeWTRProject-FilmREV/QSIDE-LifeWTRFilmStory) / [音乐](https://public.tableau.com/app/profile/institute.for.the.quantitative.study.of.inclusion.diversity.and./viz/QSIDELifeWTRProject-MusicREV/QSIDE-LifeWTRMusicStory)

#### A3. Gender Representation on Journal Editorial Boards in the Mathematical Sciences ✅

- **出处**：Topaz & Sen, *PLOS ONE*, 2016 · QSIDE
- **问题**：数学科学期刊编委会中女性占多少？与合理的基准相比如何？
- **数据**：435 本期刊、13,067 个编委席位
- **方法**：自行开发半自动性别推断方法，作者估计准确率为 97.5%；以美国博士授予院校数学系终身轨教职中女性约占 15% 为基准
- **结论**：编委席位中女性占 8.9%，低于 15% 的基准；并识别出显著高于或低于平均水平的期刊、子领域、出版商和国家
- **与本课的连接**：
  - Day 3：最清楚的"样本占比 ÷ 基准占比"范例，基准的选择本身就是论证
  - Day 2：用姓名推断性别的方法是现成的讨论题——准确率 97.5% 时，剩下的 2.5% 是谁？非二元性别的人在哪里？
- **链接**：[论文](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0161357) · [可视化：统计学期刊编委性别构成](https://public.tableau.com/app/profile/institute.for.the.quantitative.study.of.inclusion.diversity.and./viz/GenderMakeupofStatisticsJournalEditors/GenderMakeupofStatisticsJournalEditors)

#### A4. Temporal dynamics of faculty hiring in mathematics ✅

- **出处**：FitzGerald, Huang, Leisman & Topaz, *Humanities and Social Sciences Communications*, 2023 · QSIDE
- **问题**：数学领域博士授予院校的教职招聘网络如何随时间变化？谁能获得教职？
- **数据**：150 所院校、七十年间超过 120,000 条记录
- **方法**：网络分析，用 authority centrality 量化院系声望
- **结论**：
  - 数学博士授予数量与博士授予院校教职数量之间的差距随时间扩大
  - 博士毕业院校声望的对数，与获得教职概率的对数近似线性相关
  - 观察到获得教职的概率随时间下降，且女性低于男性（作者措辞为"关联"，不是因果）
  - 1950–2019 年间，14 个精英院系主导了整个网络
- **与本课的连接**：Day 3（相关与因果的措辞）；网络数据类型的示例
- **链接**：[论文](https://www.nature.com/articles/s41599-023-01708-9)

### 算法与决策

#### A5. Algorithms in Judges' Hands: Incarceration and Inequity in Broward County, Florida 🔎

- **出处**：Topaz 等，*UCLA Law Review* · QSIDE
- **问题**：COMPAS 风险评估算法上线后，法官的监禁决定发生了什么变化？
- **数据**：佛罗里达州 Broward County 在 COMPAS 上线前后超过 1 万条法院记录
- **方法**：前后比较；有向无环图（DAG）建模
- **结论**（据摘要与二手报道）：
  - 被评为低风险的人，比上线前可比的人更少被监禁；高风险的人更多被监禁
  - 总体监禁率下降，但不同种族之间的监禁差距扩大
- **与本课的连接**：Day 4。阈值改变了谁被关押：总体期望值改善了，代价却分配得更不均
- **链接**：[论文](https://www.uclalawreview.org/algorithms-in-judges-hands-incarceration-and-inequity-in-broward-county-florida/)

#### A6. A large-scale analysis of racial disparities in police stops across the United States ✅

- **出处**：Pierson, Simoiu, Overgoor, Corbett-Davies, Jenson, Shoemaker 等，*Nature Human Behaviour*, 2020 · [Stanford Open Policing Project](https://openpolicing.stanford.edu/)（Stanford Computational Journalism Lab 参与）
- **问题**：美国警察的拦停和搜查决定是否存在种族偏见？
- **数据**：全美近 1 亿次交通拦停记录
- **方法**：
  - **夜幕检验**（veil of darkness）：比较天黑前后黑人司机在被拦停者中的比例
  - **阈值检验**（threshold test）：根据搜查率和搜出违禁品的比率，推断不同群体被搜查的门槛
  - 大麻合法化作为政策变化的前后比较
- **结论**：
  - 日落后黑人司机被拦停的可能性降低，说明拦停决定存在偏见
  - 搜查黑人和拉丁裔司机的门槛低于白人司机
  - 大麻合法化后三个群体被搜查的次数都减少了，但针对黑人和拉丁裔的门槛仍然更低
- **与本课的连接**：Day 4。两种检验都是零代码学员也能理解的识别思路；阈值检验与决策阈值直接对应
- **链接**：[论文](https://www.nature.com/articles/s41562-020-0858-1) · [数据与教程](https://openpolicing.stanford.edu/)

#### A7. What's "Up Next"? Investigating Algorithmic Recommendations on YouTube Across Issues and Over Time ✅

- **出处**：Matamoros-Fernández, Gray, Bartolo, Burgess & Suzor, *Media and Communication*, 2021（开放获取；Joanne Gray 为 [Sydney CSS Lab](https://computational-social-science.sydney.edu.au/research/) 成员）
- **问题**：YouTube"接下来播放"功能放大了什么类型的内容？平台声称的改进是否可以被观察到？
- **数据**：以 "coronavirus"、"feminism"、"beauty" 三个关键词为起点，连续 6 周抓取搜索结果中排名靠前的视频及其元数据，并沿推荐链抓取三层推荐
- **方法**："平台可观察性"（platform observability）框架，计算方法与质性分析结合
- **结论**：
  - 有证据表明 YouTube 在提升"权威"媒体
  - 误导性和争议性内容仍然会被推荐
  - 视频层面随时间呈现多样性，但频道层面有明显的"赢家"获得曝光加成
  - 这些效应因议题而异
- **与本课的连接**：Day 4；平台算法组可以直接照搬这套审计设计，把对象换成 DeepSeek 或国内平台的公开推荐页面
- **链接**：[论文](https://www.cogitatiopress.com/mediaandcommunication/article/view/4184)

#### A8. Automating Public Services: Learning from Cancelled Systems 🔎

- **出处**：Redden, Brand, Sander & Warne, 2022 · [Data Justice Lab](https://datajusticelab.org/project/automating-public-services-learning-from-cancelled-systems/) 与 Carnegie UK
- **问题**：为什么政府部门会暂停或取消算法和自动化决策系统？
- **数据**：欧洲、澳大利亚、加拿大、新西兰、美国被暂停或取消的系统；欺诈检测、警务、儿童福利领域的深入案例
- **方法**：案头范围研究、文件分析、访谈（✅ 据项目页）
- **结论**（据报告摘要与二手报道）：
  - 共分析 61 个被暂停或取消的系统，约一半与司法和警务有关，也有医疗和移民领域的系统
  - 系统常因社区反对、法律诉讼或调查报道而被叫停
  - 报告主张部署方应证明已评估潜在伤害且系统确实有效，即举证责任倒转
- **与本课的连接**：Day 4 决策科学模块。系统被取消，意味着决策者重新估计了期望收益与期望代价
- **12 个深入案例的逐一拆解**：见 [cancelled-systems-cases.md](cancelled-systems-cases.md)
- **链接**：[报告](https://carnegieuk.org/publication/automating-public-services-learning-from-cancelled-systems/) · [The Conversation 摘要](https://theconversation.com/governments-use-of-automated-decision-making-systems-reflects-systemic-issues-of-injustice-and-inequality-185953)

### 缺失数据与反数据

#### A9. Towards Intersectional Feminist and Participatory ML: A Case Study in Supporting Feminicide Counterdata Collection 🔎

- **出处**：Suresh, Movva, Dogan, Bhargava, Cruxên, Martinez Cuba, Taurino, So & D'Ignazio，FAccT 2022 · [MIT Data + Feminism Lab](https://dataplusfeminism.mit.edu/)，Data Against Feminicide 项目
- **问题**：如何与监测女性被杀害（feminicide）的活动者共同设计数据集和机器学习模型，以支持他们的反数据生产？
- **数据**：新闻报道作为数据源（与 MediaCloud 合作）；**实验室本身不收集或汇总数据**（✅ 据实验室项目说明）
- **方法**：
  - 迭代的数据收集和标注，针对模型弱点，并质询"女性被杀害"这一概念的框定，包括谁被计数
  - 按交叉身份而非统计多数来建模
  - 定量、质性和参与式结合的多步骤评估
- **结论**：这篇的结论偏反思性，不是定量发现。作者讨论了机器学习如何挑战权力、拥抱多元，也指出任何技术方案在面对持久的结构性不平等时都有内在局限
- **与本课的连接**：Day 3。"官方数据缺席 → 社群生产反数据"的核心案例，过程最完整
- **链接**：[论文（MIT DSpace）](https://dspace.mit.edu/handle/1721.1/146385) · [Counting Feminicide: Data Feminism in Action（MIT Press 开放阅读）](https://mitpressonpubpub.mitpress.mit.edu/counting-feminicide) · [Data Against Feminicide 网站](https://datoscontrafeminicidio.net/en/home-2/) · [News as Data for Activists](https://api-web.dataplusfeminism.mit.edu/uploads/a1df3e3809e843c4a6a0d86e5b579889.pdf)

### 数据新闻成品

#### A10. UMass Gender Pay Gap: Top paid men making nearly 30 percent more than female colleagues ✅

- **出处**：CBS Boston 与 [Boston University Justice Media co-Lab](https://www.bu.edu/justice-media/) 合作，2022
- **问题**：马萨诸塞大学被提醒存在性别薪酬差距三年后，差距是否改善？
- **数据**：马萨诸塞州政府薪酬数据（非工会员工）
- **方法**：比较各校区收入最高者中的女性人数；同一职位的薪酬比较；采访经济学者
- **结论**：差距不仅没有改善，反而加大；2021 年几乎每个校区收入最高的 10 人中女性都明显少于一半，有两个校区只有 1 名女性
- **与本课的连接**：Day 5；学员几天内可以复刻的题目尺度，也是"数据新闻短篇"的成品范例
- **链接**：[报道](https://www.bu.edu/justice-media/2022/06/07/umass-gender-pay-gap-top-paid-men-making-nearly-30-percent-more-than-female-colleagues/)

---

## B 层 · 可直接使用的数据库与工具

### 数据库

| 名称 | 内容 | 规模 | 获取方式 | 对应 A 层研究 |
|---|---|---|---|---|
| [QSIDE Datasets](https://qsideinstitute.org/qside-datasets/) | 博物馆艺术家多样性、创作领域代表性、数学编委性别、数学教职招聘、COMPAS 前后量刑、Superfund 场地与种族、Opportunity Youth（16–24 岁）等 | 视数据集而定 | OSF 下载；引用格式见各 OSF 仓库 | A1–A5 |
| [JUSTFAIR](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0241381) | 联邦法院量刑决定，关联被告人口特征、罪名、刑期与判案法官 | 2001–2018 年近 60 万条 | 见论文的数据说明 | — |
| [Stanford Open Policing Project](https://openpolicing.stanford.edu/) | 标准化的警察拦停记录 | 超过 2 亿条 | CSV 下载，附分析教程 | A6 |
| [Data Harm Record](https://datajusticelab.org/project/data-harm-record/) | 算法系统已造成伤害的案例汇编，每条附原始来源 | 2017 年首发，2020 年更新 | 网页 | A8 |

### 教学工具与资源

| 名称 | 用途 | 来源 |
|---|---|---|
| [DataBasic.io](http://databasic.io) · [活动库](http://culture.databasic.io) | 零代码数据素养工具和活动，适合 Day 1 | MIT Data + Feminism Lab / Northeastern Data Culture Lab |
| [HCDS Artifacts](https://hcds-uoft.ca/artifacts/) | ADMAPS 算法决策生命周期审计清单；HCDS 教学工具包；BIBED 偏见评估数据集 | Toronto Human-Centered Data Science Lab |
| [Stanford CJ Lab 教程](https://cjlab.stanford.edu/initiatives/) | Search-Script-Scrape、OpenRefine、从 PDF 提取数据 | Stanford Computational Journalism Lab |
| [AFOG 课程](https://afog.berkeley.edu/) | INFO 188 / 239 / 290 课程概述与样本大纲 | UC Berkeley |
| [AI for Social Good 课程仓库](https://github.com/aminrahimian/ai-for-social-good) | 公开课程材料 | Pittsburgh Sociotechnical Systems Research Lab |
| [QSIDE Data4Justice Curriculum](https://qsideinstitute.org/data4justice-curriculum/) | 数据正义课程 | QSIDE |

---

## C 层 · 仅有方向（灵感参考，不作为证据案例）

| 机构 / 项目 | 能看到的内容 | 未列入 A 层的原因 | 仍然可借鉴的点 |
|---|---|---|---|
| **MIT Data + Feminism Lab · Audit the Streets**（[剑桥街名数据集](https://medium.com/data-feminism-lab-mit/whos-in-your-heritage-landscape-ead78981efd6)、[哥伦布 zine](https://counter-columbus.dataplusfeminism.mit.edu/)、[与《华盛顿邮报》合作的可视化](https://wapo.st/3NniYzx)） | 遗产景观审计：街名和纪念物纪念了谁 | 剑桥街名部分找不到完整的方法和结论。剑桥市一份 [2020 年传单](https://www.finditcambridge.org/sites/default/files/registration/2020-07/CCSW_SummerSeries2020.pdf)称街名纪念的人中只有 7% 是女性，但未注明来源。哥伦布可视化是完整成品，但主题是殖民历史而非性别 | "街名里的性别"项目原型；zine 作为成果形式 |
| MIT Data + Feminism Lab · 其他项目（Feminist Hackathons、Feminist Smart Cities、Waking Women Healing Institute 共同设计） | 项目描述与部分论文 | 研究阶段或产出为设计、工作坊 | 女性身体相关议题的数据缺失 |
| **Ida B. Wells JUST Data Lab**（[网站](https://www.thejustdatalab.com/) · [CDH 介绍](https://cdh.princeton.edu/engage/undergraduates/just-data-lab/)） | 学生与社区组织合作，产出孕产妇心理健康手册、包容性检测工具包、租户手册、房东类型学信息图 | 产出是工具包和行动手册，不是研究结论 | 学生项目的产出形式；Data Feminism 七项原则的教学落地 |
| **Data Justice Lab · Data Scores as Governance**（[项目页](https://datajusticelab.org/project/data-scores-as-governance/)） | 英国地方政府的"公民评分"；方法为信息公开申请、访谈、工作坊；有报告 | 报告的具体结论未核实 | 信息公开申请作为数据收集方法 |
| **Data Justice Research Centre, Calgary**（[网站](https://datajustice.ca/)） | 三个研究方向：人口数据、数字档案、监控与隐私 | 只有方向描述 | [Population Data](https://datajustice.ca/2026/03/10/population-data/) 的问题陈述可直接用作 Day 2 的导引问题 |
| **Human-Centered Data Science Lab, Toronto**（[Research](https://hcds-uoft.ca/research/)） | 儿童福利风险模型（CHI 2023 最佳论文）、加拿大 AI 登记册（FAccT 2026）、糖尿病风险模型公平性 | 论文存在，但摘要未核实；与"身份"主题的关联较间接 | ADMAPS 审计清单（见 B 层） |
| **AFOG, UC Berkeley**（[Projects](https://afog.berkeley.edu/programs/projects)） | 2018–2021 学生项目：定向减肥广告的情感伤害、平台市场的算法公平、无家可归者服务匹配系统、招聘中的情绪识别等 | 大多是立项描述，看不到成果 | 平台算法组的选题灵感；[Burrell & Fourcade, "The Society of Algorithms"](https://www.annualreviews.org/doi/abs/10.1146/annurev-soc-090820-020800) 可作阅读材料 |
| **UCLA DataX**（[Data Justice & Data in Society](https://datax.ucla.edu/data-and-justice)） | Safiya Noble 主持的 Data Justice 方向；领域关键词 | 机构框架，不是具体研究 | 领域关键词地图 |
| **Sociotechnical Systems Research Lab, Pittsburgh**（[Projects](https://engineering.pitt.edu/subsites/Labs/sociotechnical-systems/projects/)） | 疫苗错误信息、阿片类药物模拟、NIH 数据共享政策后的隐私实践 | 只有项目标题 | 课程材料（见 B 层） |
| **Computational Social Science Lab, Sydney** · AI and Gender Bias in the Asia Pacific（[Research](https://computational-social-science.sydney.edu.au/research/)） | 搜索和广告算法中的性别偏见如何影响女性获得 STEM 教育与职业机会 | 没找到研究成果 | 与平台算法组主题相关，可留意后续发表 |
| **Stanford Computational Journalism Lab**（[网站](https://cjlab.stanford.edu/)，2014–2022） | Big Local News、California Civic Data Coalition 等 | 除 Open Policing（A6）外多为数据基础设施或教学 | 教程（见 B 层） |
| **BU Justice Media co-Lab** 其他报道（[Projects](https://www.bu.edu/justice-media/projects/)） | 红线区与高温、电动车充电桩分布、PPP 贷款、警务逮捕数据等 | 已完成的报道，但未逐篇核实方法与数据来源 | 选题尺度参照；"红线区与高温"适合地理数据组 |
| **PIT-UN @ Penn**（[页面](https://snfpaideia.upenn.edu/initiatives/public-interest-technology-university-network/)） | 公共利益技术大学网络，设在 SNF Paideia Program 下 | 机构网络；页面为动态加载，信息来自 [Penn Today](https://penntoday.upenn.edu/news/penn-joins-public-interest-technology-university-network) | 公共利益技术的定义（见 [AFOG](https://afog.berkeley.edu/programs/public-interest-tech)） |
| **TILT, Tilburg** · Global Data Justice（[项目页](https://research.tilburguniversity.edu/en/projects/global-data-justice/)） | ERC 项目（2018–2023，Linnet Taylor），跨地区田野调查，构建全球数据治理框架 | 理论框架；TILT 官网对本环境返回 403 | Taylor 的数据正义框架可作 Day 1 或 Day 4 理论补充 |
| **Anti-Eviction Mapping Project**（[网站](https://antievictionmap.com/) · [About](https://antievictionmap.com/about)） | 驱逐地图、Evictorbook 房东网络、地图集、口述史、纪录片、租户问卷 | 行动型批判制图，产出是倡导地图与叙事，不是研究结论 | Day 5 成品形式的最佳参照：量化地图 + 个体叙事 + 公共展示 |

---

## E. BU Social Justice for Data Science 讲座系列：讲者与可用成果

来源：[讲座系列页面](https://www.bu.edu/cds-faculty/research-impact/lectures-seminars/social-justice-data-science/)（Boston University Faculty of Computing & Data Sciences；访问日期 2026-10-17）。下面按"有完整研究或项目 / 只有讲座主题"分层；讲座本身只有摘要，成果是另外检索的。

### 有完整研究或项目，且与本课相关

| 讲者 | 讲座主题 | 可用成果 | 方法 | 对本课的用处 | 核实 |
|---|---|---|---|---|---|
| **Ari Ezra Waldman**（UC Irvine 法学与社会学） | AI 预测与酷儿群体 | "Gender Data in the Automated Administrative State"（*Columbia Law Review*，[文章页](https://www.columbialawreview.org/?p=5408)）：法律要求、官方表格、跨部门数据共享与自动化系统采购共同制造了二元性别数据，抹去跨性别、非二元人群；"Opening the Gender Box"（*Law & Social Inquiry*, 2024，[Cambridge](https://resolve.cambridge.org/core/journals/law-and-social-inquiry/article/opening-the-gender-box-legibility-dilemmas-and-gender-data-collection-on-us-state-government-forms/2B7CDE44851054E01F94CD6BFF5C713D)）：州政府表格的性别选项如何被设计 | 公共记录申请 + 对设计表格的公务员的访谈 | **Day 3 核心案例**；也是"先质性、后量化"的范例 | 🔎 摘要 |
| **Veena Dubal**（UC Irvine 法学） | 平台劳动中数字化工资的迷思与测量 | "On Algorithmic Wage Discrimination"（*Columbia Law Review*, 2023，[PDF](https://columbialawreview.org/wp-content/uploads/2023/11/Dubal-On_Algorithmic_Wage_discrimination.pdf)）：用细粒度数据生成不可预测、个性化的时薪；劳动者把这种薪酬结构描述为赌博和欺骗 | 多年民族志 | Day 1 研究五步法的理论依据；平台算法组 | 🔎 摘要 |
| **Karen Levy**（Cornell 信息科学） | 卡车司机、技术与工作场所监控 | *Data Driven: Truckers, Technology, and the New Workplace Surveillance*（Princeton UP, 2022，[出版社页](https://press.princeton.edu/books/ebook/9780691241012/data-driven-pdf)）：联邦强制安装的电子行车记录仪原意是减少疲劳驾驶，却成为企业监控司机的工具 | 2011 年起的长期民族志 | Day 4：一个以安全为名、结果转为监控的系统；情境完整性的好例子 | 🔎 出版社与书评 |
| **Muhammad H. Zaman**（BU 强迫迁移中心） | 无国籍人群的医疗可及性 | *We Wait for a Miracle: Health Care and the Forcibly Displaced*（Johns Hopkins UP, 2023）：信任、社会网络、医疗体系与东道国法规如何影响难民和无国籍者看病 | 七国案例研究，质性为主 | Day 3：在官方数据中"不存在"的人群 | 🔎 书评 |
| **BU Law 移民权利诊所 × BU Spark!** | Immigration Enforcement Reporter | 一个记录移民执法行动的交互地图和数据库（讲座介绍称 2025 年 5 月马萨诸塞州约有 1,500 人被移民执法部门逮捕） | 社区报告 + 数据库建设 | Day 5：法学与数据科学合作建反数据库的形式参照 | 讲座页面 |

### 只有讲座主题，未找到可直接使用的完整成果

| 讲者 | 讲座主题 | 说明 |
|---|---|---|
| Jessica Simes（BU 社会学，Open Justice Lab） | 监狱条件的数据：拥挤、极端高温、医疗 | 讲座摘要提到一系列项目，但本次检索未找到对应论文；可直接查 Open Justice Lab 网站 |
| Pauline Kim（WashU 法学） | AI 时代的民权保护 | 职场歧视与隐私方面的法学研究，偏理论 |
| Chinmayi Sharma（Fordham 法学） | 政府自动化如何消除异议 | 可与 cancelled-systems-cases 对照阅读 |
| Jessica Eaglin（Cornell 法学） | 量刑算法与种族 | 常被引用的 "Constructing Recidivism Risk" 未能核实出处 |
| Jason Jackson（MIT 政治经济学） | 出租车与 Uber：技术资本主义 | 已出版专著主题为印度外资政策，与本讲座不同 |
| Bennett Capers（Fordham 法学） | 非洲未来主义、警务与正义 | 理论 |
| Chaz Arnett（Maryland 法学） | 校园监控与数据正义 | 理论；与学员年龄段相关，可作阅读 |
| Woodrow Hartzog（BU 法学） | 反对把监控正常化 | 理论；可作 Day 4 隐私阅读 |
| Patricia Williams（Northeastern 法学与人文） | 数据化人格与分裂的自我 | 理论；与"数据与身份"主线呼应 |
| Chuncheng Liu（Northeastern 传播学与社会学） | 中国社会信用体系与量化政治 | 基于十个月民族志的专著。**议题在中国语境下较敏感，是否引用请与组委确认** |

---

## F. 语言模型中的偏见：从词向量到大模型

> 用于 Day 4 理论与平台算法组的大模型审计项目。✅ 已读摘要；🔎 依据二手资料；"经典"表示本次未重新核对原文。

### 经典起点

| 研究 | 发现 | 核实 |
|---|---|---|
| Bolukbasi, Chang, Zou, Saligrama & Kalai (2016), "Man is to Computer Programmer as Woman is to Homemaker? Debiasing Word Embeddings", NeurIPS | 在 Google News 语料训练的 word2vec 词向量中，类比关系复现了职业性别刻板印象；提出把"性别方向"从词向量中去除的方法 | 经典 |
| Caliskan, Bryson & Narayanan (2017), "Semantics derived automatically from language corpora contain human-like biases", *Science* | 把内隐联想测验改造为词向量版本（WEAT），发现词向量复现了人类心理学实验中测到的多种偏见 | 经典 |
| Gonen & Goldberg (2019), "Lipstick on a Pig" | 去掉"性别方向"后，偏见仍能从词与词的聚类关系中恢复：去偏只是把偏见遮住了 | 经典 |

### 大模型时代：有完整研究过程和结论的研究

| 研究 | 方法 | 发现 | 链接 | 核实 |
|---|---|---|---|---|
| Bai, Wang, Sucholutsky & Griffiths (2025), "Explicitly unbiased large language models still form biased associations", *PNAS* | 仿照内隐联想测验设计"LLM 词语联想测验"；设计"相对决策测验"，让模型在两名候选人之间选择 | 按现有偏见基准，GPT-4 看起来没有偏见；但在 8 个对齐过的模型中，发现涵盖种族、性别、宗教、健康等 21 种刻板印象的隐性偏见。行为数据公开在 GitHub | [论文 PDF](https://cocosci.princeton.edu/papers/bai2025.pdf) · [NeurIPS 2024 版本](https://arxiv.org/html/2402.04105v2) | 🔎 摘要 |
| Hofmann et al. (2024), "AI generates covertly racist decisions about people based on their dialect", *Nature* | 比较模型对"直接提及群体"和"只看到方言文本"两种输入的反应 | 模型对非裔美国人的显性看法较正面，但对非裔美国人英语使用者的隐性判断极为负面：更倾向于分配低声望工作、判有罪、判死刑。人类反馈训练没有消除这种偏见，反而拉大了显性与隐性之间的差距 | [arXiv](https://arxiv.org/abs/2403.00742v1) · [UChicago 新闻](https://news.uchicago.edu/story/ai-biased-against-speakers-african-american-english-study-finds) | 🔎 摘要与报道 |
| Kotek, Dockum & Sun (2023), "Gender bias and stereotypes in Large Language Models", ACM Collective Intelligence | 测试 4 个大模型对职业与性别的判断 | 选择与性别刻板印象一致的职业的可能性约为 3–6 倍；比实际就业统计更偏；模型对自身选择的解释不符合事实 | [arXiv](https://arxiv.org/abs/2308.14921) | 🔎 "3–6 倍"来自二手摘要 |
| Bloomberg (2024), "OpenAI's GPT Is a Recruiter's Dream Tool. Tests Show There's Racial Bias" | 资历相同、名字不同的简历，让 GPT-3.5 按真实职位排序，重复 1,000 次 | 8 个按种族与性别区分的群体中，亚裔女性名字排第一的比例为 17.2%，黑人男性为 7.6%；无偏时每组约 12.5%。有反驳意见质疑分析方法 | [报道](https://prod.cm.bloomberg.com/graphics/2024-openai-gpt-hiring-racial-discrimination/) · [代码](https://github.com/bloomberggraphics/2024-openai-gpt-hiring-racial-discrimination) · [反驳](https://interviewing.io/blog/refuting-bloombergs-analysis-chatgpt-isnt-racist) | 🔎 报道 |

### 可以借用的偏见基准（供讲师了解，课上不必展开）

WinoBias（Zhao et al., 2018）、WinoGender（Rudinger et al., 2018）、StereoSet（Nadeem et al., 2021）、CrowS-Pairs（Nangia et al., 2020）、BBQ（Parrish et al., 2022）；中文：CBBQ。均为本次未重新核对的经典基准。

### 对本课的用处

- **Day 4 理论**：偏见从"显性"转向"隐性"，对齐可能只是把偏见藏起来
- **Day 3 测量效度**：用不同测量方式（直接提问 vs 二选一决策）会得出相反结论，"偏见"怎么定义、怎么测量本身就是问题
- **平台算法组项目**：显性 / 隐性对照审计，设计可直接借用 Bai 与 Hofmann 的思路；Bloomberg 的代码公开，可以作为方法参考

---

## D. 综合：可以迁移到本课的模式

### 研究问题原型（仅引用 A 层）

| 本课方向 | 问题原型 | 依据 |
|---|---|---|
| 性别 / 身份 | 谁被收藏、被署名、坐上编委席位？与基准相比差多少？ | A1、A2、A3 |
| 性别 / 身份 | 基准人群本身是否已经抹去了某些身份？ | A2 |
| 性别 / 身份 | 同岗位的薪酬差距有多大，是否在改善？ | A10 |
| 算法决策 | 引入算法后，总体结果和群体间差距分别怎么变？ | A5 |
| 算法决策 | 决策门槛是否因群体而不同？ | A6 |
| 平台算法 | 推荐系统放大了谁？平台的说法能否被外部观察验证？ | A7 |
| 算法治理 | 系统为什么被取消？谁推动了取消？ | A8 |
| 缺失数据 | 官方数据缺席时，谁在生产反数据，如何生产？ | A9 |

### 方法清单

| 方法 | 例子 | 学员能否借助 coding agent 复刻 |
|---|---|---|
| 公开目录爬取 + 众包或人工标注 | A1、A2 | 能（小规模） |
| 姓名推断性别并报告准确率 | A3 | 能；同时是伦理讨论题 |
| 样本占比 ÷ 基准占比 | A2、A3 | 能 |
| 政策或系统上线前后比较 | A5、A6（大麻合法化） | 能（描述层面） |
| 自然实验式检验（夜幕检验） | A6 | 能理解，可用现成数据演示 |
| 阈值检验 | A6 | 可简化为 Day 4 的阈值游戏 |
| 推荐链抓取与追踪 | A7 | 能（配对提示审计 LLM） |
| 案头范围研究 + 文件分析 | A8 | 能 |
| 新闻即数据 + 参与式标注 | A9 | 能（小规模） |
| 公开薪酬数据分组比较 | A10 | 能 |
