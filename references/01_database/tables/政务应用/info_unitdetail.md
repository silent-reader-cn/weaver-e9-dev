# 泛微OA 数据表: `info_unitdetail`

- **所属模块**: `政务应用`
- **数据库表名**: `info_unitdetail`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 数据id | `integer` | - | 否 | - |
| 2 | `uuid` | 32位随机id | `varchar2` | 32 | 是 | - |
| 3 | `mainid` | 上报单位id | `integer` | - | 是 | - |
| 4 | `type` | 数据类型 | `integer` | - | 是 | 0上报人员 1审批人员 2单位组 |
| 5 | `dataid` | 对应数据id | `integer` | - | 是 | - |
