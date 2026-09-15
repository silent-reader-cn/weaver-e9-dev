# 泛微OA 数据表: `ecologyuplist`

- **所属模块**: `版本升级`
- **数据库表名**: `ecologyuplist`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | - |
| 2 | `label` | 补丁包编号 | `varchar2` | 800 | 是 | - |
| 3 | `versionno` | 补丁包号（全称） | `varchar2` | 1000 | 是 | - |
| 4 | `content` | 补丁包内容 | `varchar2` | 2000 | 是 | - |
| 5 | `operationdate` | 补丁包升级日期 | `varchar2` | 800 | 是 | - |
| 6 | `operationtime` | 补丁包升级时间 | `varchar2` | 800 | 是 | - |
| 7 | `configcontent` | 补丁包配置内容 | `varchar2` | 2000 | 是 | - |
