# 泛微OA 数据表: `docseccategory`

- **所属模块**: `知识管理`
- **数据库表名**: `docseccategory`
- **字段总数**: `13`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `seccategorytype` | 目录类型 | `integer` | - | 否 | - |
| 2 | `uploadext` | 附件上传限制格式 | `varchar2` | 4000 | 是 | - |
| 3 | `pushoperation` | 推送操作 | `number` | (2,0) | 是 | - |
| 4 | `pushways` | 推送方式 | `varchar2` | 1000 | 是 | - |
| 5 | `wordmouldid` | word模板id | `integer` | - | 是 | - |
| 6 | `coder` | 子目录编码 | `varchar2` | 800 | 是 | - |
| 7 | `issetshare` | 提交文档时是否弹出共享设置窗口 | `integer` | - | 是 | - |
| 8 | `nodownload` | 禁止文档下载 | `integer` | - | 是 | 禁止对word、excel、wps、ppt类型文档的下载(存为本地文件)，对html类型文档无效，对html类型文档的附件不限制。(1、禁止,0、否) |
| 9 | `norepeatedname` | 禁止文档重名 | `integer` | - | 是 | 该子目录下禁止新建和修改出重名的文档(1、禁止,0、否) |
| 10 | `iscontroledbydir` | 是否受控目录 | `integer` | - | 是 | 选中时正常状态的文档1、“生效”， 0、“正常”； |
| 11 | `puboperation` | 发布操作 | `integer` | - | 是 | 该目录下文档是否需要发布操作才能变为“生效、正常“（1、是；0、否） |
| 12 | `childdocreadremind` | 子文档阅读提醒 | `integer` | - | 是 | 当打开主文档时，是否需要弹出消息，提示查看子文档（1、是；0、否） |
| 13 | `readoptercanprint` | 允许只读操作人打印 | `integer` | - | 是 | - |
