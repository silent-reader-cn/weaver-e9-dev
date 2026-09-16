# 泛微OA 数据表: `blog_syssetting`

- **中文名称**: 工作微博系统基本设置表
- **所属模块**: `工作微博`
- **数据库表名**: `blog_syssetting`
- **主键**: `id`
- **字段数**: `12`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `makeupis` | 补交是否含工作日 | `varchar2` | 16 | 是 | 否 | 否 | - | - | - |
| 2 | `caneditis` | 编辑是否含工作日 | `varchar2` | 16 | 是 | 否 | 否 | - | - | - |
| 3 | `id` | 主键id | `integer` | - | 否 | 否 | 否 | - | - | - |
| 4 | `allowrequest` | 允许请求 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `enabledate` | 开启日期 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 6 | `issingremind` | 单独提醒 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `ismanagerscore` | 上级评分 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `attachmentdir` | 附件路径 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 9 | `allowexport` | 允许导出 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 10 | `issendblognote` | 发送便签 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 11 | `makeuptime` | 补交时间 | `varchar2` | 40 | 是 | 否 | 否 | - | - | - |
| 12 | `canedittime` | 编辑时间 | `varchar2` | 40 | 是 | 否 | 否 | - | - | - |
