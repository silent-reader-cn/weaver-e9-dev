# 泛微OA 数据表: `CarInfo`

- **所属模块**: `车辆管理`
- **数据库表名**: `CarInfo`
- **字段总数**: `14`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | - |
| 2 | `carNo` | 车牌号 | `varchar2` | 2000 | 是 | - |
| 3 | `carType` | 车辆类型 | `integer` | - | 是 | - |
| 4 | `factoryNo` | 生产型号 | `varchar2` | 2000 | 是 | - |
| 5 | `price` | 价格 | `float` | - | 是 | - |
| 6 | `buyData` | 购买时间 | `varchar2` | 2000 | 是 | - |
| 7 | `engineNo` | 发动机型号 | `varchar2` | 2000 | 是 | - |
| 8 | `driver` | 司机 | `integer` | - | 是 | - |
| 9 | `remark` | 描述 | `varchar2` | 2000 | 是 | - |
| 10 | `createData` | 创建日期 | `varchar2` | 2000 | 是 | - |
| 11 | `createTime` | 创建时间 | `varchar2` | 2000 | 是 | - |
| 12 | `creater` | 创建人 | `integer` | - | 是 | - |
| 13 | `subCompanyId` | 公司 | `integer` | - | 是 | - |
| 14 | `usefee` | 使用里数 | `number` | - | 是 | - |
