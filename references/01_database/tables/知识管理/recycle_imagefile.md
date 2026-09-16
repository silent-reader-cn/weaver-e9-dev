# 泛微OA 数据表: `recycle_imagefile`

- **中文名称**: 回收站-附件信息表
- **所属模块**: `知识管理`
- **数据库表名**: `recycle_imagefile`
- **主键**: `无`
- **字段数**: `22`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `imagefileid` | 附件id | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `imagefilename` | 附件名称 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 3 | `imagefiletype` | 附件类型 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 4 | `imagefile` | 附件 | `blob` | 4000 | 是 | 否 | 否 | - | - | - |
| 5 | `imagefileused` | 使用次数 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `filerealpath` | 物理路径 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 7 | `iszip` | 是否zip | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 8 | `isencrypt` | 是否加密 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 9 | `filesize` | 附件大小 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 10 | `downloads` | 下载次数 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 11 | `miniimgpath` | 图片路径 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 12 | `imgsize` | 图片大小 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 13 | `isftp` | 是否ftp | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 14 | `ftpconfigid` | ftp设置id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 15 | `isaesencrypt` | 是否aes加密 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 16 | `aescode` | aes加密码 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 17 | `tokenkey` | 加密key | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 18 | `storagestatus` | 阿里云存储状态 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 19 | `comefrom` | 来源于 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 20 | `objid` | 对象id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 21 | `objotherpara` | 其他对象参数 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 22 | `delfilerealpath` | 是否已删除存储存储 | `char` | 1 | 是 | 否 | 否 | - | - | - |
