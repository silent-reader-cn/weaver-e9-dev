# 泛微OA 数据表: `remind_multi_ruleinfo`

- **所属模块**: `表单建模`
- **数据库表名**: `remind_multi_ruleinfo`
- **文档收录字段数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | - | - |
| 2 | `remindjobid` | 提醒id对应mode_remindjob表的id | `integer` | - | - | - |
| 3 | `receivertype` | 提醒接收人员类型 | `integer` | - | - | 1:人员<br>2:分部<br>3:部门<br>4:角色<br>5:所有人<br>6:模块创建人 1000 模块字段 |
| 4 | `receiverdetail` | 提醒人员id | `varchar2` | 4000 | - | - |
| 5 | `receiverfieldtype` | 提醒接收人员字段类型 | `integer` | - | - | 1：人员<br>2：部门<br>3：分部 |
| 6 | `receiverfield` | 提醒接收人员字段 | `varchar2` | - | - | 对应workflow_billfield表的id |
| 7 | `showlevel` | 安全级别最小值 | `integer` | - | - | - |
| 8 | `showlevel2` | 安全级别最大值 | `integer` | - | - | - |
