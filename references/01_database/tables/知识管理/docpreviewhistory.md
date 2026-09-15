# 泛微OA 数据表: `docpreviewhistory`

- **所属模块**: `知识管理`
- **数据库表名**: `docpreviewhistory`
- **字段总数**: `17`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `imagefileid` | 附件id | `integer` | - | 是 | - |
| 3 | `filepath` | 临时文件路径 | `varchar2` | 1000 | 是 | - |
| 4 | `pdffileid` | pdf附件id | `integer` | - | 是 | - |
| 5 | `pdfpath` | pdf临时文件路径 | `varchar2` | 1000 | 是 | - |
| 6 | `swffileid` | swf附件id | `integer` | - | 是 | - |
| 7 | `swfpath` | swf临时文件路径 | `varchar2` | 1000 | 是 | - |
| 8 | `swfpagecount` | swf文件页面数 | `integer` | - | 是 | - |
| 9 | `previewcount` | 预览次数 | `integer` | - | 是 | - |
| 10 | `systemtag` | ecology系统的标识 | `varchar2` | 800 | 是 | 默认：ecology |
| 11 | `filetablename` | 文件表名 | `varchar2` | 480 | 是 | 默认为文档附件表imagefile |
| 12 | `mustreconverted` | 是否必须重新转换 | `char` | 1 | 是 | 1：必须，0或其他：不需要 |
| 13 | `createdate` | 创建日期 | `char` | 10 | 是 | - |
| 14 | `createtime` | 创建时间 | `char` | 8 | 是 | - |
| 15 | `lastaccessdate` | 最后访问日期 | `char` | 10 | 是 | - |
| 16 | `lastaccesstime` | 最后访问时间 | `char` | 8 | 是 | - |
| 17 | `docid` | 文档id | `integer` | - | 是 | - |
