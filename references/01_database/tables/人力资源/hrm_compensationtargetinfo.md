# 泛微OA 数据表: `hrm_compensationtargetinfo`

- **中文名称**: 薪酬指标数据维护信息表
- **所属模块**: `人力资源`
- **数据库表名**: `hrm_compensationtargetinfo`
- **主键**: `id`
- **字段数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 是 | - | - | ID |
| 2 | `subcompanyid` | 分部id | `integer` | - | 是 | 否 | 否 | - | - | 分部id |
| 3 | `departmentid` | 部门id | `integer` | - | 是 | 否 | 否 | - | - | 部门id |
| 4 | `compensationyear` | 年 | `integer` | - | 是 | 否 | 否 | - | - | 年 |
| 5 | `compensationmonth` | 月 | `integer` | - | 是 | 否 | 否 | - | - | 月 |
| 6 | `userid` | 员工id | `integer` | - | 是 | 否 | 否 | - | - | 员工id |
| 7 | `memo` | 备注 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 备注 |
| 8 | `lastmodifytime` | 最后修改时间 | `varchar2` | 400 | 是 | 否 | 否 | - | - | 最后修改时间 |
