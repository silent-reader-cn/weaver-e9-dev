# 泛微OA 数据表: `workflow_reporttype`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_reporttype`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `typeorder` | 显示顺序 | `number` | (11,2) | 是 | - |
| 2 | `id` | ID | `integer` | - | 否 | - |
| 3 | `typename` | 报表种类名称 | `varchar2` | 480 | 是 | - |
| 4 | `typedesc` | 报表种类描述 | `varchar2` | 1000 | 是 | - |
| 5 | `typeorder_bak` | 未使用 | `integer` | - | 是 | - |
