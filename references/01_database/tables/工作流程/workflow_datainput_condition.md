# 泛微OA 数据表: `workflow_datainput_condition`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_datainput_condition`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | - |
| 2 | `datainputid` | 数据输入id | `integer` | - | 是 | - |
| 3 | `fieldname` | 字段名称 | `varchar2` | 320 | 是 | - |
| 4 | `connection` | 连接 | `integer` | - | 是 | - |
| 5 | `value` | 值 | `varchar2` | 1000 | 是 | - |
