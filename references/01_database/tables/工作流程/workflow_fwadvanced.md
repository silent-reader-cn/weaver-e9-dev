# 泛微OA 数据表: `workflow_fwadvanced`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_fwadvanced`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 是 | - |
| 2 | `wfid` | 流程id | `integer` | - | 是 | - |
| 3 | `nodeid` | 节点id | `integer` | - | 是 | - |
| 4 | `fwtype` | 类型 | `char` | 1 | 是 | 1转发 2意见征询 3转办 |
| 5 | `uuid` | uuid | `varchar2` | 480 | 是 | 唯一标识 |
