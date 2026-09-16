# 泛微OA 数据表: `docimagefile`

- **中文名称**: 文档附件关联表
- **所属模块**: `知识管理`
- **数据库表名**: `docimagefile`
- **主键**: `id`
- **字段数**: `14`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `signaturecount` | 签章 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `id` | id | `integer` | - | 否 | 否 | 是 | - | - | - |
| 3 | `docid` | 对应文档id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `imagefileid` | 图片文件id | `integer` | - | 是 | 否 | 否 | - | - | 由sequenceindex表得到，和imagefile表相关联 |
| 5 | `imagefilename` | 文件名称,包括后缀名 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 6 | `imagefiledesc` | 文件描述 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 由用户给出 |
| 7 | `imagefilewidth` | 文件宽度 | `integer` | - | 是 | 否 | 否 | - | - | 象素 只对文档中的图片文件,不包括附件及附件中的图片文件 |
| 8 | `imagefileheight` | 文件高度 | `integer` | - | 是 | 否 | 否 | - | - | 象素：只对文档中的图片文件,不包括附件及附件中的图片文件 |
| 9 | `imagefielsize` | 文件大小 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 10 | `docfiletype` | 文件类型 | `varchar2` | 16 | 是 | 否 | 否 | - | - | 1:文档中的图片<br>2:附件(包括附件中的图片)<br>3.world 文档<br>4.excel 文档<br>5.ppt文档<br>6.金山wps文档<br>7、docx文档<br>8、xlsx文档<br>9、pptx文档<br>10、金山et文档<br>11、html文档中的视频 |
| 11 | `versionid` | 唯一标识 | `integer` | - | 是 | 否 | 否 | - | - | 也用来区别world或excel文档的版本 |
| 12 | `versiondetail` | world或excel文档版本描述 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 13 | `isextfile` | 是否是office文档 | `char` | 1 | 是 | 否 | 否 | - | 1 | - |
| 14 | `hasusedtemplet` | 是否使用模板 | `char` | 1 | 是 | 否 | 否 | - | 0 | 1：使用，其他不使用 |
