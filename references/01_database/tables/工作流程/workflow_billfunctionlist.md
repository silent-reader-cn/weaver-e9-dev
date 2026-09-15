# 泛微OA 数据表: `workflow_billfunctionlist`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_billfunctionlist`
- **字段总数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `billid` | 单据id | `integer` | - | 否 | - |
| 2 | `indaffirmance` | 是否支持提交确认 | `char` | 1 | 是 | 1：支持 |
| 3 | `indmouldtype` | 是否支持图形化 | `char` | 1 | 是 | 1：支持 |
| 4 | `indshowchart` | 是否支持提交后显示流程图 | `char` | 1 | 是 | 1：支持 |
