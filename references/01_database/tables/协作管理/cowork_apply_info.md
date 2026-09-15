# 泛微OA 数据表: `cowork_apply_info`

- **所属模块**: `协作管理`
- **数据库表名**: `cowork_apply_info`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | - |
| 2 | `coworkid` | 协作ID | `varchar2` | 4000 | 是 | - |
| 3 | `status` | 审批状态 | `varchar2` | 10 | 是 | - |
| 4 | `resourceid` | 人员ID | `varchar2` | 4000 | 是 | - |
| 5 | `applydate` | 申请日期 | `varchar2` | 20 | 是 | - |
| 6 | `approveid` | 审批人 | `varchar2` | 4000 | 是 | - |
| 7 | `approvedate` | 审批日期 | `varchar2` | 20 | 是 | - |
| 8 | `ipaddress` | IP地址 | `varchar2` | 20 | 是 | - |
