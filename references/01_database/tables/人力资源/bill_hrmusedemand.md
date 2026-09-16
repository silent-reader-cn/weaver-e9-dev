# 泛微OA 数据表: `bill_hrmusedemand`

- **中文名称**: 表单_人力资源用工需求表
- **所属模块**: `人力资源`
- **数据库表名**: `bill_hrmusedemand`
- **主键**: `id`
- **字段数**: `15`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 是 | - | - | ID |
| 2 | `resource_n` | 人员id | `integer` | - | 是 | 否 | 否 | - | - | 人员id |
| 3 | `demandjobtitle` | 岗位 | `integer` | - | 是 | 否 | 否 | - | - | 岗位 |
| 4 | `demandnum` | 数量 | `integer` | - | 是 | 否 | 否 | - | - | 数量 |
| 5 | `demandkind` | 用工性质 | `integer` | - | 是 | 否 | 否 | - | - | 用工性质 |
| 6 | `leastedulevel` | 最低学历 | `integer` | - | 是 | 否 | 否 | - | - | 最低学历 |
| 7 | `demandregdate` | 报到日期 | `char` | 10 | 是 | 否 | 否 | - | - | 报到日期 |
| 8 | `otherrequest` | 其他要求 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | 其他要求 |
| 9 | `refermandid` | 提交人 | `integer` | - | 是 | 否 | 否 | - | - | 提交人 |
| 10 | `referdate` | 提交日期 | `char` | 10 | 是 | 否 | 否 | - | - | 提交日期 |
| 11 | `status` | 状态 | `integer` | - | 是 | 否 | 否 | - | 0 | 状态 |
| 12 | `createkind` | 创建类别 | `integer` | - | 是 | 否 | 否 | - | 0 | 创建类别 |
| 13 | `demanddep` | 提交部门 | `integer` | - | 是 | 否 | 否 | - | - | 提交部门 |
| 14 | `requestid` | requestid | `integer` | - | 是 | 否 | 否 | - | - | requestid |
| 15 | `manager` | manager | `integer` | - | 是 | 否 | 否 | - | - | manager |
