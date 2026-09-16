# 泛微OA 数据表: `docpreviewhistory`

- **中文名称**: 文档预览历史表
- **所属模块**: `知识管理`
- **数据库表名**: `docpreviewhistory`
- **主键**: `id`
- **字段数**: `17`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 是 | - | - | - |
| 2 | `imagefileid` | 附件id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `filepath` | 临时文件路径 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 4 | `pdffileid` | pdf附件id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `pdfpath` | pdf临时文件路径 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 6 | `swffileid` | swf附件id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `swfpath` | swf临时文件路径 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 8 | `swfpagecount` | swf文件页面数 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 9 | `previewcount` | 预览次数 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 10 | `systemtag` | ecology系统的标识 | `varchar2` | 800 | 是 | 否 | 否 | - | - | 默认：ecology |
| 11 | `filetablename` | 文件表名 | `varchar2` | 480 | 是 | 否 | 否 | - | - | 默认为文档附件表imagefile |
| 12 | `mustreconverted` | 是否必须重新转换 | `char` | 1 | 是 | 否 | 否 | - | 0 | 1：必须，0或其他：不需要 |
| 13 | `createdate` | 创建日期 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 14 | `createtime` | 创建时间 | `char` | 8 | 是 | 否 | 否 | - | - | - |
| 15 | `lastaccessdate` | 最后访问日期 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 16 | `lastaccesstime` | 最后访问时间 | `char` | 8 | 是 | 否 | 否 | - | - | - |
| 17 | `docid` | 文档id | `integer` | - | 是 | 否 | 否 | - | - | - |
