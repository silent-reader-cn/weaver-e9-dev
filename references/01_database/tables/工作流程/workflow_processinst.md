# 泛微OA 数据表: `workflow_processinst`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_processinst`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `pd_id` | 短语描述id | `integer` | - | 是 | - |
| 3 | `phrasedesc` | 短语描述 | `varchar2` | 1000 | 是 | - |
| 4 | `phraseshort` | 短语 | `varchar2` | 800 | 是 | - |
| 5 | `sortorder` | 排序 | `number` | (15,2) | 是 | - |
| 6 | `isdefault` | 是否为默认 | `integer` | - | 是 | - |
