# 泛微OA 数据表: `cus_formfield`

- **所属模块**: `知识管理`
- **数据库表名**: `cus_formfield`
- **字段总数**: `13`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `scope` | 范围 | `varchar2` | 50 | 否 | 文档对应：doccustomfieldbyseccategory |
| 2 | `scopeid` | 范围id | `integer` | - | 否 | scope为doccustomfieldbyseccategory时，该值为文档目录id |
| 3 | `fieldlable` | 字段显示名 | `varchar2` | 800 | 是 | - |
| 4 | `fieldid` | 字段id | `integer` | - | 否 | - |
| 5 | `fieldorder` | 字段顺序 | `integer` | - | 否 | - |
| 6 | `ismand` | 是否必填 | `char` | 1 | 是 | - |
| 7 | `doc_fieldlabel` | 文档字段显示名 | `integer` | - | 是 | - |
| 8 | `prj_isopen` | 项目模块是否启用 | `char` | 1 | 是 | - |
| 9 | `prj_fieldlabel` | 项目字段显示名 | `integer` | - | 是 | - |
| 10 | `isuse` | 是否使用 | `char` | 1 | 是 | - |
| 11 | `groupid` | 组 | `integer` | - | 是 | - |
| 12 | `hrm_fieldlable` | 人力资源字段显示名 | `varchar2` | 1000 | 是 | - |
| 13 | `dmlurl` | 执行的url | `varchar2` | 2000 | 是 | - |
