# 泛微OA 数据表: `hrmusedemand`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmusedemand`
- **字段总数**: `12`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `demandjobtitle` | 岗位 | `integer` | - | 是 | 岗位 |
| 3 | `demandnum` | 数量 | `integer` | - | 是 | 数量 |
| 4 | `demandkind` | 用工性质 | `integer` | - | 是 | 用工性质 |
| 5 | `leastedulevel` | 最低学历 | `integer` | - | 是 | 最低学历 |
| 6 | `demandregdate` | 报到日期 | `char` | 10 | 是 | 报到日期 |
| 7 | `otherrequest` | 其他要求 | `varchar2` | 4000 | 是 | 其他要求 |
| 8 | `refermandid` | 提交人 | `integer` | - | 是 | 提交人 |
| 9 | `referdate` | 提交日期 | `char` | 10 | 是 | 提交日期 |
| 10 | `status` | 状态 | `integer` | - | 是 | 状态 |
| 11 | `createkind` | 创建类别 | `integer` | - | 是 | 创建类别  0：工作流；1：页面维护 |
| 12 | `demanddep` | 提交部门 | `integer` | - | 是 | 提交部门 |
