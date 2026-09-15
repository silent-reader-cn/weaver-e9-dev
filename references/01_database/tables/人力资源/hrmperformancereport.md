# 泛微OA 数据表: `hrmperformancereport`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmperformancereport`
- **字段总数**: `13`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `reportgroupid` | 分组id | `integer` | - | 是 | 分组id |
| 3 | `planid` | 计划id | `integer` | - | 是 | 计划id |
| 4 | `objid` | 对象id | `integer` | - | 是 | 对象id |
| 5 | `cycle` | 考核周期 | `char` | 1 | 是 | 考核周期 |
| 6 | `docid` | 文档id | `varchar2` | 800 | 是 | 文档id |
| 7 | `allshare` | 是否分享给所有人 | `char` | 1 | 是 | 0否1是 |
| 8 | `reportdate` | 报告日期 | `varchar2` | 80 | 是 | 报告日期 |
| 9 | `reporttype` | 报告所属类型 | `char` | 1 | 是 | 报告所属类型 |
| 10 | `status` | 状态 | `char` | 1 | 是 | 状态 |
| 11 | `percent_n` | 百分比 | `integer` | - | 是 | 百分比 |
| 12 | `pointself` | 评分规则范围 | `number` | (10,3) | 是 | 评分规则范围 |
| 13 | `reporttypep` | 报告所属类型2 | `char` | 1 | 是 | 报告所属类型2 |
