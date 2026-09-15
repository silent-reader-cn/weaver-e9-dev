# 泛微OA 数据表: `mailresourcefile`

- **所属模块**: `邮件模块`
- **数据库表名**: `mailresourcefile`
- **字段总数**: `20`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `mrf_uuid` | 附件唯一标志uuid | `varchar2` | 50 | 是 | java生产的32位uuid |
| 2 | `htmlcode` | html预览方式imagefileid | `varchar2` | 800 | 是 | - |
| 3 | `pdfcode` | pdf预览方式imagefileid | `varchar2` | 800 | 是 | - |
| 4 | `storagestatus` | 阿里OSS存储状态 | `char` | 1 | 是 | 1：成功 2：上传中 3：失败 |
| 5 | `tokenkey` | 阿里OSS存储key | `varchar2` | 200 | 是 | - |
| 6 | `id` | ID | `integer` | - | 否 | - |
| 7 | `mailid` | 邮件id | `integer` | - | 是 | - |
| 8 | `filename` | 文件名称 | `varchar2` | 1000 | 是 | - |
| 9 | `attachfile` | 文件内容 | `blob` | 4000 | 是 | 存放在数据库中，现在已不使用 |
| 10 | `filetype` | 文件mime类型 | `varchar2` | 800 | 是 | - |
| 11 | `filerealpath` | 邮件文件存放目录 | `varchar2` | 255 | 是 | - |
| 12 | `iszip` | 是否压缩 | `char` | 1 | 是 | 0：否,1：是 |
| 13 | `isencrypt` | 是否加密 | `char` | 1 | 是 | 0：否,1：是 |
| 14 | `isencoded` | 的 | `char` | 1 | 是 | - |
| 15 | `isfileattrachment` | 的 | `char` | 1 | 是 | - |
| 16 | `filecontentid` | 的 | `varchar2` | 800 | 是 | - |
| 17 | `filesize` | 文件大小 | `integer` | - | 是 | - |
| 18 | `signid` | 签名id | `integer` | - | 是 | - |
| 19 | `isaesencrypt` | 是否使用aes附件加密 | `integer` | - | 是 | 1:是,0或其它：否 |
| 20 | `aescode` | aes加密密码 | `varchar2` | 1000 | 是 | - |
