# 泛微OA 数据表: `hrmresource`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmresource`
- **字段总数**: `24`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `haschangepwd` | 密码是否已经改过 | `varchar2` | 80 | 是 | 密码是否已经改过 |
| 2 | `created` | 创建时间 | `timestamp(6)` | 11 | 是 | 创建时间 |
| 3 | `creater` | 创建人id | `integer` | - | 是 | 创建人id |
| 4 | `modified` | 修改时间 | `timestamp(6)` | 11 | 是 | 修改时间 |
| 5 | `modifier` | 修改人id | `integer` | - | 是 | 修改人id |
| 6 | `passwordlocktime` | 密码锁定时间 | `date` | 7 | 是 | 密码锁定时间 |
| 7 | `salt` | 加盐 | `varchar2` | 800 | 是 | 加盐 |
| 8 | `mobilecaflag` | 未知字段 | `varchar2` | 80 | 是 | 未知字段 |
| 9 | `companystartdate` | 公司开始日期 | `char` | 10 | 是 | 公司开始日期 |
| 10 | `companyworkyear` | 公司年限 | `number` | (4,2) | 是 | 公司年限 |
| 11 | `workstartdate` | 工作开始日期 | `char` | 10 | 是 | 工作开始日期 |
| 12 | `workyear` | 工作年限 | `number` | (4,2) | 是 | 工作年限 |
| 13 | `secondarypwd` | 第二密码 | `varchar2` | 100 | 是 | 第二密码 |
| 14 | `usesecondarypwd` | 使用第二密码 | `integer` | - | 是 | 使用第二密码 |
| 15 | `usekind` | 用工性质 | `integer` | - | 是 | 用工性质 |
| 16 | `jobcall` | 职称 | `integer` | - | 是 | 职称 |
| 17 | `accumfundaccount` | 公积金帐号 | `varchar2` | 240 | 是 | 公积金帐号 |
| 18 | `birthplace` | 出生地 | `varchar2` | 480 | 是 | 出生地 |
| 19 | `folk` | 民族 | `varchar2` | 240 | 是 | 民族 |
| 20 | `residentphone` | 居住地电话 | `varchar2` | 480 | 是 | 居住地电话 |
| 21 | `residentpostcode` | 居住地邮编 | `varchar2` | 480 | 是 | 居住地邮编 |
| 22 | `extphone` | 分机 | `varchar2` | 400 | 是 | 分机 |
| 23 | `managerstr` | 所有上级 | `varchar2` | 1000 | 是 | 所有上级 |
| 24 | `status` | 状态 | `integer` | - | 是 | - |
