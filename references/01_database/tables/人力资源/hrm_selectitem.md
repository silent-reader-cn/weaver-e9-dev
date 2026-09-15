# 泛微OA 数据表: `hrm_selectitem`

- **所属模块**: `人力资源`
- **数据库表名**: `hrm_selectitem`
- **字段总数**: `12`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `fieldid` | 选择框对应的字段id | `integer` | - | 是 | 选择框对应的字段id |
| 2 | `isbill` | 关联流程 | `integer` | - | 是 | 关联流程 |
| 3 | `selectvalue` | 已选值 | `integer` | - | 是 | 已选值 |
| 4 | `selectname` | 已选名称 | `varchar2` | 1000 | 是 | 已选名称 |
| 5 | `id` | id | `integer` | - | 否 | id |
| 6 | `listorder` | 序列号 | `number` | (10,0) | 是 | 序列号 |
| 7 | `isdefault` | 是否默认 | `char` | 1 | 是 | 1默认 |
| 8 | `docpath` | 文档路径 | `varchar2` | 1000 | 是 | 文档路径 |
| 9 | `doccategory` | 文档类别 | `varchar2` | 1000 | 是 | 文档类别 |
| 10 | `isaccordtosubcom` | 与分部一致 | `char` | 1 | 是 | 与分部一致 |
| 11 | `childitemid` | 子类id | `varchar2` | 2000 | 是 | 子类id |
| 12 | `cancel` | 是否启用 | `varchar2` | 8 | 是 | 是否启用，0为关闭 |
