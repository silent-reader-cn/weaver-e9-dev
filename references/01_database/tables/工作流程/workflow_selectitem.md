# 泛微OA 数据表: `workflow_selectitem`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_selectitem`
- **字段总数**: `13`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `fieldid` | 字段id | `integer` | - | 是 | - |
| 2 | `isbill` | 是否为单据 | `integer` | - | 是 | - |
| 3 | `selectvalue` | 下拉框的值 | `integer` | - | 是 | - |
| 4 | `selectname` | 下拉框名称 | `varchar2` | 1000 | 是 | - |
| 5 | `id` | 5 | `integer` | - | 是 | - |
| 6 | `listorder` | 列表顺序 | `number` | (10,2) | 是 | - |
| 7 | `isdefault` | 是否为默认 | `char` | 1 | 是 | - |
| 8 | `docpath` | 文档路径 | `varchar2` | 1000 | 是 | - |
| 9 | `doccategory` | 文档分类 | `varchar2` | 1000 | 是 | - |
| 10 | `isaccordtosubcom` | 是否与下属机构相关 | `char` | 1 | 是 | - |
| 11 | `childitemid` | 子条目id | `varchar2` | 2000 | 是 | - |
| 12 | `cancel` | 取消 | `varchar2` | 8 | 是 | - |
| 13 | `pubid` | 父条目id | `integer` | - | 是 | - |
