# 泛微OA 数据表: `favourite`

- **所属模块**: `门户管理`
- **数据库表名**: `favourite`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | - |
| 2 | `resourceid` | 人员id | `integer` | - | 是 | - |
| 3 | `adddate` | 加入时间 | `varchar2` | 160 | 是 | - |
| 4 | `favouritename` | 名称 | `varchar2` | 1000 | 是 | - |
| 5 | `favouritedesc` | 描述 | `varchar2` | 1000 | 是 | - |
| 6 | `displayorder` | 显示顺序 | `integer` | - | 是 | - |
| 7 | `parentid` | 父id | `integer` | - | 是 | - |
