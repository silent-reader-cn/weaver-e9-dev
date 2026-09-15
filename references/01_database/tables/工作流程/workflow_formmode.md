# 泛微OA 数据表: `workflow_formmode`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_formmode`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `formid` | 表单id | `integer` | - | 是 | - |
| 3 | `isbill` | 是否为单据 | `varchar2` | 8 | 是 | - |
| 4 | `isprint` | 是否打印模板 | `varchar2` | 8 | 是 | - |
| 5 | `modename` | 模式名称 | `varchar2` | 1000 | 是 | - |
| 6 | `modedesc` | 模式描述 | `clob` | 4000 | 是 | - |
