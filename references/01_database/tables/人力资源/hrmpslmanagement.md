# 泛微OA 数据表: `hrmpslmanagement`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmpslmanagement`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `resourceid` | 人员id | `integer` | - | 是 | 对应hrmresource表主键id |
| 3 | `pslyear` | 有效期年 | `varchar2` | 240 | 是 | 有效期年 |
| 4 | `psldays` | 有效期天 | `float` | 22 | 是 | 有效期天 |
| 5 | `status` | 状态 | `integer` | - | 是 | 状态 |
| 6 | `leavetype` | 带薪假类型 | `integer` | - | 是 | 带薪假类型  -12:带薪病假  -13调休假  -6年假 |
