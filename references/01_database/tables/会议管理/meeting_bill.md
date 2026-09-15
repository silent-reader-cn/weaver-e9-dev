# 泛微OA 数据表: `meeting_bill`

- **所属模块**: `会议管理`
- **数据库表名**: `meeting_bill`
- **字段总数**: `3`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `billid` | 会议表单id | `integer` | - | 是 | - |
| 2 | `defined` | meeting_defind表中的scopeid | `integer` | - | 是 | - |
| 3 | `tablename` | 会议流程表单对应的数据库表名 | `varchar2` | 800 | 是 | - |
