# 泛微OA 数据表: `workflow_code`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_code`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `formid` | 表单/单据id | `integer` | - | 否 | - |
| 2 | `flowid` | 流程id | `integer` | - | 否 | - |
| 3 | `codefieldid` | 编号字段id | `integer` | - | 是 | - |
| 4 | `isuse` | 是否起用 | `char` | 1 | 是 | - |
| 5 | `fieldlevel` | 字段级别 | `integer` | - | 是 | - |
| 6 | `currentcode` | 当前编号 | `varchar2` | 800 | 是 | - |
| 7 | `isbill` | 是否为单据 | `char` | 1 | 是 | - |
