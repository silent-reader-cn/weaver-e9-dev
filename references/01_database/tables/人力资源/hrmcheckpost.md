# 泛微OA 数据表: `hrmcheckpost`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmcheckpost`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 考核种类的id |
| 2 | `checktypeid` | 考核种类的id | `integer` | - | 是 | 考核种类的id |
| 3 | `jobid` | 考核岗位的id | `integer` | - | 是 | 考核岗位的id |
| 4 | `deptid` | 部门id | `integer` | - | 是 | 部门id |
| 5 | `subcid` | 分部id | `integer` | - | 是 | 分部id |
