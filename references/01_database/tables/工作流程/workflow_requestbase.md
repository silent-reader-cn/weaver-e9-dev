# 泛微OA 数据表: `workflow_requestbase`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_requestbase`
- **字段总数**: `19`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `totalgroups` | 总共需要的操作者组数 | `integer` | - | 是 | - |
| 2 | `requestname` | 请求名称 | `varchar2` | 1000 | 是 | - |
| 3 | `creater` | 创建人 | `integer` | - | 是 | - |
| 4 | `createdate` | 创建日期 | `char` | 10 | 是 | - |
| 5 | `createtime` | 创建时间 | `char` | 8 | 是 | - |
| 6 | `lastoperator` | 最后操作者id | `integer` | - | 是 | - |
| 7 | `lastoperatedate` | 最后操作日期 | `char` | 10 | 是 | - |
| 8 | `lastoperatetime` | 最后操作时间 | `char` | 8 | 是 | - |
| 9 | `deleted` | 是否删除 | `integer` | - | 是 | 0：是 |
| 10 | `creatertype` | 创建人类型 | `integer` | - | 是 | 1：人力资源，2：客户 |
| 11 | `lastoperatortype` | 最后操作者类型 | `integer` | - | 是 | 1：人力资源，2：客户 |
| 12 | `nodepasstime` | 节点超时时间 | `float` | 22 | 是 | 小时 |
| 13 | `nodelefttime` | 节点处理剩余时间 | `float` | 22 | 是 | 小时 |
| 14 | `docids` | 相关文档 | `varchar2` | 4000 | 是 | - |
| 15 | `crmids` | 相关客户 | `varchar2` | 4000 | 是 | - |
| 16 | `hrmids_temp` | temp | `varchar2` | 4000 | 是 | - |
| 17 | `prjids` | 相关项目 | `varchar2` | 4000 | 是 | - |
| 18 | `cptids` | 相关资产 | `varchar2` | 4000 | 是 | - |
| 19 | `requestlevel` | 请求级别 | `integer` | - | 是 | 0 |
