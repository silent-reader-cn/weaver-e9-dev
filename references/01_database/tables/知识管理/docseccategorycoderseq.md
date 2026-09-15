# 泛微OA 数据表: `docseccategorycoderseq`

- **所属模块**: `知识管理`
- **数据库表名**: `docseccategorycoderseq`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `sequence` | 流水号 | `integer` | - | 是 | - |
| 3 | `yearseq` | 如果日期单独流水且为年的情况下将使用这里的信息 | `integer` | - | 是 | - |
| 4 | `monthseq` | 如果日期单独流水且为月的情况下将使用这里的信息 | `integer` | - | 是 | - |
| 5 | `dayseq` | 如果日期单独流水且为日的情况下将使用这里的信息 | `integer` | - | 是 | - |
| 6 | `seccategoryid` | 子目录id | `integer` | - | 是 | -1表示所有非子目录单独流水公用的流水号，子目录单独流水则对应相应的子目录id |
| 7 | `isuse` | 是否有效 | `char` | 1 | 是 | - |
