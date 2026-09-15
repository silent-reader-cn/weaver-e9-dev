# 泛微OA 数据表: `second_carinvoice`

- **所属模块**: `财务管理`
- **数据库表名**: `second_carinvoice`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | - | - |
| 2 | `mainid` | 发票台账id | `integer` | - | - | - |
| 3 | `seller_id` | 卖方单位代码/个人身份证号 | `varchar2` | 200 | - | - |
| 4 | `buyer_id` | 买方单位代码/个人身份证号 | `varchar2` | 200 | - | - |
| 5 | `company_name` | 二手车市场 | `varchar2` | 1000 | - | - |
| 6 | `company_tax_id` | 二手车市场纳税人识别号 | `varchar2` | 200 | - | - |
| 7 | `license_plate` | 车牌号 | `varchar2` | 200 | - | - |
| 8 | `registration_number` | 登记证号 | `varchar2` | 200 | - | - |
| 9 | `car_code` | 车架号/车辆识别代码 | `varchar2` | 200 | - | - |
| 10 | `car_model` | 厂牌型号 | `varchar2` | 1000 | - | - |
