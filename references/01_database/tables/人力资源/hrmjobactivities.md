# 泛微OA 数据表: `hrmjobactivities`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmjobactivities`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `jobactivitymark` | 职责标识 | `varchar2` | 480 | 是 | 职责标识 |
| 3 | `jobactivityname` | 职责描述 | `varchar2` | 1000 | 是 | 职责描述 |
| 4 | `jobgroupid` | 所属工作类型 | `integer` | - | 是 | 所属工作类型 |
| 5 | `joblevelfrom` | 该职务的最低职级 | `integer` | - | 是 | 该职务的最低职级 |
| 6 | `joblevelto` | 该职务的最高职级 | `integer` | - | 是 | 该职务的最高职级 |
| 7 | `created` | 创建时间 | `timestamp(6)` | 11 | 是 | 创建时间 |
| 8 | `creater` | 创建人id | `integer` | - | 是 | 创建人id |
| 9 | `modified` | 修改时间 | `timestamp(6)` | 11 | 是 | 修改时间 |
| 10 | `modifier` | 修改人id | `integer` | - | 是 | 修改人id |
