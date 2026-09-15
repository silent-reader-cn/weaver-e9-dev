# 泛微OA 数据表: `cptstockinmain`

- **所属模块**: `资产管理`
- **数据库表名**: `cptstockinmain`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 标识id | `integer` | - | 否 | 标识列 |
| 2 | `invoice` | 发票号 | `varchar2` | 640 | 是 | 发票号 |
| 3 | `buyerid` | 申请人 | `integer` | - | 是 | 申请人 |
| 4 | `supplierid` | 供应商 | `integer` | - | 是 | 供应商 |
| 5 | `checkerid` | 验收人 | `integer` | - | 是 | 验收人 |
| 6 | `stockindate` | 入库日期 | `char` | 10 | 是 | 入库日期 |
| 7 | `ischecked` | 是否已验收 | `integer` | - | 是 | 是否已验收 |
| 8 | `stockindept` | 入库部门 | `integer` | - | 是 | 入库部门 |
