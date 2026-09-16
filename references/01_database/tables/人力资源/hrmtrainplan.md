# 泛微OA 数据表: `hrmtrainplan`

- **中文名称**: 人力资源培训安排信息表
- **所属模块**: `人力资源`
- **数据库表名**: `hrmtrainplan`
- **主键**: `id`
- **字段数**: `17`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 是 | - | - | ID |
| 2 | `planname` | 名称 | `varchar2` | 480 | 是 | 否 | 否 | - | - | 名称 |
| 3 | `layoutid` | 培训规划id | `integer` | - | 是 | 否 | 否 | - | - | 培训规划id |
| 4 | `planorganizer` | 培训安排组织人 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 培训安排组织人 |
| 5 | `planstartdate` | 开始时间 | `char` | 10 | 是 | 否 | 否 | - | - | 开始时间 |
| 6 | `planenddate` | 结束时间 | `char` | 10 | 是 | 否 | 否 | - | - | 结束时间 |
| 7 | `plancontent` | 内容 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | 内容 |
| 8 | `planaim` | 目标 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | 目标 |
| 9 | `planaddress` | 地址 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 地址 |
| 10 | `planresource` | 组织人id | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 组织人id |
| 11 | `planactor` | 参与人 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | 参与人 |
| 12 | `planbudget` | 预算 | `float` | 22 | 是 | 否 | 否 | - | - | 预算 |
| 13 | `planbudgettype` | 预算类型 | `varchar2` | 32 | 是 | 否 | 否 | - | - | 预算类型 |
| 14 | `openrange` | 公开范围 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 公开范围 |
| 15 | `createrid` | 创建人id | `integer` | - | 是 | 否 | 否 | - | - | 创建人id |
| 16 | `createdate` | 创建日期 | `char` | 10 | 是 | 否 | 否 | - | - | 创建日期 |
| 17 | `traindocs` | 文档id | `varchar2` | 2000 | 是 | 否 | 否 | - | - | 文档id |
