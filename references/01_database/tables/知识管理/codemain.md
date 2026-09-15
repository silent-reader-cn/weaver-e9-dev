# 泛微OA 数据表: `codemain`

- **所属模块**: `知识管理`
- **数据库表名**: `codemain`
- **字段总数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 是 | - |
| 2 | `titleimg` | 编码图像 | `varchar2` | 320 | 是 | - |
| 3 | `titlename` | 编码主题 | `varchar2` | 160 | 是 | - |
| 4 | `isuse` | 是否有效 | `char` | 1 | 是 | - |
| 5 | `allowstr` | 权限字符串 | `varchar2` | 160 | 是 | - |
| 6 | `secdoccodealone` | 是否子文档单独编码 | `char` | 1 | 是 | 1：是，0：不是 |
| 7 | `seccategoryseqalone` | 是否子目录单独流水 | `char` | 1 | 是 | 1：是，0：不是 |
| 8 | `dateseqalone` | 是否日期单独流水 | `char` | 1 | 是 | 1：是，0：不是 |
| 9 | `dateseqselect` | 日期单独流水方式 | `char` | 1 | 是 | 1：年，2：月，3：日 |
| 10 | `seccategoryid` | 子目录id | `integer` | - | 是 | - |
| 11 | `docseccategorytemplateid` | 目录模版id | `integer` | - | 是 | - |
