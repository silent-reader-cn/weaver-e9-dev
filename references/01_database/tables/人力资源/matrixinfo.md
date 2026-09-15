# 泛微OA 数据表: `matrixinfo`

- **所属模块**: `人力资源`
- **数据库表名**: `matrixinfo`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `name` | 名称 | `varchar2` | 800 | 是 | 名称 |
| 3 | `descr` | 描述 | `varchar2` | 1000 | 是 | 描述 |
| 4 | `priority` | 优先级 | `integer` | - | 是 | 优先级 |
| 5 | `createdate` | 创建日期 | `varchar2` | 240 | 是 | 创建日期 |
| 6 | `createtime` | 创建时间 | `varchar2` | 240 | 是 | 创建时间 |
| 7 | `createrid` | 创建人id | `integer` | - | 是 | 创建人id |
| 8 | `issystem` | 是否系统矩阵 | `integer` | - | 是 | 是否系统矩阵 |
