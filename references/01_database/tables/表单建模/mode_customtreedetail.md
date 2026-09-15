# 泛微OA 数据表: `mode_customtreedetail`

- **所属模块**: `表单建模`
- **数据库表名**: `mode_customtreedetail`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `mainid` | 树形id | `integer` | - | 是 | 对应mode_customtree表的id |
| 3 | `nodename` | 名称 | `varchar2` | 1000 | 是 | - |
| 4 | `nodedesc` | 描述 | `varchar2` | 4000 | 是 | - |
| 5 | `sourcefrom` | 数据来源 | `integer` | - | 是 | - |
