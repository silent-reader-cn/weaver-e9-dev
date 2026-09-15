# 泛微OA 数据表: `WorkPlanWeekList_Group`

- **所属模块**: `日程管理`
- **数据库表名**: `WorkPlanWeekList_Group`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | - | 主键 |
| 2 | `name` | 数据范围名称 | `varchar2` | 1000 | - | 数据范围名称 |
| 3 | `groupvalue` | 数据范围人员ids | `clob` | - | - | 数据范围人员ids |
| 4 | `workplantype` | 日程类型ids | `varchar2` | 2000 | - | 日程类型ids |
| 5 | `haslimit` | 是否有权限设置 | `integer` | - | - | 1：有权限设置 |
| 6 | `displayorder` | 显示顺序 | `integer` | - | - | 升序 |
