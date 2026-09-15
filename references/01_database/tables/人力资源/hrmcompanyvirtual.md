# 泛微OA 数据表: `hrmcompanyvirtual`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmcompanyvirtual`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `companyname` | 总部名称 | `varchar2` | 1000 | 是 | 总部名称 |
| 3 | `companycode` | 总部机构代码 | `varchar2` | 1000 | 是 | 总部机构代码 |
| 4 | `companydesc` | 总部描述 | `varchar2` | 1000 | 是 | 总部描述 |
| 5 | `canceled` | 是否封存 | `integer` | - | 是 | 是否封存 |
| 6 | `showorder` | 序列号 | `integer` | - | 是 | 序列号 |
| 7 | `virtualtype` | 虚拟类型 | `varchar2` | 1000 | 是 | 虚拟类型 |
| 8 | `virtualtypedesc` | 虚拟类型描述 | `varchar2` | 800 | 是 | 虚拟类型描述 |
