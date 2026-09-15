# 泛微OA 数据表: `mode_dmlactionset`

- **所属模块**: `表单建模`
- **数据库表名**: `mode_dmlactionset`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `dmlsource` | 数据源 | `integer` | - | 是 | - |
| 2 | `dmlsourcetype` | 数据类型 | `varchar2` | 10 | 是 | - |
| 3 | `dmlsourceorder` | 来源类型 | `integer` | - | 是 | - |
| 4 | `id` | ID | `integer` | - | 否 | - |
| 5 | `dmlactionname` | 名称 | `varchar2` | 1000 | 否 | - |
| 6 | `dmlorder` | 执行顺序 | `integer` | - | 是 | - |
| 7 | `modeid` | 模块id | `integer` | - | 是 | 对应modeinfo表的id |
| 8 | `expandid` | 页面扩展id | `integer` | - | 是 | 对应mode_pageexpand表的id |
| 9 | `datasourceid` | 数据源 | `varchar2` | 1000 | 是 | 数据源id |
| 10 | `dmltype` | dml类型 | `varchar2` | 80 | 是 | - |
