# 泛微OA 数据表: `docpreviewhtml`

- **中文名称**: 文档预览表_html形式
- **所属模块**: `知识管理`
- **数据库表名**: `docpreviewhtml`
- **主键**: `id`
- **字段数**: `12`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 是 | - | - | - |
| 2 | `imagefileid` | 附件id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `htmlfileid` | html附件id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `previewcount` | 预览次数 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `systemtag` | ecology系统的标识 | `varchar2` | 800 | 是 | 否 | 否 | - | - | 默认：ecology |
| 6 | `filetablename` | 文件表名 | `varchar2` | 480 | 是 | 否 | 否 | - | - | 默认为文档附件表imagefile |
| 7 | `mustreconverted` | 是否必须重新转换 | `char` | 1 | 是 | 否 | 否 | - | 0 | 1：必须，0或其他：不需要 |
| 8 | `createdate` | 创建日期 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 9 | `createtime` | 创建时间 | `char` | 8 | 是 | 否 | 否 | - | - | - |
| 10 | `lastaccessdate` | 最后访问日期 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 11 | `lastaccesstime` | 最后访问时间 | `char` | 8 | 是 | 否 | 否 | - | - | - |
| 12 | `docid` | 文档id | `integer` | - | 是 | 否 | 否 | - | - | - |
