# 泛微OA 数据表: `crm_contract`

- **所属模块**: `客户管理`
- **数据库表名**: `crm_contract`
- **字段总数**: `21`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | id |
| 2 | `name` | 合同名称 | `varchar2` | 1000 | 是 | 合同名称 |
| 3 | `typeid` | 合同性质 | `integer` | - | 是 | 合同性质 |
| 4 | `docid` | 合同正本 | `varchar2` | 1000 | 是 | 文档ID |
| 5 | `price` | 合同金额 | `number` | (17,2) | 是 | 合同金额 |
| 6 | `crmid` | 相关客户 | `integer` | - | 是 | 相关客户 |
| 7 | `contacterid` | 联系人 | `integer` | - | 是 | 联系人 |
| 8 | `startdate` | 开始时间 | `char` | 10 | 是 | 开始时间 |
| 9 | `enddate` | 结束时间 | `char` | 10 | 是 | 结束时间 |
| 10 | `manager` | 负责人 | `integer` | - | 是 | 负责人 |
| 11 | `status` | 合同状态 | `integer` | - | 是 | -1：待审批；0：提交；1：已审批；2：签单；3：执行完成。 |
| 12 | `isremind` | 是否提醒 | `integer` | - | 是 | 是否提醒 |
| 13 | `remindday` | 提醒时间 | `integer` | - | 是 | 提醒时间 |
| 14 | `creater` | 创建人 | `integer` | - | 是 | 创建人 |
| 15 | `createdate` | 创建日期 | `char` | 10 | 是 | 创建日期 |
| 16 | `createtime` | 创建时间 | `char` | 10 | 是 | 创建时间 |
| 17 | `projid` | 相关项目 | `integer` | - | 是 | 相关项目 |
| 18 | `department` | 部门 | `integer` | - | 是 | 部门 |
| 19 | `subcompanyid1` | 分部 | `integer` | - | 是 | 分部 |
| 20 | `sellchanceid` | 商机id | `integer` | - | 是 | 商机id |
| 21 | `deleted` | 是否删除 | `integer` | - | 是 | 1：删除 |
