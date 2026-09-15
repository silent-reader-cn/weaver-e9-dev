# 泛微OA 数据表: `bill_hrmusedemand`

- **所属模块**: `人力资源`
- **数据库表名**: `bill_hrmusedemand`
- **字段总数**: `15`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `resource_n` | 人员id | `integer` | - | 是 | 人员id |
| 3 | `demandjobtitle` | 岗位 | `integer` | - | 是 | 岗位 |
| 4 | `demandnum` | 数量 | `integer` | - | 是 | 数量 |
| 5 | `demandkind` | 用工性质 | `integer` | - | 是 | 用工性质 |
| 6 | `leastedulevel` | 最低学历 | `integer` | - | 是 | 最低学历 |
| 7 | `demandregdate` | 报到日期 | `char` | 10 | 是 | 报到日期 |
| 8 | `otherrequest` | 其他要求 | `varchar2` | 4000 | 是 | 其他要求 |
| 9 | `refermandid` | 提交人 | `integer` | - | 是 | 提交人 |
| 10 | `referdate` | 提交日期 | `char` | 10 | 是 | 提交日期 |
| 11 | `status` | 状态 | `integer` | - | 是 | 状态 |
| 12 | `createkind` | 创建类别 | `integer` | - | 是 | 创建类别 |
| 13 | `demanddep` | 提交部门 | `integer` | - | 是 | 提交部门 |
| 14 | `requestid` | requestid | `integer` | - | 是 | requestid |
| 15 | `manager` | manager | `integer` | - | 是 | manager |
