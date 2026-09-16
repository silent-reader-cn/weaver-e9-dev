# 泛微OA 数据表: `exp_dbprosettings`

- **中文名称**: 数据库方案设置信息保存表
- **所属模块**: `集成模块`
- **数据库表名**: `exp_dbprosettings`
- **主键**: `id`
- **字段数**: `31`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `dwdmapfiletype` | 流程表单文档 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 2 | `mwdmapfiletype` | 流程表单多文档 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 3 | `remarkwdmapfiletype` | 流转意见文档 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 4 | `remarkfjmapfiletype` | 流转意见附件 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 5 | `bdmapfiletype` | 流程表单 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 6 | `id` | 主键 | `integer` | - | 否 | 否 | 是 | - | - | - |
| 7 | `name` | 方案名称 | `varchar2` | 1000 | 否 | 否 | 否 | - | - | - |
| 8 | `filesavetype` | 文件保存方式 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 9 | `regittype` | 方案类型 | `integer` | - | 是 | 否 | 否 | - | - | FileSaveType=0,对应exp_ftpdetail里的id FileSaveType=1,对应exp_localdetail里的id |
| 10 | `exptabletype` | 文档存储数据类型 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 11 | `syntype` | 同步方式 | `char` | 1 | 是 | 否 | 否 | - | - | 0,手动;1,自动 |
| 12 | `timemodul` | 同步间隔时间 | `char` | 1 | 是 | 否 | 否 | - | - | 0：周 1：月 2：年 3：天 |
| 13 | `frequency` | 星期 | `integer` | - | 是 | 否 | 否 | - | - | 1：周一 2：周二 3：周三 4：周四 5：周五 6：周六 7：周日 |
| 14 | `frequencyy` | 天 | `integer` | - | 是 | 否 | 否 | - | - | 1-28：对应1-28日 |
| 15 | `createtype` | 取值类型 | `char` | 1 | 是 | 否 | 否 | - | - | 0：正数 1：倒数 说明：TimeModul=1或2有效 |
| 16 | `createtime` | 同步时间 | `char` | 8 | 是 | 否 | 否 | - | - | 格式：03:00，表示3点正 |
| 17 | `regitdbid` | 数据库保存方案id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 18 | `maintablekeytype` | 主表主键生成规则 | `char` | 1 | 是 | 否 | 否 | - | - | 0,自增长;1,UUID;2,时间戳 |
| 19 | `dttablekeytype` | 明细表主键生成规则 | `char` | 1 | 是 | 否 | 否 | - | - | 0,自增长;1,UUID;2,时间戳 |
| 20 | `expworkflowfileflag` | 是否导出流程表单文档 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 21 | `expworkflowfileforzipflag` | 是否导出流程表单文档为ZIP | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 22 | `expworkflowremarkfileflag` | 是否导出流转意见文档 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 23 | `expworkflowremarkfileforzip` | 是否导出流转意见文档为ZIP | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 24 | `expworkflowfilepath` | 导出流程文档路径 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 25 | `expworkflowinfoflag` | 是否导出流程表单 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 26 | `expworkflowinfopath` | 导出流程表单路径 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 27 | `expworkflowremarkflag` | 是否导出流转意见 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 28 | `expsignfileflag` | 是否导出签章图片 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 29 | `expsignfilepath` | 导出签章图片路径 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 30 | `zwmapfiletype` | 流程表单正文 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 31 | `fjmapfiletype` | 流程表单附件 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
