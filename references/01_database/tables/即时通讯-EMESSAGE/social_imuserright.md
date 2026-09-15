# 泛微OA 数据表: `social_imuserright`

- **所属模块**: `即时通讯-EMESSAGE`
- **数据库表名**: `social_imuserright`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键id | `integer` | - | 否 | 主键id |
| 2 | `permissiontype` | 允许类型 | `integer` | - | 是 | 允许类型 |
| 3 | `contents` | 内容 | `integer` | - | 是 | 内容 |
| 4 | `seclevel` | 开始安全级别 | `integer` | - | 是 | 开始安全级别 |
| 5 | `seclevelmax` | 结束安全级别 | `integer` | - | 是 | 结束安全级别 |
| 6 | `jobtitleid` | 工作名id | `varchar2` | 1000 | 是 | 工作名id |
| 7 | `joblevel` | 工作级别 | `integer` | - | 是 | 工作级别 |
| 8 | `scopeid` | 分权信息 | `varchar2` | 800 | 是 | 分权信息 |
