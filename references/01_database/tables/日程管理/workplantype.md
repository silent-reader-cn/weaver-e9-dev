# 泛微OA 数据表: `workplantype`

- **中文名称**: 日程类型
- **所属模块**: `日程管理`
- **数据库表名**: `workplantype`
- **主键**: `workplantypeid`
- **字段数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `workplantypeid` | 日程类型id | `integer` | - | 否 | 否 | 是 | - | - | 日程类型id |
| 2 | `workplantypename` | 日程类型名称 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 日程类型名称 |
| 3 | `workplantypeattribute` | 日程类型属性 | `integer` | - | 是 | 否 | 否 | - | - | 0：自定义日程类型；6：系统日程类型 |
| 4 | `workplantypecolor` | 颜色 | `char` | 7 | 是 | 否 | 否 | - | - | 颜色 |
| 5 | `available` | 启用标识 | `char` | 1 | 是 | 否 | 否 | - | - | 0：不启用，1：启用 |
| 6 | `displayorder` | 显示顺序 | `integer` | - | 是 | 否 | 否 | - | - | 显示顺序 |
