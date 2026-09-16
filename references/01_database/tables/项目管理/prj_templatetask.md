# 泛微OA 数据表: `prj_templatetask`

- **中文名称**: 项目模板任务
- **所属模块**: `项目管理`
- **数据库表名**: `prj_templatetask`
- **主键**: `id`
- **字段数**: `16`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `stageid` | 阶段id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `id` | 标识id | `integer` | - | 否 | 否 | 否 | - | - | 标识列 |
| 3 | `templetid` | 模板id | `integer` | - | 是 | 否 | 否 | - | - | 模板id |
| 4 | `templettaskid` | 任务id | `integer` | - | 是 | 否 | 否 | - | - | 任务id |
| 5 | `taskname` | 名称 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 名称 |
| 6 | `taskmanager` | 任务负责人 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 任务负责人 |
| 7 | `begindate` | 开始日期 | `char` | 10 | 是 | 否 | 否 | - | - | 开始日期 |
| 8 | `budget` | 预算 | `number` | (15,3) | 是 | 否 | 否 | - | - | 预算 |
| 9 | `parenttaskid` | 上级任务 | `integer` | - | 是 | 否 | 否 | - | - | 上级任务 |
| 10 | `beftaskid` | 前置任务 | `integer` | - | 是 | 否 | 否 | - | - | 前置任务 |
| 11 | `taskdesc` | 任务说明 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | 任务说明 |
| 12 | `taskindex` | 任务排序 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 13 | `guid1` | uuid | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 14 | `enddate` | 结束日期 | `char` | 10 | 是 | 否 | 否 | - | - | 结束日期 |
| 15 | `workday` | 工期 | `integer` | - | 是 | 否 | 否 | - | - | 工期 |
| 16 | `accessory` | 附件 | `varchar2` | 2000 | 是 | 否 | 否 | - | - | 附件 |
