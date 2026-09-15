# 泛微OA 数据表: `esb_event`

- **所属模块**: `集成模块`
- **数据库表名**: `esb_event`
- **字段总数**: `15`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `EVENTID` | 事件标识 | `varchar2` | 800 | - | 事件标识 |
| 2 | `EVENTNAME` | 事件名称 | `varchar2` | 800 | - | 事件名称 |
| 3 | `EVENTTYPE` | 事件类型 | `varchar2` | 800 | - | 1、业务触发  2、监听JMS消息  3、监听AMQP消息 |
| 4 | `CONFIG` | 配置参数 | `clob` | - | - | - |
| 5 | `EVENTSTATUS` | 事件状态 | `varchar2` | 800 | - | 1、发布  2、封存  3、维护 |
| 6 | `PRODUCTCODE` | 所属产品 | `varchar2` | 800 | - | 所属产品 |
| 7 | `MODULECODE` | 所属模块 | `varchar2` | 800 | - | 所属模块 |
| 8 | `RESID` | 所属资源 | `varchar2` | 800 | - | 所属资源 |
| 9 | `DATAFORMART` | 数据格式 | `varchar2` | 800 | - | 1、JSON  2、XML |
| 10 | `INSTRUCTION` | 说明 | `clob` | - | - | 说明 |
| 11 | `CREATEDATE` | 创建日期 | `varchar2` | 80 | - | 创建日期 |
| 12 | `CREATETIME` | 创建时间 | `varchar2` | 80 | - | 创建时间 |
| 13 | `MODIFYDATE` | 修改日期 | `varchar2` | 80 | - | 修改日期 |
| 14 | `MODIFYTIME` | 修改时间 | `varchar2` | 80 | - | 修改时间 |
| 15 | `lasttime` | 最后运行时间 | `varchar2` | 50 | - | 最后运行时间 |
