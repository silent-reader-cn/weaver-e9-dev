# 泛微OA 数据表: `hrmperformancealertcheck`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmperformancealertcheck`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `alertname` | 提醒流程名称 | `varchar2` | 1000 | 是 | 提醒流程名称 |
| 3 | `cycle` | 提醒周期 | `char` | 1 | 是 | 多久提醒一次 |
| 4 | `performancedate` | 时间 | `varchar2` | 1000 | 是 | 时间 |
| 5 | `performancetype` | 提醒类型 | `char` | 1 | 是 | (计划，目标等） |
| 6 | `objid` | 对象id | `integer` | - | 是 | 对象id |
| 7 | `alerttype` | 用户类型 | `char` | 1 | 是 | （个人，部门,集团,分部） |
