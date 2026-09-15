# 泛微OA 数据表: `workflow_datainput_entry`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_datainput_entry`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `isdel` | 是否删除已有数据 | `varchar2` | 1 | 是 | 1：删除 |
| 2 | `enable` | 是否启用 | `integer` | - | 是 | - |
| 3 | `id` | ID | `integer` | - | 否 | - |
| 4 | `workflowid` | 工作流id | `integer` | - | 是 | - |
| 5 | `triggerfieldname` | 触发其他字段值的字段名称 | `varchar2` | 400 | 是 | - |
| 6 | `type` | 主字段/明细字段 | `char` | 1 | 是 | 0、主字段，1、明细字段 |
| 7 | `triggername` | 触发名称 | `varchar2` | 800 | 是 | - |
| 8 | `detailindex` | 明细索引 | `varchar2` | 80 | 是 | - |
