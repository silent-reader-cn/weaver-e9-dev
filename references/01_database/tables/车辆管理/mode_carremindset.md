# 泛微OA 数据表: `mode_carremindset`

- **所属模块**: `车辆管理`
- **数据库表名**: `mode_carremindset`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `timerangeend` | 显示时间段结束 | `integer` | - | 是 | - |
| 2 | `timerangestart` | 显示时间段开始 | `integer` | - | 是 | - |
| 3 | `dspunit` | 最小占用显示单位 | `integer` | - | 是 | - |
| 4 | `usedcolor` | 占用颜色 | `varchar2` | 80 | 是 | - |
| 5 | `conflictedcolor` | 冲突颜色 | `varchar2` | 80 | 是 | - |
| 6 | `id` | id | `integer` | - | 否 | - |
| 7 | `isremind` | 主表id | `integer` | - | 是 | - |
| 8 | `remindtype` | 当前自定义表字段 | `integer` | - | 是 | - |
