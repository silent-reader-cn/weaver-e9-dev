# 泛微OA 数据表: `workflow_coderegulate`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_coderegulate`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `formid` | 表单id | `integer` | - | 否 | - |
| 3 | `showid` | 显示id | `integer` | - | 否 | - |
| 4 | `showtype` | 显示类型 | `char` | 1 | 是 | - |
| 5 | `codevalue` | code值 | `varchar2` | 800 | 是 | - |
| 6 | `codeorder` | code顺序 | `integer` | - | 是 | - |
| 7 | `isbill` | 是否为单据 | `char` | 1 | 是 | - |
| 8 | `workflowid` | 流程id | `integer` | - | 是 | - |
| 9 | `concretefield` | 具体字段 | `varchar2` | 160 | 是 | - |
| 10 | `enablecode` | 使能code | `varchar2` | 160 | 是 | - |
