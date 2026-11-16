# 录取、身份线索与 X 推荐：证据台账

> 更新：下文“北外投档26→3”及“不估计广东IP人群”的课堂方案已撤下。现行升学Sankey及基于广东上网人口的估算，见 `gd-identity-estimation.md`。X证据部分继续使用。旧取证记录保留以便追溯，不作为当前课堂方案。

核验日期：2026-10-29。先查 `HANDOFF.md`、`edu-flows.csv`、`gd-sankey.html`、`teasers.md`、`trial-lesson-options.md`，再核原件。本文记录本次核验，不继承旧笔记的“✅”。

## 录取与身份

| 证据 | 等级与本次核验 | 可支持 / 不可支持 |
|---|---|---|
| [广东省政府，2025-06-27](https://www.gd.gov.cn/gdywdt/bmdt/content/post_4734513.html) | 二手已核验：正文注明来源南方日报网络版，L19–21 | 广东2025普通类历史考生292200、物理440208；本科线上历史91654、物理276586。是考生成绩分布，不是录取、在读或广东IP用户分布。 |
| [考试院2025本科普通类历史投档表](https://eea.gd.gov.cn/attachment/0/585/585885/4746781.pdf#page=1) | 一手已核验：PDF第1页表头及北外三行的提取文本；截图工具未返回可见图像，未完成图像复核 | 院校10030、专业组211/212/213，投档人数21/3/2；按院校代码加总26为推导。范围仅此表所列批次/选科/年度，含中外合作组213，不含提前批和其他通道；投档非最终录取。组代码211不是211工程标签；表没有专业名称和在读状态。 |
| [教育部211名单](https://www.moe.gov.cn/srcsite/A22/s7065/200512/t20051223_82762.html) | 一手材料，检索索引读到名单，正文请求超时，待正文核验 | 索引列出北京外国语大学等；页面不把完整名单或人数当作本次已核验事实使用。 |
| [教育部985名单](https://www.moe.gov.cn/srcsite/A22/s7065/200612/t20061206_128833.html) | 一手材料，检索索引可读，正文超时，待正文核验 | 标签依据学校名单；不据此制造广东985/211招生总数。 |
| [省考试院2018答疑，阳光高考转载](https://gaokao.chsi.com.cn/gkxx/zc/ss/201807/20180720/1708203502.html) | 发布方署名省考试院；检索索引可读，正文仅返回空壳；待正文核验 | 索引称2018年一二本合并；页面将该历史细节放备注并标待核，主画面只解释批次/学校标签/网络位置三类口径。 |
| [微博客服IP属地说明](https://kefu.weibo.com/faqdetail?id=21586) | 一手已核验：规则、漫游和编辑说明，更新2026-06-10 | 属地根据访问运营商服务的IP解析，国内显示省级；不等于户籍、生源或校园位置。只支持微博规则，不泛化所有平台。 |

### 可以算与不能算

- 北外在本表的投档数：21+3+2=26；限定该表、院校代码10030、组212后，投档数3。没有个体名单，不能把这个数称为某真实发帖者的候选人数或猜中概率。
- “广东IP ∩ 211在读 ∩ 某专业”需要同一时点、同一总体的交叉计数及线索真实性；目前没有。省人口、录取比例、专业比例不可机械相乘。
- 对话场景仅为课堂问题；未编造人数或行为概率。没有检索、展示真实求助者或个人名册。

## X 源代码

官方仓库 `xai-org/x-algorithm`；本次下载并逐行读取的固定提交：`5ed796374ea48ee26058aab66ab10c266bea2bef`。下列均为一手已核验的代码，证明该提交的实现，不保证生产开关、覆盖率、留存期或实际效果。

链接基址：<https://github.com/xai-org/x-algorithm/tree/5ed796374ea48ee26058aab66ab10c266bea2bef>。

| 环节 | 文件、位置 | 证据边界 |
|---|---|---|
| 动作枚举 | `phoenix/crates/serving/xai-recsys-proto/proto/recsys.proto` L443–474 | 点赞、取消点赞、回复、转发、停留、不感兴趣、举报等名称。枚举定义不是客户端采集SDK。 |
| 元数据字段 | 同文件 L1374–1400 | dwellTime/clientPlatform/ipAddress/searchQuery/timeZone等；字段存在不代表每次填充、保存或进入模型。dwellTime此处未写单位，不擅加毫秒。 |
| 事件及序列结构 | 同文件 L1519–1577 | ActionInfo含engagementTimeMs和actionName；UserAction含userId/tweetInfo/actionInfo/adInfo；UserActionSequence含userActions和metadata。 |
| 取历史序列 | `home-mixer/query_hydrators/scoring_sequence_query_hydrator.rs` L90–121 | 按user_id调用聚合服务；请求长度、窗口与配置有关，不从接口推测全部采集及留存。 |
| 编码特征 | `phoenix/xrex/models/recsys_model.py` L3768–3780；L1884–1996 | 动作multi-hot转embedding；历史作者、帖子、动作等表示拼接投影；连续动作值按配置加入。 |
| 构造预测请求 | `home-mixer/util/phoenix_request.rs` L290–303 | 候选帖和历史序列装入同一预测请求。 |
| 预测结果 | `home-mixer/scorers/phoenix_scorer.rs` L104–144 | dispatch.predict返回candidate_scores；不凭此生成真实用户概率。 |
| 权重和求和 | `home-mixer/params/param.rs` L396–508；`home-mixer/scorers/value_model.rs` L8–84；`xai-value-model/scoring.rs` L57–139 | probability/continuous预测值乘权重并求和，含条件权重，之后还有offset等；Σ不是完整线上排序。旧模拟器仅选几个头。 |
| 选择 | `home-mixer/selectors/top_k_score_selector.rs` L10–33 | 对最终score排序截取；完整链路另有重排、过滤和混排。 |
| 分发历史写入 | `home-mixer/side_effects/update_served_history_side_effect.rs` L31–77、L145–180 | 开关条件下记录请求、帖子、位置、得分等；已分发不等于用户实际看到。 |
| 存储实现 | `home-mixer/clients/served_history_client.rs` L37–44、L80–84、L154–170 | 序列化ServedHistory，按用户/平台/时间键写入Manhattan；不是全平台行为采集存储说明。 |
| 回读历史 | `home-mixer/query_hydrators/served_history_query_hydrator.rs` L25–79 | 读取分发历史，构建served_ids；是可见的反馈路径。 |

反馈闭环有代码依据：历史行为输入预测、分发历史写入后回读。但“每次互动即时重训”“提高争吵倾向”“心理奖励效果”均未在此核实，不写成事实。

## 尚缺的证据

- 广东全体211/985录取或在读人数，以及省份×学校×专业×年级的同总体交叉表。
- 专业组与专业的对应表、分专业实际录取数和在读数。
- X客户端完整事件采集SDK、端到端填充覆盖率、每个字段的留存期。
- 原有X模拟器的帖子概率是旧版合成样例，未被本次核验为真实数据；继续保留原交互，但页面将明确标示其证据状态，不能由模拟排名推出真实平台效应。
