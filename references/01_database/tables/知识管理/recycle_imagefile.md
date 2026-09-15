# 泛微OA 数据表: `recycle_imagefile`

- **所属模块**: `知识管理`
- **数据库表名**: `recycle_imagefile`
- **字段总数**: `22`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `imagefileid` | 附件id | `integer` | - | 否 | - |
| 2 | `imagefilename` | 附件名称 | `varchar2` | 1000 | 是 | - |
| 3 | `imagefiletype` | 附件类型 | `varchar2` | 1000 | 是 | - |
| 4 | `imagefile` | 附件 | `blob` | 4000 | 是 | - |
| 5 | `imagefileused` | 使用次数 | `integer` | - | 是 | - |
| 6 | `filerealpath` | 物理路径 | `varchar2` | 1000 | 是 | - |
| 7 | `iszip` | 是否zip | `char` | 1 | 是 | - |
| 8 | `isencrypt` | 是否加密 | `char` | 1 | 是 | - |
| 9 | `filesize` | 附件大小 | `varchar2` | 1000 | 是 | - |
| 10 | `downloads` | 下载次数 | `integer` | - | 否 | - |
| 11 | `miniimgpath` | 图片路径 | `varchar2` | 1000 | 是 | - |
| 12 | `imgsize` | 图片大小 | `varchar2` | 1000 | 是 | - |
| 13 | `isftp` | 是否ftp | `char` | 1 | 是 | - |
| 14 | `ftpconfigid` | ftp设置id | `integer` | - | 是 | - |
| 15 | `isaesencrypt` | 是否aes加密 | `integer` | - | 是 | - |
| 16 | `aescode` | aes加密码 | `varchar2` | 1000 | 是 | - |
| 17 | `tokenkey` | 加密key | `varchar2` | 1000 | 是 | - |
| 18 | `storagestatus` | 阿里云存储状态 | `char` | 1 | 是 | - |
| 19 | `comefrom` | 来源于 | `varchar2` | 1000 | 是 | - |
| 20 | `objid` | 对象id | `integer` | - | 是 | - |
| 21 | `objotherpara` | 其他对象参数 | `varchar2` | 1000 | 是 | - |
| 22 | `delfilerealpath` | 是否已删除存储存储 | `char` | 1 | 是 | - |
