# 泛微OA 数据表: `blog_tempshare`

- **所属模块**: `工作微博`
- **数据库表名**: `blog_tempshare`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `jobtitlescopeid` | 岗位范围 | `varchar2` | 2000 | 是 | - |
| 2 | `id` | 主键id | `integer` | - | 否 | - |
| 3 | `tempid` | 模板id | `integer` | - | 是 | - |
| 4 | `type` | 类型 | `integer` | - | 是 | - |
| 5 | `content` | 内容 | `varchar2` | 4000 | 是 | - |
| 6 | `seclevel` | 最小安全等级 | `integer` | - | 是 | - |
| 7 | `seclevelmax` | 最大安全等级 | `integer` | - | 是 | - |
| 8 | `containlower` | 包含下级 | `varchar2` | 16 | 是 | - |
| 9 | `rolelevel` | 角色等级 | `varchar2` | 16 | 是 | - |
| 10 | `jobtitlelevel` | 岗位等级 | `varchar2` | 16 | 是 | - |
