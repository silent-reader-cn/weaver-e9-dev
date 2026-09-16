# 泛微OA 数据表: `esb_event_params`

- **所属模块**: `集成模块`
- **数据库表名**: `esb_event_params`
- **文档收录字段数**: `13`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `PARAMNAME` | 参数名称 | `varchar2` | - | - | 参数名称 |
| 2 | `PARAMTYPE` | 参数类型 | `varchar2` | - | - | json、xml、string、int、double、date、datetime |
| 3 | `ARRAY` | 明细 | `char` | - | - | 0、否  1、必须 |
| 4 | `REQUIRED` | 必须 | `char` | - | - | 0、否  1、必须 |
| 5 | `PARENTNAME` | 父节点名称 | `varchar2` | - | - | 上级 |
| 6 | `TRANSMITTYPE` | 类型 | `varchar2` | - | - | url,header,request,response |
| 7 | `DESCRIPTION` | 描述 | `varchar2` | - | - | - |
| 8 | `EVENTID` | 事件标识 | `varchar2` | - | - | - |
| 9 | `DATATYPE` | 数据类型 | `varchar2` | - | - | node,attribute |
| 10 | `LEVELS` | 等级 | `varchar2` | - | - | 00#01 |
| 11 | `PARAMKEY` | 参数关键字 | `varchar2` | - | - | PARENTNAME+PARAMNAME |
| 12 | `EXT` | 扩展字段 | `varchar2` | - | - | - |
| 13 | `CLASSNAME` | 类名 | `varchar2` | - | - | - |
