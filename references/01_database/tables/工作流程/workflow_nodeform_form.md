# 泛微OA 数据表: `workflow_nodeform_form`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_nodeform_form`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `formid` | 表单id | `integer` | - | 是 | - |
| 2 | `isbill` | 是否是单据 | `integer` | - | 是 | - |
| 3 | `fieldid` | 字段id | `integer` | - | 是 | - |
| 4 | `isview` | 是否可查看 | `char` | 1 | 是 | - |
| 5 | `isedit` | 是否可编辑 | `char` | 1 | 是 | - |
| 6 | `ismandatory` | 是否必填 | `char` | 1 | 是 | - |
| 7 | `orderid` | 顺序 | `number` | (10,2) | 是 | - |
| 8 | `isalonerow` | 是否单行显示 | `char` | 1 | 是 | - |
