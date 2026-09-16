# 泛微OA 数据表: `hrmschedulesign`

- **中文名称**: 人事考勤签到签退表
- **所属模块**: `12`
- **数据库表名**: `hrmschedulesign`
- **主键**: `ID`
- **字段数**: `18`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `wxsignaddress` | 微信端签到地址 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 2 | `eb_deviceid` | 设备号 | `varchar2` | 512 | 是 | 否 | 否 | - | - | - |
| 3 | `eb_deviceid_change` | 设备号 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `isimport` | 是否是从其他系统同步过来 | `integer` | - | 是 | 否 | 否 | - | - | 1-是，0-否 |
| 5 | `suuid` | 导入批次ID | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 6 | `timezone` | 多时区所在时区 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 7 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 8 | `userid` | 用户id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 9 | `usertype` | 用户类型 | `char` | 1 | 是 | 否 | 否 | - | - | 1:内部用户，2：外部用户 |
| 10 | `signtype` | 考勤类型 | `char` | 1 | 是 | 否 | 否 | - | - | 1：签到，2：签退 |
| 11 | `signdate` | 考勤日期 | `char` | 10 | 是 | 否 | 否 | - | - | 签到或签退日期 |
| 12 | `signtime` | 考勤时间 | `char` | 8 | 是 | 否 | 否 | - | - | 签到或签退时间 |
| 13 | `clientaddress` | 客户端ip | `varchar2` | 120 | 是 | 否 | 否 | - | - | - |
| 14 | `isincom` | 是否是有效考勤打卡 | `char` | 1 | 是 | 否 | 否 | - | - | 1-有效，0-无效。 |
| 15 | `signfrom` | 考勤来源 | `varchar2` | 400 | 是 | 否 | 否 | - | - | e9pc：PC考勤 e9mobile：emobile考勤 e9e： emobile小E考勤 e9ewx：微信小E考勤 card：补打卡考勤 e9_mobile_out：外勤签到 importExcel：Excel考勤数据导入 EMSyn：云桥考勤数据同步 OutDataSourceSyn：外部考勤数据同步 DingTalk：钉钉考勤 DingTalk_out：钉钉外勤打卡 Wechat_out：微信外勤转考勤 Wechat：微信考勤 |
| 16 | `longitude` | 考勤地点经度 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 17 | `latitude` | 考勤地点纬度 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 18 | `addr` | 考勤地址 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
