# 泛微OA 数据表: `hrm_compensationtargetset`

- **所属模块**: `人力资源`
- **数据库表名**: `hrm_compensationtargetset`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `subcompanyid` | 分部id | `integer` | - | 是 | 分部id |
| 3 | `targetname` | 简称 | `varchar2` | 400 | 是 | 简称 |
| 4 | `explain` | 说明 | `varchar2` | 800 | 是 | 说明 |
| 5 | `areatype` | 应用范围类型 | `integer` | - | 是 | - |
