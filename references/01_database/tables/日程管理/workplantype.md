# 泛微OA 数据表: `workplantype`

- **所属模块**: `日程管理`
- **数据库表名**: `workplantype`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `workplantypeid` | 日程类型id | `integer` | - | 否 | 日程类型id |
| 2 | `workplantypename` | 日程类型名称 | `varchar2` | 1000 | 是 | 日程类型名称 |
| 3 | `workplantypeattribute` | 日程类型属性 | `integer` | - | 是 | 0：自定义日程类型；6：系统日程类型 |
| 4 | `workplantypecolor` | 颜色 | `char` | 7 | 是 | 颜色 |
| 5 | `available` | 启用标识 | `char` | 1 | 是 | 0：不启用，1：启用 |
| 6 | `displayorder` | 显示顺序 | `integer` | - | 是 | 显示顺序 |
