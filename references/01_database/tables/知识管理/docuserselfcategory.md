# 泛微OA 数据表: `docuserselfcategory`

- **所属模块**: `知识管理`
- **数据库表名**: `docuserselfcategory`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `userid` | 用户id | `integer` | - | 是 | - |
| 3 | `name` | 目录名称 | `varchar2` | 1000 | 是 | - |
| 4 | `parentid` | 上级目录id | `integer` | - | 是 | - |
| 5 | `parentids` | 目录结构id字符串 | `varchar2` | 1000 | 是 | - |
| 6 | `createdate` | 创建日期 | `varchar2` | 80 | 是 | - |
| 7 | `createtime` | 创建时间 | `varchar2` | 64 | 是 | - |
