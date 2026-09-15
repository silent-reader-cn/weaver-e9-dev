# 泛微OA 数据表: `mode_fileuploadset`

- **所属模块**: `表单建模`
- **数据库表名**: `mode_fileuploadset`
- **字段总数**: `12`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `modeid` | 模块id | `integer` | - | 是 | - |
| 2 | `formid` | 表单id | `integer` | - | 是 | - |
| 3 | `fieldid` | 字段id | `integer` | - | 是 | - |
| 4 | `selectfieldid` | 选择目录 | `integer` | - | 是 | - |
| 5 | `type` | 类型 | `varchar2` | 1 | 是 | - |
| 6 | `categorytype` | 目录类型 | `integer` | - | 是 | 0：固定目录 1：选择目录，9：默认目录 |
| 7 | `maincategory` | 一级目录 | `integer` | - | 是 | - |
| 8 | `subcategory` | 二级目录 | `integer` | - | 是 | - |
| 9 | `seccategory` | 三级目录 | `integer` | - | 是 | - |
| 10 | `fileformattype` | 附件上传文件类型 | `integer` | - | 是 | 0：不限制 1：文档 2：图片 |
| 11 | `fileformat` | 附件限制类型 | `varchar2` | 256 | 是 | - |
| 12 | `limitvalue` | 附件限制大小 | `integer` | - | 是 | - |
