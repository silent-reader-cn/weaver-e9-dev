# 泛微OA 数据表: `kq_ShiftOnOffWorkSections`

- **所属模块**: `E9新版考勤表结构`
- **数据库表名**: `kq_ShiftOnOffWorkSections`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `serialid` | 外键 班次id 对应表ShiftManagement | `integer` | - | 否 | - |
| 3 | `across` | 指定时段是否跨天 1表示跨天 | `varchar2` | - | 否 | - |
| 4 | `beginmin` | 当设置打卡时段时，预留字段 | `varchar2` | - | 否 | - |
| 5 | `endmin` | 当设置打卡时段时，预留字段 | `varchar2` | - | 否 | - |
| 6 | `times` | 具体时段时间 | `varchar2` | - | 否 | - |
| 7 | `onoffworktype` | 时段类型，开始(start)/结束(end) | `varchar2` | - | 否 | - |
| 8 | `isdelete` | 删除标识1标识删除 | `char` | - | 否 | - |
| 9 | `mins` | 当设置打卡时段时，表示多少分钟开始打卡 | `varchar2` | - | 否 | - |
| 10 | `record` | 上下班时段顺序 | `char` | - | 否 | - |
