# 泛微OA 数据表: `fnainitdatatb`

- **中文名称**: 预算数据初始化记录表
- **所属模块**: `财务管理`
- **数据库表名**: `fnainitdatatb`
- **主键**: `typename`
- **字段数**: `2`

> 说明：预算数据初始化记录表，记录预算初始化数据是否完成的日志表。

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `typename` | 预算初始化数据名称 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | FnaBudgetfeeType.archive、FnaBudgetfeeType.feeperiod、FnaBudgetfeeType.updateAllSubjectGroupCtrlGuid()、FnaBudgetfeeType.updateAllIsEditFeeTypeGuid()、FnaBudgetfeeType.updateAllSupSubjectIds() |
| 2 | `result1` | 是否执行 | `char` | 1 | 是 | 否 | 否 | - | - | 1：执行成功；其他：失败； |
