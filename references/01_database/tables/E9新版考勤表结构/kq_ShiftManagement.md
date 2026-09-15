# 泛微OA 数据表: `kq_ShiftManagement`

- **所属模块**: `E9新版考勤表结构`
- **数据库表名**: `kq_ShiftManagement`
- **字段总数**: `13`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `serial` | 班次名称 | `varchar2` | 200 | 否 | - |
| 3 | `isresttimeopen` | 排除休息时间是否开启 1表示开启 | `char` | - | 否 | - |
| 4 | `shiftonoffworkcount` | 一天上下班次数 | `integer` | - | 否 | - |
| 5 | `shiftonoffworksectionsid` | 一天上下班次数 对应具体明细id | `integer` | - | 否 | - |
| 6 | `punchsettings` | 打卡时段是否开启 | `char` | - | 否 | - |
| 7 | `isoffdutyfreecheck` | 是否开启下班不用打卡 1表示下班不用打卡 | `char` | - | 否 | - |
| 8 | `shiftpersonnelruleid` | 人性化班次设置 对应表shiftPersonnelRule | `integer` | - | 否 | - |
| 9 | `worktime` | 工作时长，分钟数 | `varchar2` | - | 否 | - |
| 10 | `subcompanyid` | 分权分部id | `integer` | - | 否 | - |
| 11 | `isenablenextday` | 班次是否次日起效，true表示次日起效 | `varchar2` | - | 否 | - |
| 12 | `isdelete` | 删除标识1标识删除 | `varchar2` | - | 否 | - |
| 13 | `uuid` | 唯一值，供插入后查询用 | `varchar2` | - | 否 | - |
