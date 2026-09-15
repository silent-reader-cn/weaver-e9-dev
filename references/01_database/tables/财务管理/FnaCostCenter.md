# 泛微OA 数据表: `FnaCostCenter`

- **所属模块**: `财务管理`
- **数据库表名**: `FnaCostCenter`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `supfccid` | 上级id | `integer` | - | 是 | - |
| 3 | `type` | 类型 | `integer` | - | 是 | 0:成本中心类别； 1：成本中心； |
| 4 | `name` | 名称 | `varchar2` | 600 | 是 | - |
| 5 | `code` | 编码 | `char` | 50 | 是 | - |
| 6 | `archive` | 封存 | `integer` | - | 是 | 0、null：未封存；1：封存； |
| 7 | `description` | 描述 | `varchar2` | 4000 | 是 | - |
