# 泛微OA 数据表: `rtxsetting`

- **所属模块**: `集成模块`
- **数据库表名**: `rtxsetting`
- **字段总数**: `18`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `rtxserverip` | RTX服务器地址 | `varchar2` | 400 | 是 | - |
| 2 | `rtxserveroutip` | RTX服务器对外地址 | `varchar2` | 400 | 是 | - |
| 3 | `rtxserverport` | RTX中间件端口号 | `varchar2` | 80 | 是 | RTX固定为8036 |
| 4 | `domainname` | 域名 | `varchar2` | 1000 | 是 | RtxOrOCSType=1时使用 |
| 5 | `rtxversion` | RTX版本 | `varchar2` | 80 | 是 | RtxOrOCSType=1时使用 |
| 6 | `rtxorocstype` | IM类型 | `char` | 1 | 是 | 0：RTX  1：OCS  2：其他 |
| 7 | `rtxonload` | 自动登录 | `char` | 1 | 是 | 1：是  0：否 |
| 8 | `rtxdenyhrm` | 同步组织架构及账号 | `char` | 1 | 是 | 1：是  0：否 |
| 9 | `isusedrtx` | 是否启用 | `char` | 1 | 是 | 1：是  0：否 |
| 10 | `rtxalert` | 流程到达提醒 | `char` | 1 | 是 | 1：是  0：否 |
| 11 | `cursmsserverisvalid` | 使用RTX短信 | `varchar2` | 80 | 是 | 默认8000 |
| 12 | `cursmsserver` | RTX短信地址 | `varchar2` | 80 | 是 | - |
| 13 | `rtxconnserver` | RTX服务器端口号 | `varchar2` | 80 | 是 | - |
| 14 | `userattr` | 绑定IM账号字段数据库 | `varchar2` | 1000 | 是 | 对应人员字段数据库 |
| 15 | `username` | 绑定IM账号 字段中文名 | `varchar2` | 1000 | 是 | - |
| 16 | `rtxlogintooa` | IM反向登陆 | `char` | 1 | 是 | 1：是  0：否 |
| 17 | `impwd` | 默认密码 | `varchar2` | 1000 | 是 | 默认密码 |
| 18 | `isdownload` | 中间件下载 | `varchar2` | 400 | 是 | - |
