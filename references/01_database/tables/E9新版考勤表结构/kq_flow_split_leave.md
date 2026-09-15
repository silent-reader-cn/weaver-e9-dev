# 泛微OA 数据表: `kq_flow_split_leave`

- **所属模块**: `E9新版考勤表结构`
- **数据库表名**: `kq_flow_split_leave`
- **字段总数**: `31`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `requestid` | 流程的requestid | `varchar2` | - | 否 | - |
| 3 | `workflowid` | 流程的workflowid | `varchar2` | - | 否 | - |
| 4 | `dataid` | 表单主表的id | `varchar2` | - | 否 | - |
| 5 | `detailid` | 表单明细表的id | `varchar2` | - | 否 | - |
| 6 | `resourceid` | 人员id | `varchar2` | - | 否 | - |
| 7 | `fromdate` | 拆分后的开始日期 | `varchar2` | - | 否 | - |
| 8 | `fromtime` | 拆分后的开始时间 | `varchar2` | - | 否 | - |
| 9 | `todate` | 拆分后的结束日期 | `varchar2` | - | 否 | - |
| 10 | `totime` | 拆分后的结束时间 | `varchar2` | - | 否 | - |
| 11 | `newleavetype` | 请假类型 | `varchar2` | - | 否 | - |
| 12 | `duration` | 拆分后的时长 | `float` | - | 否 | - |
| 13 | `usedetail` | 是否启用明细 | `varchar2` | - | 否 | - |
| 14 | `durationrule` | 单位规则 | `varchar2` | - | 否 | - |
| 15 | `tablenamedb` | 表单名称 | `varchar2` | - | 否 | - |
| 16 | `fromdatedb` | 原始表单数据，开始日期 | `varchar2` | - | 否 | - |
| 17 | `fromtimedb` | 原始表单数据，开始时间 | `varchar2` | - | 否 | - |
| 18 | `todatedb` | 原始表单数据，结束日期 | `varchar2` | - | 否 | - |
| 19 | `totimedb` | 原始表单数据，结束时间 | `varchar2` | - | 否 | - |
| 20 | `durationdb` | 原始表单数据，时长 | `varchar2` | - | 否 | - |
| 21 | `status` | 暂不用 | `varchar2` | - | 否 | - |
| 22 | `belongdate` | 流程归属日期 | `varchar2` | - | 否 | - |
| 23 | `d_mins` | 对应工作时长 | `varchar2` | - | 否 | - |
| 24 | `serialid` | 对应班次 | `varchar2` | - | 否 | - |
| 25 | `subcompanyid` | 分部 | `integer` | - | 否 | - |
| 26 | `departmentid` | 部门 | `integer` | - | 否 | - |
| 27 | `jobtitle` | 岗位 | `integer` | - | 否 | - |
| 28 | `leavebackrequestid` | 被销假的请假流程会存储对应的销假流程requestid | `varchar2` | - | 否 | - |
| 29 | `companion` | 陪同人ids | `blob` | - | 否 | - |
| 30 | `iscompanion` | 是否是陪同人 | `varchar2` | - | 否 | - |
| 31 | `changetype` | 加班类型，工作日，节假日和休息日 | `varchar2` | - | 否 | - |
