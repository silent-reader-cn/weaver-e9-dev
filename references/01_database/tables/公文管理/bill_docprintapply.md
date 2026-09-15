# 泛微OA 数据表: `bill_docprintapply`

- **所属模块**: `公文管理`
- **数据库表名**: `bill_docprintapply`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 编号 | `integer` | - | 否 | - |
| 2 | `resourceid` | 资源编号 | `integer` | - | 是 | - |
| 3 | `deptid` | 单位编号 | `integer` | - | 是 | - |
| 4 | `relateddocid` | 相关文档编号 | `integer` | - | 是 | - |
| 5 | `printnum` | 打印数量 | `integer` | - | 是 | - |
| 6 | `applyreason` | 打印原因 | `varchar2` | 4000 | 是 | - |
| 7 | `requestid` | 请求编号 | `integer` | - | 是 | - |
| 8 | `hasprintnum` | 已经打印数量 | `integer` | - | 否 | - |
