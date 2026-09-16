# 泛微OA 数据表: `hrmperformancediycheckpoint`

- **中文名称**: 人力资源综合素质考核表
- **所属模块**: `人力资源`
- **数据库表名**: `hrmperformancediycheckpoint`
- **主键**: `id`
- **字段数**: `12`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 是 | - | - | ID |
| 2 | `checkid` | 考核id | `integer` | - | 是 | 否 | 否 | - | 0 | 考核id |
| 3 | `targetname` | 名称 | `varchar2` | 800 | 是 | 否 | 否 | - | - | 名称 |
| 4 | `percent_n` | 上级名称 | `integer` | - | 是 | 否 | 否 | - | 0 | 上级名称 |
| 5 | `stdname` | 类型名称 | `varchar2` | 2000 | 是 | 否 | 否 | - | - | 类型名称 |
| 6 | `crmcode` | 类型编码 | `varchar2` | 400 | 是 | 否 | 否 | - | - | 类型编码 |
| 7 | `parentid` | 上级id | `integer` | - | 是 | 否 | 否 | - | 0 | 上级id |
| 8 | `levels` | 等级 | `integer` | - | 是 | 否 | 否 | - | 0 | 等级 |
| 9 | `depath` | 排序 | `varchar2` | 2000 | 是 | 否 | 否 | - | - | 排序 |
| 10 | `targetindex` | 序列号 | `varchar2` | 400 | 是 | 否 | 否 | - | - | 序列号 |
| 11 | `point` | 分值 | `number` | (10,1) | 是 | 否 | 否 | - | - | 分值 |
| 12 | `nodepointid` | HrmPerformanceNodePoint表的id | `integer` | - | 否 | 是 | 否 | - | - | HrmPerformanceNodePoint表的id |
