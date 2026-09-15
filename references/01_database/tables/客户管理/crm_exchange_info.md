# 泛微OA 数据表: `crm_exchange_info`

- **所属模块**: `客户管理`
- **数据库表名**: `crm_exchange_info`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `sortid` | 客户id | `integer` | - | 是 | 客户id |
| 2 | `type_n` | 留言类型 | `char` | 2 | 是 | 留言类型 |
| 3 | `readdate` | 查看日期 | `char` | 10 | 是 | 查看日期 |
| 4 | `readtime` | 查看时间 | `char` | 10 | 是 | 查看时间 |
| 5 | `recentid` | 同类型最后一条留言记录ID | `integer` | - | 是 | 同类型最后一条留言记录ID |
| 6 | `userid` | 人员id | `integer` | - | 是 | 人员id |
