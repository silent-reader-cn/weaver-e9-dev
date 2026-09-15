# 泛微OA 数据表: `bill_meeting_dt1_topic`

- **所属模块**: `会议管理`
- **数据库表名**: `bill_meeting_dt1_topic`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | 0 | 否 | 主键 |
| 2 | `mainid` | 对应流程主表id | `integer` | 0 | 是 | bill_meeting 的id |
| 3 | `subject` | 议程主题 | `varchar2` | 1000 | 是 | 议程主题 |
| 4 | `projid` | 相关项目 | `integer` | 0 | 是 | 相关项目 |
| 5 | `crmids` | 相关客户 | `varchar2` | 4000 | 是 | 相关客户 |
| 6 | `isopen` | 是否公开 | `integer` | 0 | 是 | 是否公开 |
| 7 | `hrmids` | 负责人 | `clob` | 4000 | 是 | 负责人 |
