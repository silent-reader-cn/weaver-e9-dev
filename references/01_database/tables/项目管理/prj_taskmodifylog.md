# 泛微OA 数据表: `prj_taskmodifylog`

- **所属模块**: `项目管理`
- **数据库表名**: `prj_taskmodifylog`
- **字段总数**: `20`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 标识id | `integer` | - | 否 | 标识列 |
| 2 | `projid` | 项目id | `integer` | - | 否 | 项目id |
| 3 | `taskid` | 任务id | `integer` | - | 否 | 任务id |
| 4 | `subject` | 标题 | `varchar2` | 800 | 否 | 标题 |
| 5 | `hrmid` | 负责人 | `varchar2` | 1000 | 是 | 负责人 |
| 6 | `begindate` | 开始日期 | `varchar2` | 80 | 是 | 开始日期 |
| 7 | `enddate` | 结束日期 | `varchar2` | 80 | 是 | 结束日期 |
| 8 | `workday` | 工期 | `integer` | - | 否 | 工期 |
| 9 | `finish` | 进度 | `integer` | - | 否 | 进度 |
| 10 | `parentid` | 上级任务 | `integer` | - | 否 | 上级任务 |
| 11 | `prefinish` | 前置任务 | `varchar2` | 4000 | 是 | 前置任务 |
| 12 | `islandmark` | 里程碑 | `char` | 1 | 否 | 里程碑 |
| 13 | `modifydate` | 修改日期 | `varchar2` | 80 | 否 | 修改日期 |
| 14 | `modifytime` | 修改时间 | `varchar2` | 64 | 否 | 修改时间 |
| 15 | `modifyby` | 修改者 | `integer` | - | 否 | 修改者 |
| 16 | `status` | 状态 | `integer` | - | 否 | 状态 |
| 17 | `operationtype` | 操作类型 | `integer` | - | 否 | 操作类型 |
| 18 | `clientip` | 客户端ip | `varchar2` | 160 | 否 | 客户端ip |
| 19 | `realmandays` | 实际工期 | `number` | (6,1) | 是 | 实际工期 |
| 20 | `fixedcost` | 预算 | `number` | (18,2) | 是 | 预算 |
