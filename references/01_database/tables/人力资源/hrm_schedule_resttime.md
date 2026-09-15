# 泛微OA 数据表: `hrm_schedule_resttime`

- **所属模块**: `人力资源`
- **数据库表名**: `hrm_schedule_resttime`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `number` | (22,0) | 否 | ID |
| 2 | `worktimeid` | 工作时间id | `number` | (22,0) | 是 | 工作时间id |
| 3 | `delflag` | 删除标志 | `number` | (22,0) | 是 | 删除标志 |
| 4 | `reststarttime` | 休息开始时间 | `varchar2` | 50 | 是 | 休息开始时间 |
| 5 | `restendtime` | 休息结束时间 | `varchar2` | 50 | 是 | 休息结束时间 |
| 6 | `reststarttime1` | 休息开始时间1 | `varchar2` | 8 | 是 | 休息开始时间1 |
| 7 | `restendtime1` | 休息结束时间1 | `varchar2` | 8 | 是 | 休息结束时间1 |
| 8 | `reststarttime2` | 休息开始时间2 | `varchar2` | 8 | 是 | 休息开始时间2 |
| 9 | `restendtime2` | 休息结束时间2 | `varchar2` | 8 | 是 | 休息结束时间2 |
