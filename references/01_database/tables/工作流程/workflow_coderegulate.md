# 泛微OA 数据表: `workflow_coderegulate`

- **中文名称**: 流程编号生成规则表
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_coderegulate`
- **主键**: `id`
- **字段数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `formid` | 表单id | `integer` | - | 否 | 否 | 否 | - | - | - |
| 3 | `showid` | 显示id | `integer` | - | 否 | 否 | 否 | - | - | - |
| 4 | `showtype` | 显示类型 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 5 | `codevalue` | code值 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 6 | `codeorder` | code顺序 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `isbill` | 是否为单据 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 8 | `workflowid` | 流程id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 9 | `concretefield` | 具体字段 | `varchar2` | 160 | 是 | 否 | 否 | - | - | - |
| 10 | `enablecode` | 使能code | `varchar2` | 160 | 是 | 否 | 否 | - | - | - |
