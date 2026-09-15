# 泛微OA 数据表: `bill_fnaloanapplydetail`

- **所属模块**: `财务管理`
- **数据库表名**: `bill_fnaloanapplydetail`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主表主键 | `integer` | - | 是 | - |
| 2 | `organizationid` | 承担主体id | `integer` | - | 是 | - |
| 3 | `relatedprj` | 相关项目 | `integer` | - | 是 | - |
| 4 | `relatedcrm` | 相关客户 | `integer` | - | 是 | - |
| 5 | `description` | 说明 | `varchar2` | 800 | 是 | - |
| 6 | `amount` | 金额 | `number` | (15,3) | 是 | - |
| 7 | `organizationtype` | 承担主体类型 | `integer` | - | 是 | - |
| 8 | `dsporder` | 排序id | `integer` | - | 是 | - |
