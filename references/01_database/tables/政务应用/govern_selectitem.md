# 泛微OA 数据表: `govern_selectitem`

- **中文名称**: 督查督办下拉框字段表
- **所属模块**: `政务督办采编`
- **数据库表名**: `govern_selectitem`
- **主键**: `id`
- **字段数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | id | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `fieldid` | 字段id | `integer` | - | 是 | 否 | 否 | - | - | govern_field表id |
| 3 | `selectvalue` | 选择项值 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `selectname` | 选择项显示名称 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 5 | `listorder` | 列表顺序 | `number` | (10,0) | 是 | 否 | 否 | - | - | - |
| 6 | `isdefault` | 是否为默认 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 7 | `docpath` | 文档路径 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 8 | `doccategory` | 文档分类 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 9 | `isaccordtosubcom` | 是否与下属机构相关 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 10 | `childitemid` | 子条目ID | `varchar2` | 2000 | 是 | 否 | 否 | - | - | - |
| 11 | `cancel` | 封存标识 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
