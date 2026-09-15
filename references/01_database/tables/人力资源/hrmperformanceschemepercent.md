# 泛微OA 数据表: `hrmperformanceschemepercent`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmperformanceschemepercent`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `itemid` | 工作计划id | `integer` | - | 是 | 工作计划id |
| 3 | `nodeid` | 节点id | `integer` | - | 是 | 节点id |
| 4 | `groupid` | 分组id | `integer` | - | 是 | 分组id |
| 5 | `percent_n` | 占比 | `integer` | - | 是 | 占比 |
| 6 | `type_n` | 所属类型 | `char` | 1 | 是 | 0:节点，1：操作着 2：下游 |
| 7 | `type_d` | 是否含下游 | `char` | 1 | 是 | 0：否，1：是 |
