# 泛微OA 数据表: `modeformextend`

- **所属模块**: `表单建模`
- **数据库表名**: `modeformextend`
- **字段总数**: `3`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `formid` | 表单id | `integer` | - | 是 | 对应workflow_bill表的id |
| 2 | `appid` | 所属应用 | `integer` | - | 是 | 对应modetreefield表的id |
| 3 | `isvirtualform` | 是否虚拟表单 | `varchar2` | 16 | 是 | - |
