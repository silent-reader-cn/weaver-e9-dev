# 泛微OA 数据表: `workflow_codedetail`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_codedetail`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `mainid` | 主表id | `integer` | - | 否 | (workflow_code)formid |
| 2 | `showid` | 编号规则显示内容 | `integer` | - | 否 | - |
| 3 | `codevalue` | 编号规则的值 | `varchar2` | 800 | 是 | - |
| 4 | `codeorder` | 编号规则排序 | `integer` | - | 是 | - |
| 5 | `isbill` | 是否为单据 | `char` | 1 | 是 | 1：是，0或其它：否 |
| 6 | `workflowid` | 流程id | `integer` | - | 是 | - |
