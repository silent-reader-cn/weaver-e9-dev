# 泛微OA 数据表: `mode_databatchimport`

- **所属模块**: `表单建模`
- **数据库表名**: `mode_databatchimport`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `importorder` | 导入顺序 | `integer` | - | 是 | - |
| 2 | `id` | ID | `integer` | - | 否 | - |
| 3 | `modeid` | 模块id | `integer` | - | 是 | 对应modeinfo表的id |
| 4 | `interfacepath` | 接口路径 | `varchar2` | 1000 | 是 | 接口路径为验证导入数据的接口路径 |
| 5 | `isuse` | 是否启用 | `integer` | - | 是 | - |
