# 泛微OA 数据表: `bill_hrmredeploy`

- **所属模块**: `人力资源`
- **数据库表名**: `bill_hrmredeploy`
- **字段总数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `resource_n` | 申请人 | `integer` | - | 是 | - |
| 3 | `redeploydate` | 调动日期 | `char` | 10 | 是 | - |
| 4 | `oldjob` | 原岗位 | `integer` | - | 是 | - |
| 5 | `newjob` | 新岗位 | `integer` | - | 是 | - |
| 6 | `oldjoblevel` | 原职级 | `integer` | - | 是 | - |
| 7 | `newjoblevel` | 现职级 | `integer` | - | 是 | - |
| 8 | `redeployreason` | 调动原因 | `varchar2` | 1000 | 是 | - |
| 9 | `ischangesalary` | 是否重新设置基准工资 | `integer` | - | 是 | - |
| 10 | `requestid` | 工作流请求的ID | `integer` | - | 是 | 对应表workflow_requestbase中的字段requestid |
| 11 | `manager` | 经理 | `integer` | - | 是 | - |
