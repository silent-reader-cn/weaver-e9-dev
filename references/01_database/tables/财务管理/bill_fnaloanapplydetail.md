# 泛微OA 数据表: `bill_fnaloanapplydetail`

- **中文名称**: 借款申请单明细表
- **所属模块**: `财务管理`
- **数据库表名**: `bill_fnaloanapplydetail`
- **主键**: `id+dsporder`
- **字段数**: `8`

> 说明：借款申请单

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | 主表主键 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `organizationid` | 承担主体id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `relatedprj` | 相关项目 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `relatedcrm` | 相关客户 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `description` | 说明 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 6 | `amount` | 金额 | `number` | (15,3) | 是 | 否 | 否 | - | - | - |
| 7 | `organizationtype` | 承担主体类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `dsporder` | 排序id | `integer` | - | 是 | 否 | 否 | - | - | - |
