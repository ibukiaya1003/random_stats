# 医疗算法偏差原始研究

## 摘录来源是什么？

### Takeaway
用户摘录来自 Kroll、Smart、Geiger 与 Jacobs 的 HDSR 文章，医疗部分引用 Obermeyer 等人的 2019 年原始研究。

### Cited Findings
- 【一手已核验】Joshua A. Kroll 等，《Unsafe at any AUC: Unlearned Lessons From Sociotechnical Disasters for Responsible AI》，HDSR，2026 年 9 月 1 日，DOI 10.1162/99608f92.91b8834f；§3.1 包含用户所给医疗段落。[HDSR 原文](https://hdsr.mitpress.mit.edu/pub/tarzjxgu/release/2)
- 【一手已核验】Ziad Obermeyer、Brian Powers、Christine Vogeli、Sendhil Mullainathan，《Dissecting racial bias in an algorithm used to manage the health of populations》，Science 366(6464), 447–453，2019，DOI 10.1126/science.aax2342。[原论文全文（FTC 镜像 PDF）](https://www.ftc.gov/system/files/documents/public_events/1548288/privacycon-2020-ziad_obermeyer.pdf)；[PubMed 文献信息](https://pubmed.ncbi.nlm.nih.gov/31649194/)

### Inferences
- 两篇文章分别是社会技术安全的论证与被引用的实证研究，不能把前者对开发者认知的归因直接当作后者直接观测到的事实。

### Gaps
- 原文中“开发者曾明确关心偏差却未意识到代理变量风险”的思想与动机，在 Science 论文中未找到可直接支持的开发前内部记录。原论文是在分析后联系厂商，并由厂商独立复核及合作试验；HDSR 归因需独立确认。[Science 原论文第 7 页](https://www.ftc.gov/system/files/documents/public_events/1548288/privacycon-2020-ziad_obermeyer.pdf)

## 算法、数据和发现是什么？

### Takeaway
研究将一所大型学术医院的真实风险评分与后续健康状况对照，发现预测费用在种族间大致校准，但等分患者的疾病负担不同，说明成本代理并不等同于健康需要。

### Cited Findings
- 【一手已核验】研究针对 2013–2015 年该院风险合同下初级保健患者；种族依据医院记录，以自报为基础，分析比较黑人与未报告其他种族或族裔的白人；样本全部有保险。研究并非对所有医院和所有人群的全国抽样。[原论文第 1、3 页](https://www.ftc.gov/system/files/documents/public_events/1548288/privacycon-2020-ziad_obermeyer.pdf)
- 【一手已核验】原模型输入包括前一年保险理赔数据中的年龄、性别、保险类型、诊断和操作编码、药物、费用等，显式排除种族；目标标签是随后一年的医疗总支出。它的真实应用是为高风险护理管理项目筛选病人。[原论文第 1、3 页](https://www.ftc.gov/system/files/documents/public_events/1548288/privacycon-2020-ziad_obermeyer.pdf)
- 【一手已核验】该院风险分数第 97 百分位处，黑人平均 4.8 种、白人 3.8 种活跃慢性病，相对差异 26.3%；同一评分下黑人在疾病严重程度的多项生物指标上也较差。[原论文第 1–3 页](https://www.ftc.gov/system/files/documents/public_events/1548288/privacycon-2020-ziad_obermeyer.pdf)
- 【一手已核验】研究按慢性病数量控制后，黑人病人每年平均费用低 1,801 美元；按具体疾病组合控制则低 1,144 美元。作者讨论医疗可及性及其他可能机制，此观察本身不分别识别各原因的因果份额。[原论文第 3 页](https://www.ftc.gov/system/files/documents/public_events/1548288/privacycon-2020-ziad_obermeyer.pdf)
- 【一手已核验】研究模拟在 97 百分位门槛、以活跃慢性病数比较边缘患者，逐步用门槛下病情更重的黑人替换门槛上病情较轻的白人，直到边缘患者健康程度相当；自动识别组内黑人占比从 17.7% 变为 46.5%。这是研究样本的反事实模拟，不是实际入组或治疗率，也不是所有黑人患者中获照护的比例。[原论文图 1 及第 2 页](https://www.ftc.gov/system/files/documents/public_events/1548288/privacycon-2020-ziad_obermeyer.pdf)
- 【一手已核验】55 百分位以上患者可被提示医生考虑，实际入组还受医生判断和资格条件影响。样本中实际入组观察值黑人占 19.2%，与自动识别门槛的模拟口径不同。[原论文第 5–6 页](https://www.ftc.gov/system/files/documents/public_events/1548288/privacycon-2020-ziad_obermeyer.pdf)
- 【一手已核验】厂商以全国 3,695,943 名商业保险患者数据复核，作者报告按其指标比较，同分黑人患者比白人多 48,772 个活跃慢性病；试验性地使用同时结合健康与费用的标签后为 7,758，减少 84%。这是厂商复核与实验结果，不证明已全国部署或所有种族健康差距消除。[原论文第 7 页](https://www.ftc.gov/system/files/documents/public_events/1548288/privacycon-2020-ziad_obermeyer.pdf)
- 【一手已核验】患者数据为受保护健康信息，不能公开；作者提供合成数据和分析代码，不等同于原始患者数据。[原论文第 7 页](https://www.ftc.gov/system/files/documents/public_events/1548288/privacycon-2020-ziad_obermeyer.pdf)；[作者代码与合成数据](https://gitlab.com/labsysmed/dissecting-bias)

### Inferences
- 这个案例适合讲“目标、代理指标和制度环境”：预测费用准确与识别医疗需要公平是不同评价问题，去除种族输入也不足以自动消除差异。上述结论只针对论文所检验的使用场景与指标。

### Gaps
- 原始商业模型源代码及固定版本本次未取得；上述输入、标签、筛选流程均为研究者从数据与厂商处获得的信息，不能扩写为完整的软件架构或当前线上部署情况。
