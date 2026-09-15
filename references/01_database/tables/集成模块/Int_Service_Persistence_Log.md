# 泛微OA 数据表: `Int_Service_Persistence_Log`

- **所属模块**: `集成模块`
- **数据库表名**: `Int_Service_Persistence_Log`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 标识 | `integer` | - | 否 | 无 |
| 2 | `org_filename` | 原始文件名 | `varchar2` | 500 | 是 | 无 |
| 3 | `to_filename` | 重命名的文件名 | `varchar2` | 500 | 是 | 无 |
| 4 | `opttime` | 操作时间 | `varchar2` | 100 | 是 | 无 |
| 5 | `result` | 初始化结果 | `integer` | - | 是 | 1,成功;0,失败 |
| 6 | `summary` | 结果信息 | `varchar2` | 2000 | 是 | 成功写入success等信息,失败写入失败原因 |
