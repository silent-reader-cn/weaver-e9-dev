# 泛微OA 数据表: `fnaadvanceinfoamountlog`

- **所属模块**: `财务管理`
- **数据库表名**: `fnaadvanceinfoamountlog`
- **字段总数**: `16`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `requestid` | 流程id | `integer` | - | 是 | - |
| 3 | `dtlnumber` | 明细表序号 | `integer` | - | 是 | - |
| 4 | `dtlid` | 明细表记录id | `integer` | - | 是 | - |
| 5 | `guid1` | 批次号 | `varchar2` | 400 | 是 | - |
| 6 | `nodeid` | 操作节点id | `integer` | - | 是 | - |
| 7 | `src` | 流程操作类型 | `varchar2` | 200 | 是 | - |
| 8 | `advancedirection` | 金额方向 | `integer` | - | 是 | - |
| 9 | `advancetype` | 类型 | `integer` | - | 是 | - |
| 10 | `amountadvancebefore` | 调整前金额 | `number` | (18,2) | 是 | - |
| 11 | `amountadvanceafter` | 调整后金额 | `number` | (18,2) | 是 | - |
| 12 | `createuid` | 创建人id | `integer` | - | 是 | - |
| 13 | `createdate` | 创建日期 | `char` | 10 | 是 | - |
| 14 | `createtime` | 创建时间 | `char` | 8 | 是 | - |
| 15 | `memo1` | 调整说明 | `varchar2` | 4000 | 是 | - |
| 16 | `fnawftype` | 日志类型 | `char` | 50 | 是 | - |
