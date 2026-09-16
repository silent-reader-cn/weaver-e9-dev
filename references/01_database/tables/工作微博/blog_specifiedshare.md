# 泛微OA 数据表: `blog_specifiedshare`

- **中文名称**: 工作微博指定分享表
- **所属模块**: `工作微博`
- **数据库表名**: `blog_specifiedshare`
- **主键**: `id`
- **字段数**: `14`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `shareid` | 分享id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `datatype` | 数据类型 | `varchar2` | 16 | 是 | 否 | 否 | - | - | - |
| 3 | `containlower` | 是否含下级 | `varchar2` | 16 | 是 | 否 | 否 | - | - | - |
| 4 | `rolelevel` | 角色类型 | `varchar2` | 16 | 是 | 否 | 否 | - | - | - |
| 5 | `jobtitlelevel` | 岗位等级 | `varchar2` | 16 | 是 | 否 | 否 | - | - | - |
| 6 | `jobtitlescopeid` | 岗位范围 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 7 | `canviewmintime` | 可查看起始时间 | `char` | 10 | 是 | 否 | 否 | - | -1 | - |
| 8 | `id` | 主键id | `integer` | - | 否 | 否 | 否 | - | - | - |
| 9 | `specifiedid` | 指定共享id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 10 | `type` | 类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 11 | `content` | 内容 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 12 | `seclevel` | 最小安全等级 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 13 | `sharelevel` | 分享等级 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 14 | `seclevelmax` | 最大安全等级 | `integer` | - | 是 | 否 | 否 | - | 100 | - |
