# 泛微OA 数据表: `fnainitdatatb`

- **所属模块**: `财务管理`
- **数据库表名**: `fnainitdatatb`
- **字段总数**: `2`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `typename` | 预算初始化数据名称 | `varchar2` | 1000 | 是 | FnaBudgetfeeType.archive、FnaBudgetfeeType.feeperiod、FnaBudgetfeeType.updateAllSubjectGroupCtrlGuid()、FnaBudgetfeeType.updateAllIsEditFeeTypeGuid()、FnaBudgetfeeType.updateAllSupSubjectIds() |
| 2 | `result1` | 是否执行 | `char` | 1 | 是 | 1：执行成功；其他：失败； |
