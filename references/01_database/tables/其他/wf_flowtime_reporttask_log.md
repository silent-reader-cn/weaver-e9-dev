# 泛微OA 数据表: `wf_flowtime_reporttask_log`

- **所属模块**: `其他`
- **数据库表名**: `wf_flowtime_reporttask_log`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `taskstatus` | 耗时计算任务状态 | `char` | 1 | 是 | 0：计算中 1：任务计算成功 |
| 3 | `startdate` | 任务开始时间 | `varchar2` | 80 | 是 | - |
| 4 | `enddate` | 任务结束日期 | `varchar2` | 80 | 是 | - |
| 5 | `taskstarttime` | 任务开始时间 | `varchar2` | 160 | 是 | - |
| 6 | `taskendtime` | 任务结束时间 | `varchar2` | 160 | 是 | - |
| 7 | `exception` | 异常说明 | `varchar2` | 1000 | 是 | - |
