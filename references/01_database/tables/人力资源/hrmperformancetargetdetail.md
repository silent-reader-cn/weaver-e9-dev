# 泛微OA 数据表: `hrmperformancetargetdetail`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmperformancetargetdetail`
- **字段总数**: `13`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `targetid` | 人力资源指标id | `integer` | - | 是 | 人力资源指标id |
| 3 | `targetname` | 指标名称 | `varchar2` | 800 | 是 | 指标名称 |
| 4 | `targetcode` | 指标编码 | `varchar2` | 160 | 是 | 指标编码 |
| 5 | `type_l` | 评分指标类型1 | `char` | 1 | 是 | 评分指标类型1 |
| 6 | `cycle` | 考核周期 | `char` | 1 | 是 | 考核周期 |
| 7 | `type_t` | 评分指标类型2 | `char` | 1 | 是 | 评分指标类型2 |
| 8 | `unit` | 个数 | `varchar2` | 80 | 是 | 个数 |
| 9 | `targetvalue` | 指标值 | `number` | (15,1) | 是 | 指标值 |
| 10 | `previewvalue` | 预览值 | `number` | (15,1) | 是 | 预览值 |
| 11 | `memo` | 定义 | `varchar2` | 1000 | 是 | 定义 |
| 12 | `others` | 其他人员 | `varchar2` | 800 | 是 | 其他人员 |
| 13 | `owner` | 包含自己 | `integer` | - | 是 | 包含自己 |
