# 泛微OA 数据表: `fnavoucherxmlcontentdset`

- **中文名称**: 预算凭证xml节点设置信息表
- **所属模块**: `财务管理`
- **数据库表名**: `fnavoucherxmlcontentdset`
- **主键**: `id`
- **字段数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `fnavoucherxmlid` | fnavoucherxml.id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `fnavoucherxmlcontentid` | fnavoucherxmlcontent.id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `dsetalias` | 数据集别名 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 5 | `inittiming` | 初始化时机 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `fnadatasetid` | 数据集id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `dsetmemo` | 数据集备注 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 8 | `orderid` | 排序id | `number` | (5,2) | 是 | 否 | 否 | - | - | - |
| 9 | `parameter` | 参数字符串 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
