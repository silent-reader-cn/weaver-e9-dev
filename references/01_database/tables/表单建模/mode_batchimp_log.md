# 泛微OA 数据表: `mode_batchimp_log`

- **所属模块**: `表单建模`
- **数据库表名**: `mode_batchimp_log`
- **字段总数**: `12`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 是 | - |
| 2 | `modeid` | 模块id | `integer` | - | 是 | 模块的id，即modeinfo的id |
| 3 | `operatetype` | 操作类型 | `integer` | - | 是 | 记录操作类型 |
| 4 | `ipaddress` | IP | `varchar2` | 400 | 是 | 记录当前操作的ip |
| 5 | `operator` | 操作人 | `integer` | - | 是 | 记录操作人 |
| 6 | `optdatetime` | 操作日期 | `varchar2` | 400 | 是 | 记录操作的日期 |
| 7 | `addrow` | 增加 | `integer` | - | 是 | 记录增加的个数 |
| 8 | `updaterow` | 更新 | `integer` | - | 是 | 记录更新的个数 |
| 9 | `delrow` | 删除 | `integer` | - | 是 | 记录删除的个数 |
| 10 | `adddetailrow` | 增加明细 | `integer` | - | 是 | 记录增加明细的个数 |
| 11 | `deldetailrow` | 删除明细 | `integer` | - | 是 | 记录删除明细的个数 |
| 12 | `failurerow` | 失败 | `varchar2` | 2000 | 否 | 对应mode_impfailurelog中的searchid字段 |
