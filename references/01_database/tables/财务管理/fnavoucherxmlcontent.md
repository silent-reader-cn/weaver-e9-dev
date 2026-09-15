# 泛微OA 数据表: `fnavoucherxmlcontent`

- **所属模块**: `财务管理`
- **数据库表名**: `fnavoucherxmlcontent`
- **字段总数**: `13`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `fnavoucherxmlid` | fnavoucherxml.id | `integer` | - | 是 | - |
| 3 | `contenttype` | 节点类型 | `char` | 1 | 是 | - |
| 4 | `contentparentid` | 节点父id | `integer` | - | 是 | - |
| 5 | `contentname` | 节点名称 | `varchar2` | 800 | 是 | - |
| 6 | `contentvaluetype` | 节点值类型 | `char` | 1 | 是 | - |
| 7 | `contentmemo` | 节点备注 | `varchar2` | 4000 | 是 | - |
| 8 | `orderid` | 排序id | `number` | (5,2) | 是 | - |
| 9 | `isnullnotprint` | 节点值为空时是否显示 | `integer` | - | 是 | - |
| 10 | `contentvalue` | 节点值 | `clob` | 4000 | 是 | - |
| 11 | `parameter` | 节点参数字符串 | `clob` | 4000 | 是 | - |
| 12 | `isnullnotprintnode` | 子节点为空时是否显示 | `integer` | - | 是 | - |
| 13 | `oldid` | 作废 | `integer` | - | 是 | - |
