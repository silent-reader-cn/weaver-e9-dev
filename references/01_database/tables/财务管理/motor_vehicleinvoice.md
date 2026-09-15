# 泛微OA 数据表: `motor_vehicleinvoice`

- **所属模块**: `财务管理`
- **数据库表名**: `motor_vehicleinvoice`
- **字段总数**: `13`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | - | - |
| 2 | `mainid` | 发票台账id | `integer` | - | - | - |
| 3 | `machine_code` | 机打代码 | `varchar2` | 200 | - | - |
| 4 | `machine_number` | 机打号码 | `varchar2` | 200 | - | - |
| 5 | `pretax_amount` | 税前金额 | `varchar2` | 200 | - | - |
| 6 | `seller_tax_id` | 销售单位纳税人识别号 | `varchar2` | 200 | - | - |
| 7 | `buyer_id` | 买方单位代码/个人身份证号 | `varchar2` | 200 | - | - |
| 8 | `tax_authorities` | 主管税务机关 | `varchar2` | 1000 | - | - |
| 9 | `tax_authorities_code` | 主管税务机关代码 | `varchar2` | 200 | - | - |
| 10 | `car_code` | 车架号/车辆识别代码 | `varchar2` | 200 | - | - |
| 11 | `car_engine_code` | 发动机号码 | `varchar2` | 200 | - | - |
| 12 | `car_model` | 厂牌型号 | `varchar2` | 1000 | - | - |
| 13 | `certificate_number` | 合格证号 | `varchar2` | 200 | - | - |
