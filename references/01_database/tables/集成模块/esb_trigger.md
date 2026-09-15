# 泛微OA 数据表: `esb_trigger`

- **所属模块**: `集成模块`
- **数据库表名**: `esb_trigger`
- **字段总数**: `12`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `triggerid` | 触发标识 | `varchar2` | 100 | 否 | 触发标识 |
| 2 | `publishid` | 发布服务标识 | `varchar2` | 800 | 是 | 发布服务标识 |
| 3 | `triggertype` | 触发类型 | `varchar2` | 800 | 是 | 触发类型 |
| 4 | `resourceid` | 资源标识 | `varchar2` | 800 | 是 | 资源标识 |
| 5 | `config` | 配置信息 | `clob` | 4000 | 是 | 配置信息 |
| 6 | `description` | 说明 | `varchar2` | 1000 | 是 | 说明 |
| 7 | `state` | 状态 | `char` | 1 | 是 | 1:启用，0:未启用 |
| 8 | `version` | 版本号 | `integer` | - | 是 | 版本号 |
| 9 | `createdate` | 创建日期 | `varchar2` | 80 | 是 | 创建日期 |
| 10 | `createtime` | 创建时间 | `varchar2` | 80 | 是 | 创建时间 |
| 11 | `modifydate` | 修改日期 | `varchar2` | 80 | 是 | 修改日期 |
| 12 | `modifytime` | 修改时间 | `varchar2` | 80 | 是 | 修改时间 |
