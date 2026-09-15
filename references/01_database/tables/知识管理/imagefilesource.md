# 泛微OA 数据表: `imagefilesource`

- **所属模块**: `知识管理`
- **数据库表名**: `imagefilesource`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | id，自增长 |
| 2 | `imagefileid` | 文件id | `integer` | - | 是 | - |
| 3 | `comefrom` | 来源 | `varchar2` | 1000 | 是 | - |
| 4 | `objid` | 来源对象 | `integer` | - | 是 | - |
| 5 | `objotherpara` | 对象另外参数 | `varchar2` | 1000 | 是 | - |
