# 泛微OA 数据表: `hrmscheduleapplication`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmscheduleapplication`
- **字段总数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `onedayworkhours` | 一天工作时间 | `varchar2` | 800 | 是 | 一天工作时间 |
| 2 | `id` | ID | `integer` | - | 否 | ID |
| 3 | `unit` | 单位 | `integer` | - | 是 | 0:无限制，1:半天，2：全天 |
| 4 | `type` | 类型 | `integer` | - | 是 | 类型 |
