# 泛微OA 数据表: `ofs_setting`

- **所属模块**: `集成模块`
- **数据库表名**: `ofs_setting`
- **字段总数**: `15`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `messagetypeid` | 消息类型 | `integer` | - | 是 | 在mobile后台注册的消息类型id（标识码） |
| 2 | `remindemessage` | emessage消息推送开关 | `integer` | - | 是 | 1：是 0：否，默认值 |
| 3 | `remindebridge` | ebridge消息推送开关 | `integer` | - | 是 | 1：是 0：否，默认值 |
| 4 | `remindebridgetemplate` | ebridge消息消息模板 | `varchar2` | 1000 | 是 | remindebridge消息模板 |
| 5 | `isuse` | 是否启用 | `integer` | - | 否 | 1：是 0：否，默认值 |
| 6 | `oashortname` | 显示OA系统简称 | `varchar2` | 50 | 是 | 显示OA系统简称 |
| 7 | `oafullname` | 显示OA系统全称 | `varchar2` | 100 | 是 | 显示OA系统全称 |
| 8 | `showsysname` | 显示异构系统名称 | `varchar2` | 1000 | 是 | 0：不显示：不显示异构系统名称 1：简称：显示异构系统简称 2：全称：显示异构系统全称 |
| 9 | `showdone` | 显示已办事宜 | `integer` | - | 是 | 1：是 0：否，默认值 |
| 10 | `remindim` | im推送开关 | `integer` | - | 是 | 1：是 0：否，默认值 |
| 11 | `remindapp` | emessage消息推送开关 | `integer` | - | 是 | 1：是 0：否，默认值 |
| 12 | `modifier` | 修改人 | `integer` | - | 是 | 修改人 |
| 13 | `modifydate` | 修改日期，格式：yyyy-MM-dd | `varchar2` | 80 | 是 | 修改日期，格式：yyyy-MM-dd |
| 14 | `modifytime` | 修改时间，格式：hh24:mm:ss | `varchar2` | 80 | 是 | 修改时间，格式：hh24:mm:ss |
| 15 | `remindoa` | oa消息推送开关 | `integer` | - | 是 | 1：是 0：否，默认值 |
