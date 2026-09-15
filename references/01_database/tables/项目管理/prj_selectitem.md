# 泛微OA 数据表: `prj_selectitem`

- **所属模块**: `项目管理`
- **数据库表名**: `prj_selectitem`
- **字段总数**: `12`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `fieldid` | 字段id | `integer` | - | 是 | 字段id |
| 2 | `isbill` | 备用字段 | `integer` | - | 是 | 备用字段 |
| 3 | `selectvalue` | 选项值 | `integer` | - | 是 | 选项值 |
| 4 | `selectname` | 选项显示名称 | `varchar2` | 1000 | 是 | 选项显示名称 |
| 5 | `id` | 标识id | `integer` | - | 否 | 标识列 |
| 6 | `listorder` | 顺序 | `number` | (10,0) | 是 | 顺序 |
| 7 | `isdefault` | 是否默认 | `char` | 1 | 是 | 是否默认 |
| 8 | `docpath` | 备用字段 | `varchar2` | 1000 | 是 | 备用字段 |
| 9 | `doccategory` | 备用字段 | `varchar2` | 1000 | 是 | 备用字段 |
| 10 | `isaccordtosubcom` | 备用字段 | `char` | 1 | 是 | 备用字段 |
| 11 | `childitemid` | 备用字段 | `varchar2` | 2000 | 是 | 备用字段 |
| 12 | `cancel` | 是否取消 | `varchar2` | 8 | 是 | 是否取消 |
