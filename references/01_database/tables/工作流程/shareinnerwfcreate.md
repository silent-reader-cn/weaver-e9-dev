# 泛微OA 数据表: `shareinnerwfcreate`

- **所属模块**: `工作流程`
- **数据库表名**: `shareinnerwfcreate`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 是 | - |
| 2 | `gid` | 操作者明细表id | `integer` | - | 否 | - |
| 3 | `workflowid` | 流程id | `integer` | - | 否 | - |
| 4 | `content` | 相关对象id | `integer` | - | 是 | - |
| 5 | `min_seclevel` | 最小安全级别 | `integer` | - | 是 | - |
| 6 | `max_seclevel` | 最大安全级别 | `integer` | - | 是 | - |
| 7 | `isbelong` | 是否属于 | `integer` | - | 是 | - |
