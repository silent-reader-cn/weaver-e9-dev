# 泛微OA 数据表: `hrm_searchselectitem`

- **所属模块**: `人力资源`
- **数据库表名**: `hrm_searchselectitem`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `fieldid` | 字段id | `integer` | - | 是 | - |
| 3 | `selectvalue` | 选项值 | `varchar2` | 400 | 是 | - |
| 4 | `selectname` | 选项名 | `varchar2` | 1000 | 是 | - |
| 5 | `listorder` | 列表顺序 | `number` | (10,0) | 是 | - |
| 6 | `isdefault` | 是否默认 | `char` | 1 | 是 | - |
| 7 | `cancel` | 可取消 | `varchar2` | 8 | 是 | - |
