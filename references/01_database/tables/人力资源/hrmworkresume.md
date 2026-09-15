# 泛微OA 数据表: `hrmworkresume`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmworkresume`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `resourceid` | 人力资源id | `integer` | - | 是 | 人力资源id |
| 3 | `startdate` | 开始时间 | `char` | 10 | 是 | 开始时间 |
| 4 | `enddate` | 结束时间 | `char` | 10 | 是 | 结束时间 |
| 5 | `company` | 公司 | `varchar2` | 800 | 是 | 公司 |
| 6 | `jobtitle` | 职位 | `varchar2` | 240 | 是 | 职位 |
| 7 | `workdesc` | 工作描述 | `varchar2` | 4000 | 是 | 工作描述 |
| 8 | `leavereason` | 离职原因 | `varchar2` | 1000 | 是 | 离职原因 |
