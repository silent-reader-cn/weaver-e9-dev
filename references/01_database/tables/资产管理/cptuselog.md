# 泛微OA 数据表: `cptuselog`

- **所属模块**: `资产管理`
- **数据库表名**: `cptuselog`
- **字段总数**: `15`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 标识id | `integer` | - | 否 | 标识列 |
| 2 | `capitalid` | 资产id | `integer` | - | 是 | 资产id |
| 3 | `usedate` | 流转日期 | `char` | 10 | 是 | 流转日期 |
| 4 | `usedeptid` | 流转部门 | `integer` | - | 是 | 流转部门 |
| 5 | `useresourceid` | 流转人员 | `integer` | - | 是 | 流转人员 |
| 6 | `usecount` | 流转数量 | `number` | (18,2) | 是 | 流转数量 |
| 7 | `useaddress` | 流转地点 | `varchar2` | 1000 | 是 | 流转地点 |
| 8 | `userequest` | 流转流程 | `integer` | - | 是 | 流转流程 |
| 9 | `maintaincompany` | 备用字段 | `varchar2` | 800 | 是 | 备用字段 |
| 10 | `usestatus` | 流转状态 | `integer` | - | 是 | 流转状态 |
| 11 | `remark` | 备注 | `varchar2` | 4000 | 是 | 备注 |
| 12 | `olddeptid` | 原始部门 | `integer` | - | 是 | 原始部门 |
| 13 | `fee` | 流转费用 | `number` | (15,2) | 是 | 流转费用 |
| 14 | `resourceid` | 人力资源 | `varchar2` | 480 | 是 | 人力资源 |
| 15 | `mendperioddate` | 维修期限 | `varchar2` | 480 | 是 | 维修期限 |
