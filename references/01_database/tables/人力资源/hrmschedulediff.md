# 泛微OA 数据表: `hrmschedulediff`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmschedulediff`
- **字段总数**: `15`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `diffname` | 考勤种类名称 | `varchar2` | 480 | 是 | 考勤种类名称 |
| 3 | `diffdesc` | 考勤种类描述 | `varchar2` | 1000 | 是 | 考勤种类描述 |
| 4 | `difftype` | 非一致种类 | `char` | 1 | 是 | 0:增加，1:减少 |
| 5 | `difftime` | 非一致时间种类 | `char` | 1 | 是 | 0:工作时间，1:休息日，2:公众假日 |
| 6 | `mindifftime` | 最小计算时间 | `integer` | - | 是 | 最小计算时间 |
| 7 | `workflowid` | 相关工作流id | `integer` | - | 是 | 相关工作流id |
| 8 | `salaryable` | 是否计算薪资 | `char` | 1 | 是 | 0:否，1:是 |
| 9 | `counttype` | 计算方式 | `char` | 1 | 是 | 0:倍数，1:固定 |
| 10 | `countnum` | 计算和 | `number` | (10,2) | 是 | 计算和 |
| 11 | `diffremark` | 备注 | `varchar2` | 4000 | 是 | 备注 |
| 12 | `salaryitem` | 相关工资项目 | `integer` | - | 是 | 相关工资项目 |
| 13 | `color` | 颜色 | `varchar2` | 240 | 是 | 颜色 |
| 14 | `diffscope` | 应用范围 | `integer` | - | 是 | 应用范围 |
| 15 | `subcompanyid` | 所属分部 | `integer` | - | 是 | 所属分部 |
