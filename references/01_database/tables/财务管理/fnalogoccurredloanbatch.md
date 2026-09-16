# 泛微OA 数据表: `fnalogoccurredloanbatch`

- **中文名称**: 已发生借款导入日志表
- **所属模块**: `财务管理`
- **数据库表名**: `fnalogoccurredloanbatch`
- **主键**: `id`
- **字段数**: `15`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `batchguid` | 批次uuid | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 3 | `tablename` | 表名 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 4 | `requestid` | 流程id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `workflowid` | 路径id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `applicantid` | 借款人 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `borrowtype` | 借款类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `amountborrow` | 金额金额 | `number` | (18,2) | 是 | 否 | 否 | - | - | - |
| 9 | `sqltype` | sql类型 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 10 | `sqlcondition1` | sql条件1 | `varchar2` | 2000 | 是 | 否 | 否 | - | - | - |
| 11 | `sqlcondition2` | sql条件2 | `varchar2` | 2000 | 是 | 否 | 否 | - | - | - |
| 12 | `sqlcondition3` | sql条件3 | `varchar2` | 2000 | 是 | 否 | 否 | - | - | - |
| 13 | `creater` | 创建人 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 14 | `createdate` | 创建日期 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 15 | `createtime` | 创建时间 | `varchar2` | 64 | 是 | 否 | 否 | - | - | - |
