# 泛微OA 数据表: `WorkPlanWeekList_GroupLimit`

- **所属模块**: `日程管理`
- **数据库表名**: `WorkPlanWeekList_GroupLimit`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | - | 主键 |
| 2 | `groupid` | 一周日程按钮数据范围id | `integer` | - | - | 一周日程按钮数据范围id |
| 3 | `objtype` | 类型 | `integer` | - | - | 1:人员；2：分部；3：部门；4：角色；5：岗位；6：所有人 |
| 4 | `objvalue` | id值 | `integer` | - | - | 对应类型objtype的id值 |
| 5 | `seclevelmin` | 最小安全级别 | `integer` | - | - | 最小安全级别 |
| 6 | `seclevelmax` | 最大安全级别 | `integer` | - | - | 最大安全级别 |
| 7 | `rolelevel` | 角色级别 | `integer` | - | - | 0：部门；1：分部；2：总部 |
| 8 | `joblevel` | 岗位级别 | `integer` | - | - | 0：总部；1：指定分部；2：指定部门 |
| 9 | `jobvalue` | 指定岗位级别 | `integer` | - | - | 当joblevel为1时，为分部id;当joblevel为2时，为部门id |
