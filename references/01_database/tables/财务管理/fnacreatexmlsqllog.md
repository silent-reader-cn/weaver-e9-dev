# 泛微OA 数据表: `fnacreatexmlsqllog`

- **所属模块**: `财务管理`
- **数据库表名**: `fnacreatexmlsqllog`
- **字段总数**: `3`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `guid1` | uuid | `varchar2` | 50 | 是 | - |
| 3 | `exesql` | 执行的sql | `clob` | 4000 | 是 | - |
