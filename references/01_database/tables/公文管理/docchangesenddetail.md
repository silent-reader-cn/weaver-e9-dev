# 泛微OA 数据表: `docchangesenddetail`

- **所属模块**: `公文管理`
- **数据库表名**: `docchangesenddetail`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 编号 | `integer` | - | 否 | - |
| 2 | `type` | 类型 | `varchar2` | 8 | 是 | - |
| 3 | `receiver` | 接收者 | `integer` | - | 是 | - |
| 4 | `receivedate` | 接收日期 | `varchar2` | 80 | 是 | - |
| 5 | `receivetime` | 接收时间 | `varchar2` | 80 | 是 | - |
| 6 | `requestid` | 请求编号 | `integer` | - | 是 | - |
| 7 | `detail` | 详情 | `varchar2` | 1000 | 是 | - |
| 8 | `status` | 状态 | `varchar2` | 8 | 是 | - |
