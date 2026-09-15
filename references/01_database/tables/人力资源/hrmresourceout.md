# 泛微OA 数据表: `hrmresourceout`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmresourceout`
- **字段总数**: `12`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `resourceid` | 人员id | `integer` | - | 是 | - |
| 3 | `wxname` | 微信昵称 | `varchar2` | 1000 | 是 | - |
| 4 | `wxopenid` | 用户微信 | `varchar2` | 256 | 是 | - |
| 5 | `wxuuid` | 用户微信 | `varchar2` | 512 | 是 | - |
| 6 | `customid` | 所属客户 | `integer` | - | 是 | - |
| 7 | `country` | 所属国家 | `varchar2` | 1000 | 是 | - |
| 8 | `province` | 所属省份 | `varchar2` | 1000 | 是 | - |
| 9 | `city` | 所属城市 | `varchar2` | 1000 | 是 | - |
| 10 | `customfrom` | 信息来源 | `varchar2` | 1000 | 是 | - |
| 11 | `isoutmanager` | 是否是外部管理员 | `integer` | - | 是 | - |
| 12 | `tmpcustomid` | 客户id | `integer` | - | 是 | - |
