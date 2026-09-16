# 泛微OA 数据表: `mode_dmlactionset`

- **中文名称**: DML接口动作基本信息
- **所属模块**: `表单建模`
- **数据库表名**: `mode_dmlactionset`
- **主键**: `id`
- **字段数**: `12`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `dmlsource` | 数据源 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `dmlsourcetype` | 数据类型 | `varchar2` | 10 | 是 | 否 | 否 | - | - | - |
| 3 | `dmlsourceorder` | 来源类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 5 | `dmlactionname` | 名称 | `varchar2` | 1000 | 否 | 否 | 否 | - | - | - |
| 6 | `dmlorder` | 执行顺序 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `modeid` | 模块id | `integer` | - | 是 | 否 | 否 | - | - | 对应modeinfo表的id |
| 8 | `expandid` | 页面扩展id | `integer` | - | 是 | 否 | 否 | - | - | 对应mode_pageexpand表的id |
| 9 | `datasourceid` | 数据源 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 数据源id |
| 10 | `dmltype` | dml类型 | `varchar2` | 80 | 是 | 否 | 否 | - | - | insert：insert操作<br>update：update操作<br>delete：delete操作 |
| 11 | `isresetright` | 是否重构权限 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 12 | `targetmodeid` | 目标模块id | `integer` | - | 是 | 否 | 否 | - | - | - |
