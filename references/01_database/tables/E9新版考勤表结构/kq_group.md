# 泛微OA 数据表: `kq_group`

- **所属模块**: `E9新版考勤表结构`
- **数据库表名**: `kq_group`
- **字段总数**: `22`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键ID | `integer` | - | 否 | - |
| 2 | `groupname` | 组名称 | `varchar2` | 500 | 否 | - |
| 3 | `subcompanyid` | 所属分部 | `integer` | - | 否 | - |
| 4 | `kqtype` | 考勤组类型 | `integer` | - | 否 | - |
| 5 | `excludeid` | 无需考勤人员 | `varchar2` | 4000 | 否 | - |
| 6 | `signintype` | 打卡方式 | `integer` | - | 否 | - |
| 7 | `ipscope` | 应用IP范围 | `varchar2` | 500 | 否 | - |
| 8 | `locationcheck` | 启用办公地点考勤 | `integer` | - | 否 | - |
| 9 | `locationcheckscope` | 办公地点有效范围 | `integer` | - | 否 | - |
| 10 | `wificheck` | 启用wifi考勤 | `integer` | - | 否 | - |
| 11 | `weekday` | 考勤工作日 | `varchar2` | 100 | 否 | - |
| 12 | `shiftcyclename` | 周期名称 | `varchar2` | 500 | 否 | - |
| 13 | `shiftcycleday` | 每个周期天数 | `integer` | - | 否 | - |
| 14 | `shiftcycleserialids` | 周期班次 | `varchar2` | 500 | 否 | - |
| 15 | `serialids` | 考勤班次 | `varchar2` | 1000 | 否 | - |
| 16 | `signstart` | 考勤开始时间 | `varchar2` | 5 | 否 | - |
| 17 | `workhour` | 工作时长 | `number` | - | 否 | - |
| 18 | `outsidesign` | 允许外勤打卡 | `integer` | - | 否 | - |
| 19 | `validity` | 有效期 | `integer` | - | 否 | - |
| 20 | `validityfromdate` | 有效期开始时间 | `varchar2` | 10 | 否 | - |
| 21 | `validityenddate` | 有效期结束时间 | `varchar2` | 10 | 否 | - |
| 22 | `isdelete` | 是否删除 | `integer` | - | 否 | - |
