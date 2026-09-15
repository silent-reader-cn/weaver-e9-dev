# 泛微OA 数据表: `workflow_modeview`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_modeview`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `formid` | 表单id或单据id | `integer` | - | 是 | - |
| 2 | `nodeid` | 节点id | `integer` | - | 是 | - |
| 3 | `isbill` | 是否是单据 | `integer` | - | 是 | - |
| 4 | `fieldid` | 字段id | `integer` | - | 是 | - |
| 5 | `isview` | 可查看 | `char` | 1 | 是 | - |
| 6 | `isedit` | 可编辑 | `char` | 1 | 是 | - |
| 7 | `ismandatory` | 必填 | `char` | 1 | 是 | - |
