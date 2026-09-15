# 泛微OA 数据表: `workflow_requestdeletelog`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_requestdeletelog`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `isold` | 是否老数据 | `char` | 1 | 是 | 1： 物理删除 0：逻辑删除 |
| 2 | `isvalid` | 是否恢复 | `char` | 1 | 是 | 1：已恢复 空或其他：未恢复 |
| 3 | `request_id` | 请求id | `integer` | - | 否 | - |
| 4 | `request_name` | 请求名称 | `varchar2` | 1000 | 是 | - |
| 5 | `operate_userid` | 操作用户id | `integer` | - | 否 | - |
| 6 | `operate_date` | 操作日期 | `char` | 10 | 否 | - |
| 7 | `operate_time` | 操作时间 | `char` | 8 | 否 | - |
| 8 | `workflow_id` | 流程id | `integer` | - | 否 | - |
| 9 | `client_address` | 客户端地址 | `varchar2` | 1000 | 是 | - |
| 10 | `deletetabledata` | 删除的表单数据JSON格式 | `clob` | 4000 | 是 | - |
