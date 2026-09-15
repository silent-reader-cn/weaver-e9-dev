# 泛微OA 数据表: `hrmtrainplan`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmtrainplan`
- **字段总数**: `17`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `planname` | 名称 | `varchar2` | 480 | 是 | 名称 |
| 3 | `layoutid` | 培训规划id | `integer` | - | 是 | 培训规划id |
| 4 | `planorganizer` | 培训安排组织人 | `varchar2` | 1000 | 是 | 培训安排组织人 |
| 5 | `planstartdate` | 开始时间 | `char` | 10 | 是 | 开始时间 |
| 6 | `planenddate` | 结束时间 | `char` | 10 | 是 | 结束时间 |
| 7 | `plancontent` | 内容 | `varchar2` | 4000 | 是 | 内容 |
| 8 | `planaim` | 目标 | `varchar2` | 4000 | 是 | 目标 |
| 9 | `planaddress` | 地址 | `varchar2` | 1000 | 是 | 地址 |
| 10 | `planresource` | 组织人id | `varchar2` | 1000 | 是 | 组织人id |
| 11 | `planactor` | 参与人 | `varchar2` | 4000 | 是 | 参与人 |
| 12 | `planbudget` | 预算 | `float` | 22 | 是 | 预算 |
| 13 | `planbudgettype` | 预算类型 | `varchar2` | 32 | 是 | 预算类型 |
| 14 | `openrange` | 公开范围 | `varchar2` | 1000 | 是 | 公开范围 |
| 15 | `createrid` | 创建人id | `integer` | - | 是 | 创建人id |
| 16 | `createdate` | 创建日期 | `char` | 10 | 是 | 创建日期 |
| 17 | `traindocs` | 文档id | `varchar2` | 2000 | 是 | 文档id |
