# 泛微OA 数据表: `matrixfieldinfo`

- **所属模块**: `人力资源`
- **数据库表名**: `matrixfieldinfo`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `matrixid` | 矩阵id | `integer` | - | 是 | 矩阵id |
| 3 | `browsertypeid` | 浏览按钮类型id | `integer` | - | 是 | 浏览按钮类型id |
| 4 | `browservalue` | 浏览按钮值 | `varchar2` | 1000 | 是 | 浏览按钮值 |
| 5 | `custombrowser` | 自定义浏览按钮 | `char` | 1 | 是 | 自定义浏览按钮 |
| 6 | `displayname` | 显示名称 | `varchar2` | 800 | 是 | 显示名称 |
| 7 | `fieldname` | 字段名称 | `varchar2` | 800 | 是 | 字段名称 |
| 8 | `fieldtype` | 字段类型 | `char` | 1 | 是 | 字段类型 |
| 9 | `priority` | 优先级 | `integer` | - | 是 | 优先级 |
| 10 | `colwidth` | 列宽 | `integer` | - | 是 | 列宽 |
