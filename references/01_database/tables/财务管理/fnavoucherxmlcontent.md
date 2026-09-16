# 泛微OA 数据表: `fnavoucherxmlcontent`

- **中文名称**: 预算凭证xml节点信息表
- **所属模块**: `财务管理`
- **数据库表名**: `fnavoucherxmlcontent`
- **主键**: `id`
- **字段数**: `13`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `fnavoucherxmlid` | fnavoucherxml.id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `contenttype` | 节点类型 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 4 | `contentparentid` | 节点父id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `contentname` | 节点名称 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 6 | `contentvaluetype` | 节点值类型 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 7 | `contentmemo` | 节点备注 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 8 | `orderid` | 排序id | `number` | (5,2) | 是 | 否 | 否 | - | - | - |
| 9 | `isnullnotprint` | 节点值为空时是否显示 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 10 | `contentvalue` | 节点值 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 11 | `parameter` | 节点参数字符串 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 12 | `isnullnotprintnode` | 子节点为空时是否显示 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 13 | `oldid` | 作废 | `integer` | - | 是 | 否 | 否 | - | - | - |
