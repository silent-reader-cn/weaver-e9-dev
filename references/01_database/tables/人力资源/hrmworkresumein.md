# 泛微OA 数据表: `hrmworkresumein`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmworkresumein`
- **字段总数**: `13`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `lastmoddate` | 最后修改日期 | `char` | 10 | 是 | 最后修改日期 |
| 2 | `lastmodtime` | 最后修改时间 | `char` | 8 | 是 | 最后修改时间 |
| 3 | `id` | ID | `integer` | - | 否 | ID |
| 4 | `resourceid` | 人力资源id | `integer` | - | 是 | 人力资源id |
| 5 | `datefrom` | 任职开始日期 | `char` | 10 | 是 | 任职开始日期 |
| 6 | `dateto` | 任职结束日期 | `char` | 10 | 是 | 任职结束日期 |
| 7 | `departmentid` | 部门id | `integer` | - | 是 | 部门id |
| 8 | `jobtitle` | 岗位id | `integer` | - | 是 | 岗位id |
| 9 | `joblevel` | 职级 | `integer` | - | 是 | 职级 |
| 10 | `createid` | 创建人 | `integer` | - | 是 | 创建人 |
| 11 | `createdate` | 创建日期 | `char` | 10 | 是 | 创建日期 |
| 12 | `createtime` | 创建时间 | `char` | 8 | 是 | 创建时间 |
| 13 | `lastmoderid` | 最后修改人 | `integer` | - | 是 | 最后修改人 |
