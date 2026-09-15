# 泛微OA 数据表: `docpopupuser`

- **所属模块**: `知识管理`
- **数据库表名**: `docpopupuser`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `userid` | 用户id | `integer` | - | 是 | - |
| 3 | `docid` | 文档id | `integer` | - | 是 | - |
| 4 | `haspopnum` | 已经弹出次数 | `integer` | - | 是 | - |
| 5 | `beiyong` | 备用 | `varchar2` | 1000 | 是 | - |
