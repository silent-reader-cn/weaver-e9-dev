# 泛微OA 数据表: `mode_impexp_log`

- **所属模块**: `表单建模`
- **数据库表名**: `mode_impexp_log`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | - |
| 2 | `creator` | 创建者 | `integer` | - | 否 | - |
| 3 | `createdate` | 创建日期 | `varchar2` | 80 | 是 | - |
| 4 | `createtime` | 创建时间 | `varchar2` | 64 | 是 | - |
| 5 | `type` | 类型 | `integer` | - | 否 | - |
| 6 | `datatype` | 数据类型 | `integer` | - | 否 | - |
| 7 | `fileid` | 附件id | `integer` | - | 是 | - |
| 8 | `objid` | 操作id | `integer` | - | 是 | - |
