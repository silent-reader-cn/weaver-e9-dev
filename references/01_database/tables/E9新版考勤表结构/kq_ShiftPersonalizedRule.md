# 泛微OA 数据表: `kq_ShiftPersonalizedRule`

- **中文名称**: 人性化班次设置考勤规则
- **所属模块**: `人力资源`
- **数据库表名**: `kq_ShiftPersonalizedRule`
- **主键**: `id`
- **字段数**: `16`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `serialid` | 外键 班次id 对应表ShiftManagement | `integer` | - | 否 | 否 | 否 | - | - | - |
| 3 | `permitlateminutes` | 允许迟到分钟数 | `varchar2` | - | 否 | 否 | 否 | - | - | - |
| 4 | `seriouslateminutes` | 严重迟到分钟数 | `varchar2` | - | 否 | 否 | 否 | - | - | - |
| 5 | `lateabsentminutes` | 迟到视作旷工分钟数 | `varchar2` | - | 否 | 否 | 否 | - | - | - |
| 6 | `permitleaveearlyminutes` | 允许早退分钟数 | `varchar2` | - | 否 | 否 | 否 | - | - | - |
| 7 | `seriousleaveearlyminutes` | 严重早退分钟数 | `varchar2` | - | 否 | 否 | 否 | - | - | - |
| 8 | `leaveearlyabsentminutes` | 早退视作旷工分钟数 | `varchar2` | - | 否 | 否 | 否 | - | - | - |
| 9 | `permitlatestatus` | 允许迟到是否开启 | `char` | - | 否 | 否 | 否 | - | - | - |
| 10 | `seriouslatestatus` | 严重迟到是否开启 | `char` | - | 否 | 否 | 否 | - | - | - |
| 11 | `lateabsentstatus` | 迟到视作旷工是否开启 | `char` | - | 否 | 否 | 否 | - | - | - |
| 12 | `permitleaveearlystatus` | 允许早退是否开启 | `char` | - | 否 | 否 | 否 | - | - | - |
| 13 | `seriousleaveearlystatus` | 严重早退是否开启 | `char` | - | 否 | 否 | 否 | - | - | - |
| 14 | `leaveearlyabsentstatus` | 早退视作旷工是否开启 | `char` | - | 否 | 否 | 否 | - | - | - |
| 15 | `isdelete` | 删除标识1标识删除 | `char` | - | 否 | 否 | 否 | - | - | - |
| 16 | `uuid` | 唯一值，供插入后查询用 | `varchar2` | - | 否 | 否 | 否 | - | - | - |
