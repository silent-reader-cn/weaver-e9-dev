# 泛微OA 数据表: `mode_exportexcelset`

- **中文名称**: 导出excel设置表
- **所属模块**: `表单建模`
- **数据库表名**: `mode_exportexcelset`
- **主键**: `customid`
- **字段数**: `7`

> 说明：导出excel设置信息表

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `customid` | 查询列表id | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `iscustomstyle` | 是否自定义导出样式 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 3 | `isgroupexport` | 是否分组导出 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 4 | `isexportfield` | 是否自定义导出字段 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 5 | `lastoperator` | 操作者id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `operatedate` | 操作日期 | `varchar2` | 10 | 是 | 否 | 否 | - | - | - |
| 7 | `operatetime` | 操作时间 | `varchar2` | 8 | 是 | 否 | 否 | - | - | - |
