# 泛微OA 数据表: `Modetabslog_xxx`

- **所属模块**: `表单建模`
- **数据库表名**: `Modetabslog_xxx`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | - |
| 2 | `tabid` | 标签id | `integer` | - | 是 | - |
| 3 | `operate` | 操作 | `integer` | - | 是 | - |
| 4 | `modeid` | 模块id | `integer` | - | 是 | - |
| 5 | `billid` | 数据id | `integer` | - | 是 | - |
| 6 | `creator` | 创建者 | `integer` | - | 是 | - |
| 7 | `fromuser` | 表单使用者 | `integer` | - | 是 | - |
| 8 | `createdate` | 创建日期 | `varchar2` | 80 | 是 | - |
| 9 | `createtime` | 创建时间 | `varchar2` | 64 | 是 | - |
