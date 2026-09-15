# 泛微OA 数据表: `workflow_browserurl`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_browserurl`
- **字段总数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `labelid` | 浏览框显示名称 | `integer` | - | 是 | - |
| 3 | `fielddbtype` | 数据库表字段类型 | `varchar2` | 320 | 是 | - |
| 4 | `browserurl` | 页面链接url | `varchar2` | 1000 | 是 | - |
| 5 | `tablename` | 数据库表名称 | `varchar2` | 400 | 是 | - |
| 6 | `columname` | 数据库表字段名称 | `varchar2` | 400 | 是 | - |
| 7 | `keycolumname` | 数据库表关键字段名称 | `varchar2` | 400 | 是 | - |
| 8 | `linkurl` | 信息链接url | `varchar2` | 1000 | 是 | - |
| 9 | `typeid` | 类型id | `integer` | - | 是 | - |
| 10 | `useable` | 是否可用 | `char` | 1 | 是 | - |
| 11 | `orderid` | 自定义顺序id | `integer` | - | 是 | - |
