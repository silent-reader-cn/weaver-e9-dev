# 泛微OA 数据表: `govern_selectitem`

- **所属模块**: `政务应用`
- **数据库表名**: `govern_selectitem`
- **字段总数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | - |
| 2 | `fieldid` | 字段id | `integer` | - | 是 | govern_field表id |
| 3 | `selectvalue` | 选择项值 | `integer` | - | 是 | - |
| 4 | `selectname` | 选择项显示名称 | `varchar2` | 1000 | 是 | - |
| 5 | `listorder` | 列表顺序 | `number` | (10,0) | 是 | - |
| 6 | `isdefault` | 是否为默认 | `char` | 1 | 是 | - |
| 7 | `docpath` | 文档路径 | `varchar2` | 1000 | 是 | - |
| 8 | `doccategory` | 文档分类 | `varchar2` | 1000 | 是 | - |
| 9 | `isaccordtosubcom` | 是否与下属机构相关 | `char` | 1 | 是 | - |
| 10 | `childitemid` | 子条目ID | `varchar2` | 2000 | 是 | - |
| 11 | `cancel` | 封存标识 | `varchar2` | 1000 | 是 | - |
