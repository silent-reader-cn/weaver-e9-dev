# 泛微OA 数据表: `esb_event_params`

- **中文名称**: ESB事件参数维护表
- **所属模块**: `集成模块`
- **数据库表名**: `esb_event_params`
- **主键**: `无`
- **字段数**: `13`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `PARAMNAME` | 参数名称 | `varchar2` | - | 是 | 否 | 否 | - | - | 参数名称 |
| 2 | `PARAMTYPE` | 参数类型 | `varchar2` | - | 是 | 否 | 否 | - | - | json、xml、string、int、double、date、datetime |
| 3 | `ARRAY` | 明细 | `char` | - | 是 | 否 | 否 | - | - | 0、否 1、必须 |
| 4 | `REQUIRED` | 必须 | `char` | - | 是 | 否 | 否 | - | - | 0、否 1、必须 |
| 5 | `PARENTNAME` | 父节点名称 | `varchar2` | - | 是 | 否 | 否 | - | - | 上级 |
| 6 | `TRANSMITTYPE` | 类型 | `varchar2` | - | 是 | 否 | 否 | - | - | url,header,request,response |
| 7 | `DESCRIPTION` | 描述 | `varchar2` | - | 是 | 否 | 否 | - | - | - |
| 8 | `EVENTID` | 事件标识 | `varchar2` | - | 否 | 否 | 否 | - | - | - |
| 9 | `DATATYPE` | 数据类型 | `varchar2` | - | 是 | 否 | 否 | - | - | node,attribute |
| 10 | `LEVELS` | 等级 | `varchar2` | - | 是 | 否 | 否 | - | - | 00#01 |
| 11 | `PARAMKEY` | 参数关键字 | `varchar2` | - | 是 | 否 | 否 | - | - | PARENTNAME+PARAMNAME |
| 12 | `EXT` | 扩展字段 | `varchar2` | - | 是 | 否 | 否 | - | - | - |
| 13 | `CLASSNAME` | 类名 | `varchar2` | - | 是 | 否 | 否 | - | - | - |
