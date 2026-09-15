# 泛微OA 数据表: `crm_detailpagetabconfig`

- **所属模块**: `客户管理`
- **数据库表名**: `crm_detailpagetabconfig`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | id |
| 2 | `name` | 栏目名称 | `varchar2` | 1000 | 是 | 栏目名称 |
| 3 | `linkurl` | 内部链接 | `varchar2` | 1000 | 是 | 内部链接 |
| 4 | `isopen` | 是否启用 | `integer` | - | 是 | 是否启用 |
| 5 | `type` | 类型 | `integer` | - | 是 | 类型 |
| 6 | `deleted` | 是否删除 | `integer` | - | 是 | 1：删除；0：未删除 |
| 7 | `dsporder` | 0 | `integer` | - | 是 | 0 |
| 8 | `candel` | 能否删除 | `integer` | - | 是 | 能否删除 |
| 9 | `shortname` | 简称 | `varchar2` | 400 | 是 | 简称 |
| 10 | `isdefault` | 默认选中 | `integer` | - | 是 | 1：选中 |
