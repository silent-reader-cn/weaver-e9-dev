# 泛微OA 数据表: `hrmjobgroups`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmjobgroups`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `jobgroupname` | 工作类型描述 | `varchar2` | 1000 | 是 | 工作类型描述 |
| 3 | `jobgroupremark` | 工作类型标识 | `varchar2` | 4000 | 是 | 工作类型标识 |
| 4 | `created` | 创建时间 | `timestamp(6)` | 11 | 是 | 创建时间 |
| 5 | `creater` | 创建者 | `integer` | - | 是 | 创建者 |
| 6 | `modified` | 修改时间 | `timestamp(6)` | 11 | 是 | 修改时间 |
| 7 | `modifier` | 修改人 | `integer` | - | 是 | 修改人 |
