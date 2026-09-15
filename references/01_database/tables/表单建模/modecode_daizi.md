# 泛微OA 数据表: `modecode_daizi`

- **所属模块**: `表单建模`
- **数据库表名**: `modecode_daizi`
- **字段总数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `fieldvalue` | 字段值 | `varchar2` | 100 | 是 | - |
| 2 | `shortvalue` | 短值 | `varchar2` | 100 | 是 | - |
| 3 | `id` | id | `integer` | - | 否 | - |
| 4 | `codedetailid` | 详细编码值 | `varchar2` | 100 | 是 | modecodedetail 表对应的id |
