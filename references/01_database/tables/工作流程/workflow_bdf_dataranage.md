# 泛微OA 数据表: `workflow_bdf_dataranage`

- **中文名称**: 流程浏览数据定义数据范围
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_bdf_dataranage`
- **主键**: `id`
- **字段数**: `14`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `workflowid` | 流程ID | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `fieldid` | 字段ID | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `type` | 类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `objid` | 类型对应值ID | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 6 | `seclevel1` | 安全级别最小值 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `seclevel2` | 安全级别最大值 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `conditions` | 矩阵ID | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 9 | `conditioncn` | 矩阵详情 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 10 | `bhxj` | 包含下级 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 11 | `virtualid` | 虚拟机构 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 12 | `objfieldid` | 类型对应字段ID | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 13 | `orders` | 显示顺序 | `number` | (5,2) | 是 | 否 | 否 | - | - | - |
| 14 | `administrativelevel` | 未使用 | `char` | 2 | 是 | 否 | 否 | - | - | - |
