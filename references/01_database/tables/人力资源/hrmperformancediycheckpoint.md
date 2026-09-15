# 泛微OA 数据表: `hrmperformancediycheckpoint`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmperformancediycheckpoint`
- **字段总数**: `12`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `checkid` | 考核id | `integer` | - | 是 | 考核id |
| 3 | `targetname` | 名称 | `varchar2` | 800 | 是 | 名称 |
| 4 | `percent_n` | 上级名称 | `integer` | - | 是 | 上级名称 |
| 5 | `stdname` | 类型名称 | `varchar2` | 2000 | 是 | 类型名称 |
| 6 | `crmcode` | 类型编码 | `varchar2` | 400 | 是 | 类型编码 |
| 7 | `parentid` | 上级id | `integer` | - | 是 | 上级id |
| 8 | `levels` | 等级 | `integer` | - | 是 | 等级 |
| 9 | `depath` | 排序 | `varchar2` | 2000 | 是 | 排序 |
| 10 | `targetindex` | 序列号 | `varchar2` | 400 | 是 | 序列号 |
| 11 | `point` | 分值 | `number` | (10,1) | 是 | 分值 |
| 12 | `nodepointid` | HrmPerformanceNodePoint表的id | `integer` | - | 否 | HrmPerformanceNodePoint表的id |
