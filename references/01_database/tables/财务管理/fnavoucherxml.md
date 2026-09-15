# 泛微OA 数据表: `fnavoucherxml`

- **所属模块**: `财务管理`
- **数据库表名**: `fnavoucherxml`
- **字段总数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `xmlname` | 名称 | `char` | 100 | 是 | - |
| 3 | `xmlmemo` | 备注 | `varchar2` | 4000 | 是 | - |
| 4 | `xmlversion` | 版本号 | `char` | 10 | 是 | - |
| 5 | `xmlencoding` | 编码字符串 | `char` | 50 | 是 | - |
| 6 | `workflowid` | wfid | `integer` | - | 是 | - |
| 7 | `typename` | 凭证类型名称 | `varchar2` | 400 | 是 | - |
| 8 | `datasourceid` | oa外部数据源id | `varchar2` | 1000 | 是 | - |
| 9 | `interfacesaddress` | 凭证接口地址 | `varchar2` | 4000 | 是 | - |
| 10 | `profession` | 作废 | `integer` | - | 是 | - |
| 11 | `easpackage` | eas类包路径 | `varchar2` | 500 | 是 | - |
