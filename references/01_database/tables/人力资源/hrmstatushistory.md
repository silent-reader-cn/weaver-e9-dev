# 泛微OA 数据表: `hrmstatushistory`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmstatushistory`
- **字段总数**: `27`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `resourceid` | 人力资源id | `integer` | - | 是 | 人力资源id |
| 3 | `changedate` | 调整生效日期 | `char` | 10 | 是 | 调整生效日期 |
| 4 | `changeenddate` | 调整截至日期 | `char` | 10 | 是 | 调整截至日期 |
| 5 | `changereason` | 调整原因 | `varchar2` | 4000 | 是 | 调整原因 |
| 6 | `changecontractid` | 相关合同id | `integer` | - | 是 | 相关合同id |
| 7 | `oldjobtitleid` | 调整前岗位 | `integer` | - | 是 | 调整前岗位 |
| 8 | `oldjoblevel` | 调整前职级 | `integer` | - | 是 | 调整前职级 |
| 9 | `newjobtitleid` | 调整后岗位 | `integer` | - | 是 | 调整后岗位 |
| 10 | `newjoblevel` | 调整后职级 | `integer` | - | 是 | 调整后职级 |
| 11 | `infoman` | 通知人 | `varchar2` | 1000 | 是 | 通知人 |
| 12 | `type_n` | 调整类型id | `integer` | - | 是 | 调整类型id |
| 13 | `isdispose` | 是否即可生效 | `integer` | - | 是 | 是否即可生效 |
| 14 | `ischangesalary` | 是否改变工资 | `integer` | - | 是 | 是否改变工资 |
| 15 | `status` | 人力资源状态 | `integer` | - | 是 | 0:不活跃,1:活跃 |
| 16 | `oldmanagerid` | 调整前上级 | `integer` | - | 是 | 调整前上级 |
| 17 | `newmanagerid` | 调整后上级 | `integer` | - | 是 | 调整后上级 |
| 18 | `olddepartmentid` | 调整前部门 | `integer` | - | 是 | 调整前部门 |
| 19 | `newdepartmentid` | 调整后部门 | `integer` | - | 是 | 调整后部门 |
| 20 | `oldsubcompanyid` | 调整前分部 | `integer` | - | 是 | 调整前分部 |
| 21 | `newsubcompanyid` | 调整后分部 | `integer` | - | 是 | 调整后分部 |
| 22 | `operator` | 操作者 | `integer` | - | 是 | 操作者 |
| 23 | `operatedate` | 调整日期 | `char` | 10 | 是 | 调整日期 |
| 24 | `operatetime` | 调整时间 | `char` | 8 | 是 | 调整时间 |
| 25 | `clientaddress` | 客户端ip | `char` | 50 | 是 | 客户端ip |
| 26 | `operatefrom` | 调整来源 | `char` | 50 | 是 | 调整来源 |
| 27 | `type_o` | type_o | `integer` | - | 是 | type_o |
