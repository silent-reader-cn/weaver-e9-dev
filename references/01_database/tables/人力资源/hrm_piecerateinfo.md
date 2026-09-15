# 泛微OA 数据表: `hrm_piecerateinfo`

- **所属模块**: `人力资源`
- **数据库表名**: `hrm_piecerateinfo`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `subcompanyid` | 分部id | `integer` | - | 是 | 分部id |
| 3 | `departmentid` | 部门id | `integer` | - | 是 | 部门id |
| 4 | `pieceyear` | 年 | `integer` | - | 是 | 年 |
| 5 | `piecemonth` | 月 | `integer` | - | 是 | 月 |
| 6 | `usercode` | 员工编号 | `varchar2` | 30 | 是 | 员工编号 |
| 7 | `piecerateno` | 计件编号 | `varchar2` | 30 | 是 | 计件编号 |
| 8 | `pieceratedate` | 工作日期 | `varchar2` | 1000 | 是 | 工作日期 |
| 9 | `piecenum` | 数量 | `number` | (15,2) | 是 | 数量 |
| 10 | `memo` | 备注 | `varchar2` | 1000 | 是 | 备注 |
