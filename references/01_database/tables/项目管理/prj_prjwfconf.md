# 泛微OA 数据表: `prj_prjwfconf`

- **所属模块**: `项目管理`
- **数据库表名**: `prj_prjwfconf`
- **字段总数**: `25`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 标识id | `integer` | - | 否 | 标识列 |
| 2 | `wftype` | 流程类型 | `integer` | - | 是 | 流程类型 |
| 3 | `wfid` | 流程id | `integer` | - | 是 | 流程id |
| 4 | `formid` | 表单id | `integer` | - | 是 | 表单id |
| 5 | `prjtype` | 项目类型 | `integer` | - | 是 | 项目类型 |
| 6 | `isopen` | 是否启用 | `char` | 1 | 是 | 是否启用 |
| 7 | `isasync` | 是否异步触发action | `integer` | - | 是 | 是否异步触发action (该字段预留,目前未开放) |
| 8 | `actname` | action名字 | `varchar2` | 1000 | 是 | action名字 |
| 9 | `creater` | 创建者 | `integer` | - | 是 | 创建者 |
| 10 | `createdate` | 创建日期 | `char` | 10 | 是 | 创建日期 |
| 11 | `createtime` | 创建时间 | `char` | 8 | 是 | 创建时间 |
| 12 | `lastmoddate` | 修改日期 | `char` | 10 | 是 | 修改日期 |
| 13 | `lastmodtime` | 修改时间 | `char` | 8 | 是 | 修改时间 |
| 14 | `xmjl` | 项目经理 | `integer` | - | 是 | 项目经理 |
| 15 | `xgxm` | 相关项目 | `integer` | - | 是 | 相关项目 |
| 16 | `xmmb` | 项目模板 | `integer` | - | 是 | 项目模板 |
| 17 | `cus1` | 预留字段1 | `integer` | - | 是 | 预留字段1 |
| 18 | `cus2` | 预留字段2 | `integer` | - | 是 | 预留字段2 |
| 19 | `cus3` | 预留字段3 | `integer` | - | 是 | 预留字段3 |
| 20 | `cus4` | 预留字段4 | `integer` | - | 是 | 预留字段4 |
| 21 | `cus5` | 预留字段5 | `integer` | - | 是 | 预留字段5 |
| 22 | `cus6` | 预留字段6 | `integer` | - | 是 | 预留字段6 |
| 23 | `cus7` | 预留字段7 | `integer` | - | 是 | 预留字段7 |
| 24 | `cus8` | 预留字段8 | `integer` | - | 是 | 预留字段8 |
| 25 | `guid1` | uuid标识号 | `char` | 36 | 是 | uuid标识号 |
