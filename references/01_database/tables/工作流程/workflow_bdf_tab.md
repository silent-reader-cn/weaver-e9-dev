# 泛微OA 数据表: `workflow_bdf_tab`

- **中文名称**: 浏览框数据定义-tab设置
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_bdf_tab`
- **主键**: `workflowid + fieldid`
- **字段数**: `6`

> 说明：浏览框数据定义-浏览框tab设置

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `workflowid` | 流程ID | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `fieldid` | 字段ID | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `tabkey` | 浏览框tab唯一key | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `showtab` | 是否显示 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 5 | `defaultselectedtab` | 默认选中 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 6 | `showorder` | tab显示顺序 | `integer` | - | 是 | 否 | 否 | - | - | - |
