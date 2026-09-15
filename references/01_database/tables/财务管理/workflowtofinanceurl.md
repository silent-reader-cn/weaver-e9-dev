# 泛微OA 数据表: `workflowtofinanceurl`

- **所属模块**: `财务管理`
- **数据库表名**: `workflowtofinanceurl`
- **字段总数**: `12`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `guid1` | uuid | `varchar2` | 50 | 是 | - |
| 3 | `sendurl` | 推送url | `varchar2` | 4000 | 是 | - |
| 4 | `requestid` | 流程reqid | `integer` | - | 是 | - |
| 5 | `fnavoucherxmlid` | 凭证配置表id | `integer` | - | 是 | - |
| 6 | `createdate` | 创建日期 | `char` | 10 | 是 | - |
| 7 | `createtime` | 创建时间 | `char` | 8 | 是 | - |
| 8 | `xmlsend` | 推送xml | `clob` | 4000 | 是 | - |
| 9 | `requestids` | 流程reqids | `clob` | 4000 | 是 | - |
| 10 | `xmlreceive` | 接口返回xml | `clob` | 4000 | 是 | - |
| 11 | `xmlobjsend` | 推送xml序列化对象 | `clob` | 4000 | 是 | - |
| 12 | `xmlobjreceive` | 接口返回xml序列化对象 | `clob` | 4000 | 是 | - |
