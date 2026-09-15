# 泛微OA 数据表: `KQ_ATT_VACATION`

- **所属模块**: `E9新版考勤表结构`
- **数据库表名**: `KQ_ATT_VACATION`
- **字段总数**: `14`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键id | `integer` | - | 否 | - |
| 2 | `requestid` | requestid | `integer` | - | 否 | - |
| 3 | `dataid` | 主表的话对应的id | `integer` | - | 否 | - |
| 4 | `detailid` | 明细表的话对应的id | `integer` | - | 否 | - |
| 5 | `workflowid` | workflowid | `integer` | - | 否 | - |
| 6 | `resourceid` | 人员id | `integer` | - | 否 | - |
| 7 | `fromdate` | 拆分的请假开始日期 | `varchar2` | - | 否 | - |
| 8 | `fromtime` | 拆分的请假开始时间 | `varchar2` | - | 否 | - |
| 9 | `todate` | 拆分的请假结束日期 | `varchar2` | - | 否 | - |
| 10 | `totime` | 拆分的请假结束时间 | `varchar2` | - | 否 | - |
| 11 | `duration` | 冻结的时长 | `varchar2` | - | 否 | - |
| 12 | `newleavetype` | 请假类型 | `integer` | - | 否 | - |
| 13 | `durationrule` | 单位，半天，天还是小时 | `integer` | - | 否 | - |
| 14 | `status` | 0扣减，1冻结，2释放 | `integer` | - | 否 | - |
