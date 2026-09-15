# 泛微OA 数据表: `cpt_specialfield`

- **所属模块**: `资产管理`
- **数据库表名**: `cpt_specialfield`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 标识id | `integer` | - | 否 | 标识列 |
| 2 | `fieldid` | 字段id | `integer` | - | 是 | 字段id |
| 3 | `displayname` | 显示名称 | `varchar2` | 1000 | 是 | 显示名称 |
| 4 | `linkaddress` | 链接url | `varchar2` | 1000 | 是 | 链接url |
| 5 | `descriptivetext` | 描述文字 | `varchar2` | 2000 | 是 | 描述文字 |
| 6 | `isbill` | 备用字段 | `integer` | - | 是 | 备用字段 |
| 7 | `isform` | 备用字段 | `integer` | - | 是 | 备用字段 |
