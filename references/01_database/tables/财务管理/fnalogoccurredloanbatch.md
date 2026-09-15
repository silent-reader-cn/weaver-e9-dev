# 泛微OA 数据表: `fnalogoccurredloanbatch`

- **所属模块**: `财务管理`
- **数据库表名**: `fnalogoccurredloanbatch`
- **字段总数**: `15`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `batchguid` | 批次uuid | `varchar2` | 400 | 是 | - |
| 3 | `tablename` | 表名 | `varchar2` | 400 | 是 | - |
| 4 | `requestid` | 流程id | `integer` | - | 是 | - |
| 5 | `workflowid` | 路径id | `integer` | - | 是 | - |
| 6 | `applicantid` | 借款人 | `integer` | - | 是 | - |
| 7 | `borrowtype` | 借款类型 | `integer` | - | 是 | - |
| 8 | `amountborrow` | 金额金额 | `number` | (18,2) | 是 | - |
| 9 | `sqltype` | sql类型 | `varchar2` | 400 | 是 | - |
| 10 | `sqlcondition1` | sql条件1 | `varchar2` | 2000 | 是 | - |
| 11 | `sqlcondition2` | sql条件2 | `varchar2` | 2000 | 是 | - |
| 12 | `sqlcondition3` | sql条件3 | `varchar2` | 2000 | 是 | - |
| 13 | `creater` | 创建人 | `integer` | - | 是 | - |
| 14 | `createdate` | 创建日期 | `varchar2` | 80 | 是 | - |
| 15 | `createtime` | 创建时间 | `varchar2` | 64 | 是 | - |
