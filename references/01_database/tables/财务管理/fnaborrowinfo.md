# 泛微OA 数据表: `fnaborrowinfo`

- **所属模块**: `财务管理`
- **数据库表名**: `fnaborrowinfo`
- **字段总数**: `15`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `createdate` | 创建日期 | `char` | 10 | 是 | - |
| 2 | `createtime` | 创建时间 | `char` | 8 | 是 | - |
| 3 | `recordtype` | 记录类型 | `char` | 50 | 是 | 借款：borrow 冲销：reverse 冻结借款：freezeBorrow |
| 4 | `applicantid` | 申请人id | `integer` | - | 是 | - |
| 5 | `departmentid` | 部门id | `integer` | - | 是 | 申请人申请时所在部门id |
| 6 | `subcompanyid1` | 分部id | `integer` | - | 是 | 申请人申请时所在分部id |
| 7 | `id` | 主键 | `integer` | - | 否 | - |
| 8 | `requestid` | 流程id | `integer` | - | 是 | - |
| 9 | `dtlnumber` | 明细表序号 | `integer` | - | 是 | 记录来自的流程表单的明细表序号 |
| 10 | `dtlid` | 明细表记录id | `integer` | - | 是 | 记录来自的流程明细表记录id |
| 11 | `borrowdirection` | 借款方向 | `integer` | - | 是 | 1：借款；-1：冻结借款、还款、冲销； |
| 12 | `borrowtype` | 借款类型 | `integer` | - | 是 | 借款流程的借款类型：0：个人借款；1：公务借款； |
| 13 | `borrowrequestid` | 借款流程requestid | `integer` | - | 是 | 还款流程，冲销记录选择的借款流程requestid |
| 14 | `borrowrequestiddtlid` | 借款流程的明细id | `integer` | - | 是 | 还款流程，冲销记录选择的借款流程的明细记录id |
| 15 | `amountborrow` | 金额 | `number` | (18,2) | 是 | 借款流程：借款金额；还款流程：冲销金额； |
