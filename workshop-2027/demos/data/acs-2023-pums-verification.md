# ACS 2023 马萨诸塞州样本：第 5 页复核

2026-10-31 核验：Claude 项目会话 `84b61ce5-1ba1-4b0d-b541-57b43e9b9936` 记录了从美国人口普查局下载 [person](https://www2.census.gov/programs-surveys/acs/data/pums/2023/1-Year/csv_pma.zip) 和 [housing](https://www2.census.gov/programs-surveys/acs/data/pums/2023/1-Year/csv_hma.zip) 文件，以及 `uniq.py`、`uniq_dob.py` 生成脚本。临时目录中的 CSV 仍可读取；其各自 SHA-256 与同目录 ZIP 内文件一致。尚未从官方重新下载文件比对散列，故来源为官方来源的下载记录及本地复算，而非本次重新下载验证。

- person CSV `psam_p25.csv` SHA-256: `90f33bb5c993d8f7ef812f71c8e8e2e8a8430cb913e769e8309fa1537dd1c1b3`
- housing CSV `psam_h25.csv` SHA-256: `2e9085a0a241491e7c67d38555d9b83b44e3d0563978bd8379f643dd06bf9731`
- 本次逐行重新计算：73,126 行；OCCP 516 个非空代码，25,955 条空值；空值作为第 517 类。代码 0440 有 1,556 条；[官方字典](https://www2.census.gov/programs-surveys/acs/tech_docs/pums/data_dict/PUMS_Data_Dictionary_2023.pdf)称该类别 Other Managers。数字是未加权的样本记录数，不是全州人口数。
- 勾选 PUMA、AGEP、SEX、MAR、CIT、OCCP，按照六字段的原始值精确分组（空值独立一类），得到 57,020 组，50,635 个单人组：50,635 ÷ 73,126 × 100 = 69.2435%；Σ(组人数²) ÷ 73,126 = 2.30077。原始预计算 JSON 和 HTML 嵌入表分别给 69.24% 和 2.30，符合四舍五入。
- 原脚本按 SERIALNO 连接 person 和 housing；空值填 NA，组合先编码为 uint64 哈希后统计，保留 u 的百分比两位小数以及平均组大小两位小数。上面六项不需要 housing；本次以原始值元组分组直接复算，不依赖该哈希。本次未逐个复核全部组合，不能排除哈希碰撞及其他组合问题。
- 出生日期模式另外在年龄后加随机 0–364（seed 7），是合成日序号，不是真实生日，且生成过程假定日期均匀分布；无法据此声称真实人口识别率。样本内唯一不等于全州唯一，也不等于再识别成功；数据未使用 PWGTP 权重。
- 复核脚本：`scripts/verify_pums_occupation.py <psam_p25.csv>`，使用标准库读取公开 person CSV。
