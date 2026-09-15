# 泛微OA 数据表: `bill_hrmovertimesapa`

- **所属模块**: `人力资源`
- **数据库表名**: `bill_hrmovertimesapa`
- **字段总数**: `16`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `resourceid` | 姓名 | `integer` | - | 是 | 姓名 |
| 3 | `departmentid` | 部门 | `integer` | - | 是 | 部门 |
| 4 | `applydate` | 申请日期 | `char` | 10 | 是 | 申请日期 |
| 5 | `reason` | 加班理由 | `varchar2` | 1000 | 是 | 加班理由 |
| 6 | `fromdate` | 加班起始日期 | `char` | 10 | 是 | 加班起始日期 |
| 7 | `fromtime` | 加班起始时间 | `char` | 8 | 是 | 加班起始时间 |
| 8 | `tilldate` | 加班终止日期 | `char` | 10 | 是 | 加班终止日期 |
| 9 | `tilltime` | 加班终止时间 | `char` | 8 | 是 | 加班终止时间 |
| 10 | `totalhours` | 共计（小时） | `number` | (15,2) | 是 | 共计（小时） |
| 11 | `weekhours` | 平时加班时间（小时） | `number` | (15,2) | 是 | 平时加班时间（小时） |
| 12 | `weekendhours` | 周末加班时间（小时） | `number` | (15,2) | 是 | 周末加班时间（小时） |
| 13 | `holidayhours` | 节假日加班时间（小时） | `number` | (15,2) | 是 | 节假日加班时间（小时） |
| 14 | `comments` | 备注 | `varchar2` | 1000 | 是 | 备注 |
| 15 | `requestid` | 工作流请求的ID | `integer` | - | 是 | 对应表workflow_requestbase中的字段requestid |
| 16 | `resourceCode` | 人力资源编号 | `varchar2` | 60 | 否 | sapa专用 |
