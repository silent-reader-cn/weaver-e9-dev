# 泛微OA 数据表: `workflow_bdf_dataranage`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_bdf_dataranage`
- **字段总数**: `14`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 是 | - |
| 2 | `workflowid` | 流程ID | `integer` | - | 是 | - |
| 3 | `fieldid` | 字段ID | `integer` | - | 是 | - |
| 4 | `type` | 类型 | `integer` | - | 是 | - |
| 5 | `objid` | 类型对应值ID | `varchar2` | 4000 | 是 | - |
| 6 | `seclevel1` | 安全级别最小值 | `integer` | - | 是 | - |
| 7 | `seclevel2` | 安全级别最大值 | `integer` | - | 是 | - |
| 8 | `conditions` | 矩阵ID | `varchar2` | 4000 | 是 | - |
| 9 | `conditioncn` | 矩阵详情 | `varchar2` | 4000 | 是 | - |
| 10 | `bhxj` | 包含下级 | `integer` | - | 是 | - |
| 11 | `virtualid` | 虚拟机构 | `varchar2` | 80 | 是 | - |
| 12 | `objfieldid` | 类型对应字段ID | `varchar2` | 4000 | 是 | - |
| 13 | `orders` | 显示顺序 | `number` | (5,2) | 是 | - |
| 14 | `administrativelevel` | 未使用 | `char` | 2 | 是 | - |
