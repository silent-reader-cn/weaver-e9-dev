# 泛微OA 数据表: `exp_xmlprosettings`

- **所属模块**: `集成模块`
- **数据库表名**: `exp_xmlprosettings`
- **字段总数**: `25`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `name` | 方案名称 | `varchar2` | 1000 | 否 | - |
| 3 | `filesavetype` | 文件保存方式 | `char` | 1 | 是 | - |
| 4 | `regittype` | 方案类型 | `integer` | - | 是 | FileSaveType=0,对应exp_ftpdetail里的id FileSaveType=1,对应exp_localdetail里的id |
| 5 | `syntype` | 同步方式 | `char` | 1 | 是 | 0,手动;1,自动 |
| 6 | `timemodul` | 同步间隔时间 | `char` | 1 | 是 | 0：周  1：月  2：年  3：天 |
| 7 | `frequency` | 星期 | `integer` | - | 是 | 1：周一  2：周二  3：周三  4：周四  5：周五  6：周六  7：周日 |
| 8 | `frequencyy` | 天 | `integer` | - | 是 | 1-28：对应1-28日 |
| 9 | `createtype` | 取值类型 | `char` | 1 | 是 | 0：正数  1：倒数  说明：TimeModul=1或2有效 |
| 10 | `createtime` | 同步时间 | `char` | 8 | 是 | 格式：03:00，表示3点正 |
| 11 | `xmltype` | XML格式类型 | `char` | 1 | 是 | 0,自由格式;1,中信格式 |
| 12 | `xmlecodingtype` | 编码 | `char` | 1 | 是 | - |
| 13 | `xmlfiletype` | 文件信息格式 | `char` | 1 | 是 | 0,ftp路径;1,base64编码 |
| 14 | `xmlhaveremark` | 是否导出签字意见 | `char` | 1 | 是 | - |
| 15 | `xmltext` | xml模板内容 | `varchar2` | 4000 | 是 | - |
| 16 | `expworkflowfileflag` | 是否导出流程表单文档 | `char` | 1 | 是 | - |
| 17 | `expworkflowfileforzipflag` | 是否导出流程表单文档为ZIP | `char` | 1 | 是 | - |
| 18 | `expworkflowremarkfileflag` | 是否导出流转意见文档 | `char` | 1 | 是 | - |
| 19 | `expworkflowremarkfileforzip` | 是否导出流转意见文档为ZIP | `char` | 1 | 是 | - |
| 20 | `expworkflowfilepath` | 导出流程文档路径 | `varchar2` | 1000 | 是 | - |
| 21 | `expworkflowinfoflag` | 是否导出流程表单 | `char` | 1 | 是 | - |
| 22 | `expworkflowinfopath` | 导出流程表单路径 | `varchar2` | 1000 | 是 | - |
| 23 | `expworkflowremarkflag` | 是否导出流转意见 | `char` | 1 | 是 | - |
| 24 | `expsignfileflag` | 是否导出签章图片 | `char` | 1 | 是 | - |
| 25 | `expsignfilepath` | 导出签章图片路径 | `varchar2` | 1000 | 是 | - |
