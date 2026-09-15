# 泛微OA 数据表: `hrm_att_vacation`

- **所属模块**: `人力资源`
- **数据库表名**: `hrm_att_vacation`
- **字段总数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `field001` | 请求id | `integer` | - | 否 | requestid |
| 3 | `field002` | 流程id | `integer` | - | 否 | workflowid |
| 4 | `field003` | 人员id | `integer` | - | 否 | resourceid |
| 5 | `field004` | 请假开始日期 | `varchar2` | 800 | 否 | fromdate |
| 6 | `field005` | 请假开始时间 | `varchar2` | 800 | 否 | fromtime |
| 7 | `field006` | 请假结束日期 | `varchar2` | 800 | 否 | todate |
| 8 | `field007` | 请假结束时间 | `varchar2` | 800 | 否 | totime |
| 9 | `field008` | 请假天数 | `varchar2` | 800 | 否 | leavedays |
| 10 | `field009` | 请假类型 | `integer` | - | 否 | leavetype |
| 11 | `field010` | 假期状态 | `integer` | - | 否 | status(0-抵扣  1-冻结  2-释放) |
