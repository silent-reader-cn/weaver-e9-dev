# 泛微OA 数据表: `imagefile`

- **中文名称**: 文档附件图片表
- **所属模块**: `知识管理`
- **数据库表名**: `imagefile`
- **主键**: `无`
- **字段数**: `22`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `delfilerealpath` | 啥 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 2 | `iszip` | 是否压缩 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 3 | `isencrypt` | 是否加密 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 4 | `filesize` | 文件大小 | `varchar2` | 160 | 是 | 否 | 否 | - | 0 /*文件大小，bytes*/ | - |
| 5 | `downloads` | 下载次数 | `integer` | - | 否 | 否 | 否 | - | 0 | - |
| 6 | `miniimgpath` | 缩略图存放路径 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 7 | `imgsize` | 缩略图大小 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 8 | `isftp` | 是否FTP存储 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 9 | `ftpconfigid` | FTP服务器配置ID | `integer` | - | 是 | 否 | 否 | - | - | - |
| 10 | `isaesencrypt` | 是否使用AES附件加密 | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 11 | `aescode` | AES加密密码 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 12 | `tokenkey` | 令牌标记 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 13 | `storagestatus` | 阿里云存储状态 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 14 | `comefrom` | 附件来源 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 15 | `objid` | 来源对象 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 16 | `objotherpara` | 对象另外参数 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 17 | `imagefileid` | 图片文件id | `integer` | - | 否 | 否 | 否 | - | - | 由sequenceindex表得到，和imagefile表相关联 |
| 18 | `imagefilename` | 文件名称,包括后缀名 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 19 | `imagefiletype` | 文件MIME类型 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 20 | `imagefile` | 文件 | `blob` | 4000 | 是 | 否 | 否 | - | - | - |
| 21 | `imagefileused` | 文件使用次数 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 22 | `filerealpath` | 文件存放目录 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
