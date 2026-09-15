# 泛微OA 数据表: `machineinvoice`

- **所属模块**: `财务管理`
- **数据库表名**: `machineinvoice`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | - | - |
| 2 | `mainid` | 发票台账id | `integer` | - | - | - |
| 3 | `time` | 时间 | `varchar2` | 200 | - | - |
| 4 | `category` | 种类 | `varchar2` | 200 | - | - |
| 5 | `seller_tax_id` | 销售方纳税人识别号 | `varchar2` | 200 | - | - |
| 6 | `buyer_tax_id` | 购买方纳税人识别号 | `varchar2` | 200 | - | - |
