# 泛微OA 数据表: `blog_specifiedshare`

- **所属模块**: `工作微博`
- **数据库表名**: `blog_specifiedshare`
- **字段总数**: `14`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `shareid` | 分享id | `integer` | - | 是 | - |
| 2 | `datatype` | 数据类型 | `varchar2` | 16 | 是 | - |
| 3 | `containlower` | 是否含下级 | `varchar2` | 16 | 是 | - |
| 4 | `rolelevel` | 角色类型 | `varchar2` | 16 | 是 | - |
| 5 | `jobtitlelevel` | 岗位等级 | `varchar2` | 16 | 是 | - |
| 6 | `jobtitlescopeid` | 岗位范围 | `varchar2` | 4000 | 是 | - |
| 7 | `canviewmintime` | 可查看起始时间 | `char` | 10 | 是 | - |
| 8 | `id` | 主键id | `integer` | - | 否 | - |
| 9 | `specifiedid` | 指定共享id | `integer` | - | 是 | - |
| 10 | `type` | 类型 | `integer` | - | 是 | - |
| 11 | `content` | 内容 | `varchar2` | 4000 | 是 | - |
| 12 | `seclevel` | 最小安全等级 | `integer` | - | 是 | - |
| 13 | `sharelevel` | 分享等级 | `integer` | - | 是 | - |
| 14 | `seclevelmax` | 最大安全等级 | `integer` | - | 是 | - |
