# 泛微OA 数据表: `fnawfrequestidlog`

- **所属模块**: `财务管理`
- **数据库表名**: `fnawfrequestidlog`
- **字段总数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `requestid` | reqid | `integer` | - | 否 | - |
| 2 | `wffnatype` | 预算action类型 | `varchar2` | 240 | 是 | 预算变更流程：FnaChangeEffectNew；费用分摊流程：FnaShareEffectNew； |
| 3 | `lockdate` | 触发日期 | `varchar2` | 160 | 是 | - |
| 4 | `locktime` | 触发时间 | `varchar2` | 160 | 是 | - |
