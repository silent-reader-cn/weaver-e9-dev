# 泛微OA 数据表: `hrmschedulesignimp`

- **所属模块**: `E9新版考勤表结构`
- **数据库表名**: `hrmschedulesignimp`
- **字段总数**: `20`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `userid` | 人员id | `integer` | - | 是 | 人员id |
| 3 | `usertype` | 人员类型 | `char` | 1 | 是 | 人员类型 |
| 4 | `signtype` | 打卡类型 | `char` | 1 | 是 | 打卡类型：1为签到，2为签退。 |
| 5 | `signdate` | 打卡日期 | `char` | 10 | 是 | 打卡日期 |
| 6 | `signtime` | 打卡时间 | `char` | 8 | 是 | 打卡时间 |
| 7 | `clientaddress` | ip地址 | `varchar2` | 1000 | 是 | ip地址 |
| 8 | `isincom` | 是否有效 | `char` | 1 | 是 | 是否有效 |
| 9 | `signfrom` | 打卡判断说明 | `varchar2` | 1000 | 是 | 打卡判断说明 |
| 10 | `longitude` | 经度 | `varchar2` | 1000 | 是 | 经度 |
| 11 | `latitude` | 纬度 | `varchar2` | 1000 | 是 | 纬度 |
| 12 | `addr` | 地址 | `varchar2` | 1000 | 是 | 地址 |
| 13 | `wxsignaddress` | 微信签到地址 | `varchar2` | 1000 | 是 | 微信签到地址 |
| 14 | `eb_deviceid` | 设备号 | `varchar2` | 512 | 是 | 设备号 |
| 15 | `eb_deviceid_change` | 设备类型 | `integer` | - | 是 | 设备类型 |
| 16 | `importsql` | 导入语句说明 | `varchar2` | 1000 | 是 | 导入语句说明 |
| 17 | `impdatetime` | 考勤导入时间 | `varchar2` | 1000 | 是 | 考勤导入时间 |
| 18 | `suuid` | SUUID | `varchar2` | 1000 | 是 | SUUID |
| 19 | `uuid` | UUID | `varchar2` | 1000 | 是 | UUID |
| 20 | `delflag` | 状态 | `char` | 1 | 是 | 0为有效，非0为无效 |
