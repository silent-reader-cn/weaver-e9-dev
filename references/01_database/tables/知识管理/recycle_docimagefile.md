# 泛微OA 数据表: `recycle_docimagefile`

- **所属模块**: `知识管理`
- **数据库表名**: `recycle_docimagefile`
- **字段总数**: `14`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | - |
| 2 | `docid` | 文档id | `integer` | - | 是 | - |
| 3 | `imagefileid` | 附件id | `integer` | - | 是 | - |
| 4 | `imagefilename` | 附件名称 | `varchar2` | 1000 | 是 | - |
| 5 | `imagefiledesc` | 附件排序 | `varchar2` | 1000 | 是 | - |
| 6 | `imagefilewidth` | 附件宽度 | `integer` | - | 是 | - |
| 7 | `imagefileheight` | 附件高度 | `integer` | - | 是 | - |
| 8 | `imagefielsize` | 附件大小 | `integer` | - | 是 | - |
| 9 | `docfiletype` | 文件类型 | `varchar2` | 1000 | 是 | - |
| 10 | `versionid` | 文件版本 | `integer` | - | 是 | - |
| 11 | `versiondetail` | 版本描述 | `varchar2` | 1000 | 是 | - |
| 12 | `isextfile` | 是否是office文档 | `char` | 1 | 是 | - |
| 13 | `hasusedtemplet` | 是否使用模板 | `char` | 1 | 是 | - |
| 14 | `signaturecount` | 签章数量 | `integer` | - | 是 | - |
