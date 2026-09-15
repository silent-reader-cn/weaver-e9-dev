# 泛微OA 数据表: `hrm_compensationtargetinfo`

- **所属模块**: `人力资源`
- **数据库表名**: `hrm_compensationtargetinfo`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `subcompanyid` | 分部id | `integer` | - | 是 | 分部id |
| 3 | `departmentid` | 部门id | `integer` | - | 是 | 部门id |
| 4 | `compensationyear` | 年 | `integer` | - | 是 | 年 |
| 5 | `compensationmonth` | 月 | `integer` | - | 是 | 月 |
| 6 | `userid` | 员工id | `integer` | - | 是 | 员工id |
| 7 | `memo` | 备注 | `varchar2` | 1000 | 是 | 备注 |
| 8 | `lastmodifytime` | 最后修改时间 | `varchar2` | 400 | 是 | 最后修改时间 |
