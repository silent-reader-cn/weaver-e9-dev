# 泛微OA 数据表: `mode_deletelog`

- **所属模块**: `表单建模`
- **数据库表名**: `mode_deletelog`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | - |
| 2 | `creator` | 创建者 | `integer` | - | 是 | - |
| 3 | `createdate` | 创建日期 | `varchar2` | 80 | 是 | - |
| 4 | `createtime` | 创建时间 | `varchar2` | 64 | 是 | - |
| 5 | `ip` | ip地址 | `varchar2` | 160 | 是 | - |
| 6 | `objecttype` | 类型 | `varchar2` | 8 | 是 | - |
| 7 | `objectid` | 操作id | `integer` | - | 是 | - |
| 8 | `objectname` | 操作名称 | `varchar2` | 1000 | 是 | - |
