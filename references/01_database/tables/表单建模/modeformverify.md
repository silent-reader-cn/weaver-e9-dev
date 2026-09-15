# 泛微OA 数据表: `modeformverify`

- **所属模块**: `表单建模`
- **数据库表名**: `modeformverify`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `varchar2` | 32 | 否 | - |
| 2 | `formid` | 表单id | `integer` | - | 否 | - |
| 3 | `fieldids` | 字段id | `clob` | 4000 | 否 | - |
| 4 | `operate` | 操作者 | `integer` | - | 否 | - |
| 5 | `tips` | 必填 | `clob` | 4000 | 是 | - |
| 6 | `color` | 颜色 | `varchar2` | 800 | 是 | - |
| 7 | `detailtable` | 明细表 | `varchar2` | 800 | 是 | - |
