# 泛微OA 数据表: `crm_customertypepersonal`

- **中文名称**: 客户分类定制
- **所属模块**: `客户管理`
- **数据库表名**: `crm_customertypepersonal`
- **主键**: `无`
- **字段数**: `3`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `userid` | 人员id | `integer` | - | 是 | 否 | 否 | - | - | 人员id |
| 2 | `maintype` | 主分类 | `integer` | - | 是 | 否 | 否 | - | - | 0为type；1为description；2为status；3为size |
| 3 | `subtype` | 子分类 | `integer` | - | 是 | 否 | 否 | - | - | 0为type；1为description；2为status；3为size |
