# 泛微OA 数据表: `fnaloaninfo`

- **中文名称**: 借款信息表
- **所属模块**: `财务管理`
- **数据库表名**: `fnaloaninfo`
- **主键**: `id`
- **字段数**: `12`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | 主键 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `loantype` | 来源 | `integer` | - | 是 | 否 | 否 | - | - | 1：借款单；2：冲销借款；3：财务销账； |
| 3 | `organizationid` | 组织id | `integer` | - | 是 | 否 | 否 | - | - | 分部id；部门id；个人id；成本中心id； |
| 4 | `organizationtype` | 组织类型 | `integer` | - | 是 | 否 | 否 | - | - | 0：总部； 1：分部； 2：部门； 18004：成本中心； |
| 5 | `occurdate` | 发生日期 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 6 | `amount` | 金额 | `number` | (15,3) | 是 | 否 | 否 | - | - | 可以有负值， 负值就为冲销借款 |
| 7 | `debitremark` | 凭证号 | `varchar2` | 480 | 是 | 否 | 否 | - | - | - |
| 8 | `remark` | 备注 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 9 | `requestid` | 流程requestid | `integer` | - | 是 | 否 | 否 | - | - | 关联流程requestid |
| 10 | `relatedcrm` | 科目id | `integer` | - | 是 | 否 | 否 | - | - | 相关科目 |
| 11 | `relatedprj` | 项目id | `integer` | - | 是 | 否 | 否 | - | - | 相关项目 |
| 12 | `processorid` | 经办人id | `integer` | - | 是 | 否 | 否 | - | - | - |
