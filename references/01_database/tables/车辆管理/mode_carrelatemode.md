# 泛微OA 数据表: `mode_carrelatemode`

- **所属模块**: `车辆管理`
- **数据库表名**: `mode_carrelatemode`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `mainid` | 主表id | `integer` | - | 是 | 对应carbasic表id |
| 3 | `carfieldid` | 车辆系统表中字段id | `integer` | - | 是 | - |
| 4 | `modefieldid` | 当前自定义表字段id | `integer` | - | 是 | - |
| 5 | `requirednode` | 流程节点信息 | `varchar2` | 100 | 是 | - |
