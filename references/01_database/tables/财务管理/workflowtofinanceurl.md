# 泛微OA 数据表: `workflowtofinanceurl`

- **中文名称**: 财务凭证流程推送记录表
- **所属模块**: `财务管理`
- **数据库表名**: `workflowtofinanceurl`
- **主键**: `id`
- **字段数**: `12`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `guid1` | uuid | `varchar2` | 50 | 是 | 否 | 否 | - | - | - |
| 3 | `sendurl` | 推送url | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 4 | `requestid` | 流程reqid | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `fnavoucherxmlid` | 凭证配置表id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `createdate` | 创建日期 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 7 | `createtime` | 创建时间 | `char` | 8 | 是 | 否 | 否 | - | - | - |
| 8 | `xmlsend` | 推送xml | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 9 | `requestids` | 流程reqids | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 10 | `xmlreceive` | 接口返回xml | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 11 | `xmlobjsend` | 推送xml序列化对象 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 12 | `xmlobjreceive` | 接口返回xml序列化对象 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
