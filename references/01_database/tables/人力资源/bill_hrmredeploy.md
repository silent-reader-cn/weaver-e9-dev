# 泛微OA 数据表: `bill_hrmredeploy`

- **中文名称**: 工作流单据表（职位调动）
- **所属模块**: `人力资源`
- **数据库表名**: `bill_hrmredeploy`
- **主键**: `id`
- **字段数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `resource_n` | 申请人 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `redeploydate` | 调动日期 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 4 | `oldjob` | 原岗位 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `newjob` | 新岗位 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `oldjoblevel` | 原职级 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `newjoblevel` | 现职级 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `redeployreason` | 调动原因 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 9 | `ischangesalary` | 是否重新设置基准工资 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 10 | `requestid` | 工作流请求的ID | `integer` | - | 是 | 否 | 否 | - | - | 对应表workflow_requestbase中的字段requestid |
| 11 | `manager` | 经理 | `integer` | - | 是 | 否 | 否 | - | - | - |
