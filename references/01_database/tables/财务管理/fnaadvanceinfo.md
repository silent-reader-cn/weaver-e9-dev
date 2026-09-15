# 泛微OA 数据表: `fnaadvanceinfo`

- **所属模块**: `财务管理`
- **数据库表名**: `fnaadvanceinfo`
- **字段总数**: `12`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `requestid` | 流程id | `integer` | - | 是 | - |
| 3 | `dtlnumber` | 明细表序号 | `integer` | - | 是 | 记录来自的流程表单的明细表序号 |
| 4 | `dtlid` | 明细表记录id | `integer` | - | 是 | 记录来自的流程明细表记录id |
| 5 | `advancedirection` | 借款方向 | `integer` | - | 是 | 1：预付款；-1：冻结、冲销预付款； |
| 6 | `advancetype` | 借款类型 | `integer` | - | 是 | 预付款数据类型：0：个人；1：公务； |
| 7 | `advancerequestid` | 预付款流程requestid | `integer` | - | 是 | 冲销预付款流程，冲销记录选择的预付款流程requestid |
| 8 | `advancerequestiddtlid` | 预付款流程的明细id | `integer` | - | 是 | 冲销预付款流程，冲销记录选择的预付款流程的明细记录id |
| 9 | `amountadvance` | 金额 | `number` | (18,2) | 是 | 预付款金额； |
| 10 | `createdate` | 创建日期 | `char` | 10 | 是 | - |
| 11 | `createtime` | 创建时间 | `char` | 8 | 是 | - |
| 12 | `recordtype` | 记录类型 | `char` | 50 | 是 | 借款：advance 冲销：reverse 冻结借款：freezeAdvance |
