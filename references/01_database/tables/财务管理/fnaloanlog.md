# 泛微OA 数据表: `fnaloanlog`

- **所属模块**: `财务管理`
- **数据库表名**: `fnaloanlog`
- **字段总数**: `14`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `loantypeid` | 还款方式 | `integer` | - | 是 | - |
| 3 | `resourceid` | 还款人 | `integer` | - | 是 | - |
| 4 | `departmentid` | 部门id | `integer` | - | 是 | - |
| 5 | `crmid` | 相关客户 | `integer` | - | 是 | - |
| 6 | `projectid` | 相关项目 | `integer` | - | 是 | - |
| 7 | `amount` | 借款还款金额 | `number` | (10,3) | 是 | - |
| 8 | `description` | 说明 | `varchar2` | 4000 | 是 | - |
| 9 | `credenceno` | 凭证号 | `varchar2` | 480 | 是 | - |
| 10 | `occurdate` | 费用日期 | `char` | 10 | 是 | - |
| 11 | `returndate` | 还款日期 | `char` | 10 | 是 | - |
| 12 | `releatedid` | 作废 | `integer` | - | 是 | - |
| 13 | `releatedname` | 作废 | `varchar2` | 1000 | 是 | - |
| 14 | `dealuser` | 作废 | `integer` | - | 是 | - |
