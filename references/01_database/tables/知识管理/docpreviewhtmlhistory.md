# 泛微OA 数据表: `docpreviewhtmlhistory`

- **所属模块**: `知识管理`
- **数据库表名**: `docpreviewhtmlhistory`
- **字段总数**: `12`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `imagefileid` | 附件id | `integer` | - | 是 | - |
| 3 | `htmlfileid` | html附件id | `integer` | - | 是 | - |
| 4 | `previewcount` | 预览次数 | `integer` | - | 是 | - |
| 5 | `systemtag` | ecology系统的标识 | `varchar2` | 800 | 是 | 默认：ecology |
| 6 | `filetablename` | 文件表名 | `varchar2` | 480 | 是 | 默认为文档附件表imagefile |
| 7 | `mustreconverted` | 是否必须重新转换 | `char` | 1 | 是 | 1：必须，0或其他：不需要 |
| 8 | `createdate` | 创建日期 | `char` | 10 | 是 | - |
| 9 | `createtime` | 创建时间 | `char` | 8 | 是 | - |
| 10 | `lastaccessdate` | 最后访问日期 | `char` | 10 | 是 | - |
| 11 | `lastaccesstime` | 最后访问时间 | `char` | 8 | 是 | - |
| 12 | `docid` | 文档id | `integer` | - | 是 | - |
