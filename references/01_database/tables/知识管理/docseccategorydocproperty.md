# 泛微OA 数据表: `docseccategorydocproperty`

- **中文名称**: 文档目录属性表
- **所属模块**: `知识管理`
- **数据库表名**: `docseccategorydocproperty`
- **主键**: `id`
- **字段数**: `16`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 是 | - | - | - |
| 2 | `seccategoryid` | 子目录id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `viewindex` | 显示顺序 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `type` | 类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `labelid` | 标签id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `visible` | 是否显示 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `customname` | 自定义名称 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 8 | `columnwidth` | 列宽 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 9 | `mustinput` | 是否必填 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 10 | `iscustom` | 是否自定义 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 11 | `scope` | 自定义字段scope | `varchar2` | 50 | 是 | 否 | 否 | - | - | - |
| 12 | `scopeid` | 自定义字段scopeid | `integer` | - | 是 | 否 | 否 | - | - | - |
| 13 | `fieldid` | 自定义字段fieldid | `integer` | - | 是 | 否 | 否 | - | - | - |
| 14 | `docseccategorytemplateid` | 目录模板id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 15 | `customnameeng` | 自定义名称英文 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 16 | `customnametran` | 自定义名称繁体中文 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
