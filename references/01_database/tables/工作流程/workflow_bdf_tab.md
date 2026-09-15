# 泛微OA 数据表: `workflow_bdf_tab`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_bdf_tab`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `workflowid` | 流程ID | `integer` | - | 是 | - |
| 2 | `fieldid` | 字段ID | `integer` | - | 是 | - |
| 3 | `tabkey` | 浏览框tab唯一key | `integer` | - | 是 | - |
| 4 | `showtab` | 是否显示 | `char` | 1 | 是 | - |
| 5 | `defaultselectedtab` | 默认选中 | `char` | 1 | 是 | - |
| 6 | `showorder` | tab显示顺序 | `integer` | - | 是 | - |
