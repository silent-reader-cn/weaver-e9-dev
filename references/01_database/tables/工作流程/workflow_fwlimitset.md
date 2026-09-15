# 泛微OA 数据表: `workflow_fwlimitset`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_fwlimitset`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 是 | - |
| 2 | `wfid` | 流程id | `integer` | - | 是 | - |
| 3 | `nodeid` | 节点id | `integer` | - | 是 | - |
| 4 | `fwtype` | 类型 | `char` | 1 | 是 | - |
| 5 | `modetype` | 模式 | `char` | 1 | 是 | - |
| 6 | `isopen` | 是否打开 | `char` | 1 | 是 | - |
| 7 | `lastoperator` | 最后操作者 | `integer` | - | 是 | - |
| 8 | `lastoperatedate` | 最后操作日期 | `char` | 10 | 是 | - |
| 9 | `lastoperatetime` | 最后操作时间 | `char` | 8 | 是 | - |
