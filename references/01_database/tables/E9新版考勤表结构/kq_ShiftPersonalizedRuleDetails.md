# 泛微OA 数据表: `kq_ShiftPersonalizedRuleDetails`

- **中文名称**: 人性化班次设置其他规则
- **所属模块**: `人力资源`
- **数据库表名**: `kq_ShiftPersonalizedRuleDetails`
- **主键**: `id`
- **字段数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `personalizedruleid` | 外键 班次个性化设置id 对应表ShiftPersonalizedRule | `integer` | - | 否 | 否 | 否 | - | - | - |
| 3 | `enable` | 规则是否启用 1表示启用 | `char` | - | 否 | 否 | 否 | - | - | - |
| 4 | `advancetime` | 提前时长 存的是分钟数 | `varchar2` | - | 否 | 否 | 否 | - | - | - |
| 5 | `postponetime` | 延后时长 存的是分钟数 | `varchar2` | - | 否 | 否 | 否 | - | - | - |
| 6 | `ruledetailtype` | 规则类型:早到早走earlyInEarlyOut,晚到晚走lateInLateOut,晚走晚到lateOutLateIn | `varchar2` | - | 否 | 否 | 否 | - | - | - |
| 7 | `isdelete` | 删除标识1标识删除 | `char` | - | 否 | 否 | 否 | - | - | - |
| 8 | `record` | 多条数据顺序 | `varchar2` | - | 否 | 否 | 否 | - | - | - |
