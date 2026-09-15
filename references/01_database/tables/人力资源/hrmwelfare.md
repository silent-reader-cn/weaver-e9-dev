# 泛微OA 数据表: `hrmwelfare`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmwelfare`
- **字段总数**: `16`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `resourceid` | 人员id | `integer` | - | 是 | 人员id |
| 3 | `datefrom` | 开始时间 | `char` | 10 | 是 | 开始时间 |
| 4 | `dateto` | 结束时间 | `char` | 10 | 是 | 结束时间 |
| 5 | `basesalary` | 基本工资 | `number` | (18,2) | 是 | 基本工资 |
| 6 | `homesub` | 房贴 | `number` | (18,2) | 是 | 房贴 |
| 7 | `vehiclesub` | 车贴 | `number` | (18,2) | 是 | 车贴 |
| 8 | `mealsub` | 饭贴 | `number` | (18,2) | 是 | 饭贴 |
| 9 | `othersub` | 其他 | `number` | (18,2) | 是 | 其他 |
| 10 | `adjustreason` | 调整原因 | `varchar2` | 1000 | 是 | 调整原因 |
| 11 | `createid` | 创建人id | `integer` | - | 是 | 创建人id |
| 12 | `createdate` | 创建日期 | `char` | 10 | 是 | 创建日期 |
| 13 | `createtime` | 创建时间 | `char` | 8 | 是 | 创建时间 |
| 14 | `lastmoderid` | 最后修改人id | `integer` | - | 是 | 最后修改人id |
| 15 | `lastmoddate` | 最后修改日期 | `char` | 10 | 是 | 最后修改日期 |
| 16 | `lastmodtime` | 最后修改时间 | `char` | 8 | 是 | 最后修改时间 |
