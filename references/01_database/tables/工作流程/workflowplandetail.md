# 泛微OA 数据表: `workflowplandetail`

- **所属模块**: `工作流程`
- **数据库表名**: `workflowplandetail`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `userid` | 用户id | `integer` | - | 是 | - |
| 3 | `autotype` | 触发频率 | `char` | 1 | 是 | 0：周，1：月，2：季度，3：年 |
| 4 | `flowdate` | 触发时间 | `varchar2` | 80 | 是 | 对应的年+月（周） |
| 5 | `flowid` | 流程id | `integer` | - | 是 | - |
| 6 | `usertype` | 用户类型 | `char` | 1 | 是 | 1：普通用户，2：客户 |
