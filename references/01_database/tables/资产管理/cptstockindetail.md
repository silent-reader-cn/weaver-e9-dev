# 泛微OA 数据表: `cptstockindetail`

- **所属模块**: `资产管理`
- **数据库表名**: `cptstockindetail`
- **字段总数**: `12`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 标识id | `integer` | - | 否 | 标识列 |
| 2 | `cptstockinid` | 资产入库主表id | `integer` | - | 是 | 资产入库主表id |
| 3 | `cpttype` | 资产资料 | `integer` | - | 是 | 资产资料 |
| 4 | `plannumber` | 入库数量 | `integer` | - | 是 | 入库数量 |
| 5 | `innumber` | 验收数量 | `integer` | - | 是 | 验收数量 |
| 6 | `customerid` | 供应商 | `integer` | - | 是 | 供应商 |
| 7 | `selectdate` | 入库日期 | `char` | 10 | 是 | 入库日期 |
| 8 | `capitalspec` | 规格 | `varchar2` | 480 | 是 | 规格 |
| 9 | `location` | 存放地点 | `varchar2` | 800 | 是 | 存放地点 |
| 10 | `invoice` | 发票号 | `varchar2` | 640 | 是 | 发票号 |
| 11 | `price` | 单价 | `number` | (15,2) | 是 | 单价 |
| 12 | `contractno` | 合同号 | `varchar2` | 800 | 是 | 合同号 |
