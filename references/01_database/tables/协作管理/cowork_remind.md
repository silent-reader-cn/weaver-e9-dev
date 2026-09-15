# 泛微OA 数据表: `cowork_remind`

- **所属模块**: `协作管理`
- **数据库表名**: `cowork_remind`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | - |
| 2 | `reminderid` | 提醒评论相关人 | `integer` | - | 是 | - |
| 3 | `discussid` | 评论ID | `integer` | - | 是 | - |
| 4 | `coworkid` | 协作ID | `integer` | - | 是 | - |
| 5 | `createdate` | 创建日期 | `varchar2` | 80 | 是 | - |
| 6 | `createtime` | 创建时间 | `varchar2` | 64 | 是 | - |
| 7 | `status` | 状态 | `integer` | - | 是 | - |
| 8 | `remindtype` | 提醒类型 | `integer` | - | 是 | - |
