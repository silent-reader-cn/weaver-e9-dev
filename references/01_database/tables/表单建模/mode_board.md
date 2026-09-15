# 泛微OA 数据表: `mode_board`

- **所属模块**: `表单建模`
- **数据库表名**: `mode_board`
- **字段总数**: `15`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `grouptype` | 分组类型 | `varchar2` | 1 | 是 | - |
| 2 | `id` | id | `integer` | - | 否 | - |
| 3 | `name` | 看板名称 | `varchar2` | 1000 | 是 | - |
| 4 | `appid` | 所属应用 | `integer` | - | 是 | - |
| 5 | `customid` | 查询 | `integer` | - | 是 | - |
| 6 | `reffield` | 数据关联字段 | `integer` | - | 是 | - |
| 7 | `reftypefield` | 关联字段类型 | `integer` | - | 是 | - |
| 8 | `titlefield` | 标题字段 | `integer` | - | 是 | - |
| 9 | `principalfield` | 负责人字段 | `integer` | - | 是 | - |
| 10 | `enddatefield` | 截止日期字段 | `varchar2` | 10 | 是 | - |
| 11 | `progressfield` | 进度 | `varchar2` | 100 | 是 | - |
| 12 | `statusfield` | 状态字段 | `integer` | - | 是 | - |
| 13 | `statusvalues` | 状态值 | `clob` | 4000 | 是 | - |
| 14 | `managerfield` | 上级字段 | `integer` | - | 是 | - |
| 15 | `uuid` | uuid | `varchar2` | 100 | 是 | - |
