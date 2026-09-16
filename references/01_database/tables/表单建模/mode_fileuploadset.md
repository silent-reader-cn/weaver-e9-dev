# 泛微OA 数据表: `mode_fileuploadset`

- **中文名称**: 建模附件上传详细设置表
- **所属模块**: `表单建模`
- **数据库表名**: `mode_fileuploadset`
- **主键**: `modeid + formid + fieldid`
- **字段数**: `12`

> 说明：附件上传设置功能添加，用于保存用户对于具体附件字段的详细设置

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `modeid` | 模块id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `formid` | 表单id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `fieldid` | 字段id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `selectfieldid` | 选择目录 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `type` | 类型 | `varchar2` | 1 | 是 | 否 | 否 | - | - | - |
| 6 | `categorytype` | 目录类型 | `integer` | - | 是 | 否 | 否 | - | - | 0：固定目录 1：选择目录，9：默认目录 |
| 7 | `maincategory` | 一级目录 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `subcategory` | 二级目录 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 9 | `seccategory` | 三级目录 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 10 | `fileformattype` | 附件上传文件类型 | `integer` | - | 是 | 否 | 否 | - | - | 0：不限制 1：文档 2：图片 |
| 11 | `fileformat` | 附件限制类型 | `varchar2` | 256 | 是 | 否 | 否 | - | - | - |
| 12 | `limitvalue` | 附件限制大小 | `integer` | - | 是 | 否 | 否 | - | - | - |
