# 泛微OA 数据表: `coremaillog`

- **所属模块**: `集成模块`
- **数据库表名**: `coremaillog`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键id | `integer` | - | 否 | - |
| 2 | `datatype` | 数据类型 | `integer` | - | 是 | - |
| 3 | `operatedata` | 关联数据 | `varchar2` | 1000 | 是 | - |
| 4 | `operatetype` | 操作类型 | `integer` | - | 是 | - |
| 5 | `operateresult` | 操作结果 | `integer` | - | 是 | - |
| 6 | `operateremark` | 失败原因 | `varchar2` | 2000 | 是 | - |
| 7 | `logdate` | 日志日期 | `varchar2` | 50 | 是 | - |
| 8 | `logtime` | 日志时间 | `varchar2` | 50 | 是 | - |
