# 泛微OA 数据表: `bill_hrmschedulemain`

- **所属模块**: `人力资源`
- **数据库表名**: `bill_hrmschedulemain`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `resource_n` | 申请人 | `integer` | - | 是 | 申请人 |
| 3 | `reason` | 事由 | `varchar2` | 1000 | 是 | 事由 |
| 4 | `sumday` | 总天数 | `integer` | - | 是 | 总天数 |
| 5 | `requestid` | 流程id | `integer` | - | 是 | 流程id |
| 6 | `departmentid` | 部门 | `integer` | - | 是 | 部门 |
