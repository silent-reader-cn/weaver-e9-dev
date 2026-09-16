# 泛微OA 数据表: `bill_approvecustomer`

- **中文名称**: 客户审批流转单
- **所属模块**: `客户管理`
- **数据库表名**: `bill_approvecustomer`
- **主键**: `id`
- **字段数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `managerid` | 客户经理id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `requestid` | 工作流请求的ID | `integer` | - | 是 | 否 | 否 | - | - | 对应表workflow_requestbase中的字段requestid |
| 4 | `approveid` | 被审批客户的的id | `integer` | - | 是 | 否 | 否 | - | - | crmId.对应表CRM_CustomerInfo的id |
| 5 | `approvevalue` | 申请的客户等级 | `integer` | - | 是 | 否 | 否 | - | - | 两种情况，情况A、 (approvetype=1),1、无效客户；2、基础客户；3、潜在客户；4、成功客户； 情况B、(approvetype=2),2、门户申请；3、门户冻结 |
| 6 | `approvedesc` | 申请描述 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 公司名称+申请状态 |
| 7 | `status` | 审批状态 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 8 | `approvetype` | 审批类型 | `integer` | - | 是 | 否 | 否 | - | - | 1、客户状态变更；2、门户状态变更 |
| 9 | `customertype` | 客户类型 | `integer` | - | 否 | 否 | 否 | - | - | 客户类型（用于配置流程出口条件） |
