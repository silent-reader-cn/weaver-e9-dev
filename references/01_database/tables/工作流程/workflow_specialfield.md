# 泛微OA 数据表: `workflow_specialfield`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_specialfield`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `fieldid` | 字段的id | `integer` | - | 是 | - |
| 3 | `displayname` | 显示名 | `varchar2` | 1000 | 是 | - |
| 4 | `linkaddress` | 链接地址 | `varchar2` | 1000 | 是 | - |
| 5 | `descriptivetext` | 描述性文字 | `varchar2` | 4000 | 是 | - |
| 6 | `isbill` | isbill=1 表示字段为单据字段 | `integer` | - | 是 | - |
| 7 | `isform` | isform=1 表示字段为表单字段 | `integer` | - | 是 | - |
