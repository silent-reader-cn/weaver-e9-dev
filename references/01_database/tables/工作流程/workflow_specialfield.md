# 泛微OA 数据表: `workflow_specialfield`

- **中文名称**: 特殊字段表
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_specialfield`
- **主键**: `id`
- **字段数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `fieldid` | 字段的id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `displayname` | 显示名 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 4 | `linkaddress` | 链接地址 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 5 | `descriptivetext` | 描述性文字 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 6 | `isbill` | isbill=1 表示字段为单据字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `isform` | isform=1 表示字段为表单字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
