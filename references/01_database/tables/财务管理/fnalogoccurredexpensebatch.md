# 泛微OA 数据表: `fnalogoccurredexpensebatch`

- **所属模块**: `财务管理`
- **数据库表名**: `fnalogoccurredexpensebatch`
- **字段总数**: `18`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `batchguid` | 导入批次guid | `varchar2` | 400 | 是 | - |
| 3 | `tablename` | 表名 | `varchar2` | 400 | 是 | - |
| 4 | `organizationid` | 承担主体id | `integer` | - | 是 | - |
| 5 | `organizationtype` | 承担主体类型 | `integer` | - | 是 | - |
| 6 | `occurdate` | 费用日期 | `varchar2` | 80 | 是 | - |
| 7 | `amount` | 金额 | `number` | (18,2) | 是 | - |
| 8 | `subject` | 科目 | `integer` | - | 是 | - |
| 9 | `status` | 费用状态 | `integer` | - | 是 | - |
| 10 | `type` | 类型 | `integer` | - | 是 | - |
| 11 | `requestid` | 流程id | `integer` | - | 是 | - |
| 12 | `sqltype` | sql类型 | `varchar2` | 400 | 是 | - |
| 13 | `sqlcondition1` | sql条件1 | `varchar2` | 2000 | 是 | - |
| 14 | `sqlcondition2` | sql条件2 | `varchar2` | 2000 | 是 | - |
| 15 | `sqlcondition3` | sql条件3 | `varchar2` | 2000 | 是 | - |
| 16 | `creater` | 操作人id | `integer` | - | 是 | - |
| 17 | `createdate` | 操作日期 | `varchar2` | 80 | 是 | - |
| 18 | `createtime` | 操作时间 | `varchar2` | 64 | 是 | - |
