# 泛微OA 数据表: `fnaborrowinfoamountlog`

- **所属模块**: `财务管理`
- **数据库表名**: `fnaborrowinfoamountlog`
- **字段总数**: `16`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `requestid` | 流程requestid | `integer` | - | 是 | - |
| 3 | `dtlnumber` | 明细表序号 | `integer` | - | 是 | 记录来自的流程表单的明细表序号 |
| 4 | `dtlid` | 明细表记录id | `integer` | - | 是 | 记录来自的流程明细表记录id |
| 5 | `guid1` | 批次号 | `varchar2` | 50 | 是 | 同次修改操作的批次字段 |
| 6 | `nodeid` | 操作节点id | `integer` | - | 是 | - |
| 7 | `src` | 流程操作类型 | `varchar2` | 25 | 是 | - |
| 8 | `borrowdirection` | 借款方向 | `integer` | - | 是 | 1：借款；-1：冻结借款、还款、冲销； |
| 9 | `borrowtype` | 借款类型 | `integer` | - | 是 | 借款流程的借款类型：0：个人借款；1：公务借款； |
| 10 | `amountborrowbefore` | 调整前金额 | `number` | (18,2) | 是 | 借款流程：借款金额； 还款（报销）流程：冲销金额； |
| 11 | `amountborrowafter` | 调整后金额 | `number` | (18,2) | 是 | 借款流程：借款金额； 还款流程：还款金额； |
| 12 | `createuid` | 创建人id | `integer` | - | 是 | - |
| 13 | `createdate` | 创建日期 | `char` | 10 | 是 | - |
| 14 | `createtime` | 创建时间 | `char` | 8 | 是 | - |
| 15 | `memo1` | 调整说明 | `varchar2` | 4000 | 是 | - |
| 16 | `fnawftype` | 日志类型 | `char` | 50 | 是 | 借款流程：borrow 还款流程：repayment |
