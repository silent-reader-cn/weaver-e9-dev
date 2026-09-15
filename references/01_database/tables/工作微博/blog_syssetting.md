# 泛微OA 数据表: `blog_syssetting`

- **所属模块**: `工作微博`
- **数据库表名**: `blog_syssetting`
- **字段总数**: `12`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `makeupis` | 补交是否含工作日 | `varchar2` | 16 | 是 | - |
| 2 | `caneditis` | 编辑是否含工作日 | `varchar2` | 16 | 是 | - |
| 3 | `id` | 主键id | `integer` | - | 否 | - |
| 4 | `allowrequest` | 允许请求 | `integer` | - | 是 | - |
| 5 | `enabledate` | 开启日期 | `varchar2` | 80 | 是 | - |
| 6 | `issingremind` | 单独提醒 | `integer` | - | 是 | - |
| 7 | `ismanagerscore` | 上级评分 | `integer` | - | 是 | - |
| 8 | `attachmentdir` | 附件路径 | `varchar2` | 4000 | 是 | - |
| 9 | `allowexport` | 允许导出 | `char` | 1 | 是 | - |
| 10 | `issendblognote` | 发送便签 | `char` | 1 | 是 | - |
| 11 | `makeuptime` | 补交时间 | `varchar2` | 40 | 是 | - |
| 12 | `canedittime` | 编辑时间 | `varchar2` | 40 | 是 | - |
