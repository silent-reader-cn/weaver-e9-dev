# 泛微OA 数据表: `docseccategorydocproperty`

- **所属模块**: `知识管理`
- **数据库表名**: `docseccategorydocproperty`
- **字段总数**: `16`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `seccategoryid` | 子目录id | `integer` | - | 是 | - |
| 3 | `viewindex` | 显示顺序 | `integer` | - | 是 | - |
| 4 | `type` | 类型 | `integer` | - | 是 | - |
| 5 | `labelid` | 标签id | `integer` | - | 是 | - |
| 6 | `visible` | 是否显示 | `integer` | - | 是 | - |
| 7 | `customname` | 自定义名称 | `varchar2` | 800 | 是 | - |
| 8 | `columnwidth` | 列宽 | `integer` | - | 是 | - |
| 9 | `mustinput` | 是否必填 | `integer` | - | 是 | - |
| 10 | `iscustom` | 是否自定义 | `integer` | - | 是 | - |
| 11 | `scope` | 自定义字段scope | `varchar2` | 50 | 是 | - |
| 12 | `scopeid` | 自定义字段scopeid | `integer` | - | 是 | - |
| 13 | `fieldid` | 自定义字段fieldid | `integer` | - | 是 | - |
| 14 | `docseccategorytemplateid` | 目录模板id | `integer` | - | 是 | - |
| 15 | `customnameeng` | 自定义名称英文 | `varchar2` | 1000 | 是 | - |
| 16 | `customnametran` | 自定义名称繁体中文 | `varchar2` | 1000 | 是 | - |
