# 泛微OA 数据表: `recycle_docimagefile`

- **中文名称**: 回收站-文档附件关联表
- **所属模块**: `知识管理`
- **数据库表名**: `recycle_docimagefile`
- **主键**: `id`
- **字段数**: `14`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | id | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `docid` | 文档id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `imagefileid` | 附件id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `imagefilename` | 附件名称 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 5 | `imagefiledesc` | 附件排序 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 6 | `imagefilewidth` | 附件宽度 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `imagefileheight` | 附件高度 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `imagefielsize` | 附件大小 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 9 | `docfiletype` | 文件类型 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 10 | `versionid` | 文件版本 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 11 | `versiondetail` | 版本描述 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 12 | `isextfile` | 是否是office文档 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 13 | `hasusedtemplet` | 是否使用模板 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 14 | `signaturecount` | 签章数量 | `integer` | - | 是 | 否 | 否 | - | - | - |
