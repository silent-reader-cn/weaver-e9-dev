# 泛微OA 数据表: `fnafeewfinfo`

- **所属模块**: `财务管理`
- **数据库表名**: `fnafeewfinfo`
- **字段总数**: `15`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `fnawftypereverseadvance` | 启用预申请业务逻辑 | `integer` | - | 是 | 大于0表示：启用了报销明细表效果 |
| 2 | `budgetcanbenegative` | 报销金额可为负数 | `integer` | - | 是 | 1:报销金额可为负数；其他不可为负数 |
| 3 | `id` | 主键 | `integer` | - | 否 | - |
| 4 | `workflowid` | 流程workflowid | `integer` | - | 是 | - |
| 5 | `enable` | 启用 | `integer` | - | 是 | 1：启用；其他：未启用； |
| 6 | `lastmodifieddate` | 最后编辑日期 | `char` | 10 | 是 | - |
| 7 | `templatefile` | 业务逻辑处理页面 | `varchar2` | 4000 | 是 | pc端： 流程业务逻辑页面 |
| 8 | `templatefilemobile` | 业务逻辑处理页面 | `varchar2` | 4000 | 是 | mobile端： 流程业务逻辑页面 |
| 9 | `fnawftype` | 费控流程类型 | `varchar2` | 50 | 是 | borrow：借款流程； repayment：还款流程； fnafeewf：报销流程 |
| 10 | `fnawftypeborrow` | 启用借款业务逻辑 | `integer` | - | 是 | 大于0表示：启用了借款流明细表效果 |
| 11 | `fnawftypecoll` | 启用还款业务逻辑 | `integer` | - | 是 | 大于0表示：启用了还款明细表效果 |
| 12 | `fnawftypereverse` | 启用冲销业务逻辑 | `integer` | - | 是 | 大于0表示：启用了冲销明细表效果 |
| 13 | `fnawftypereim` | 启用报销业务逻辑 | `integer` | - | 是 | 大于0表示：启用了报销明细表效果 |
| 14 | `overstandardtips` | 作废 | `varchar2` | 4000 | 是 | - |
| 15 | `isallnodescontrol` | 是否：所有节点均进行费控校验 | `integer` | - | 是 | - |
