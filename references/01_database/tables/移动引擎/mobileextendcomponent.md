# 泛微OA 数据表: `mobileextendcomponent`

- **所属模块**: `移动引擎`
- **数据库表名**: `mobileextendcomponent`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `varchar2` | 50 | 否 | 32位uuid |
| 2 | `objid` | 所属自定义页面id | `varchar2` | 1000 | 是 | 插件所在的自定义页面，apphomepage表的id列外键 |
| 3 | `objtype` | 所属自定义页面类型 | `varchar2` | 640 | 是 | 无用，已废弃 |
| 4 | `mectype` | 插件类型 | `varchar2` | 1000 | 是 | 插件类型，如html，list等。此类型枚举插件配置文件中配置的id |
| 5 | `mecparam` | 插件内容 | `nclob` | 4000 | 是 | 插件的配置信息，json数据格式 |
