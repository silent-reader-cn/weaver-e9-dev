# 泛微OA 数据表: `workflow_codeseqreserved`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_codeseqreserved`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `codeseqid` | 流程编号流水号表id | `integer` | - | 是 | - |
| 3 | `reservedid` | 预留号 | `integer` | - | 是 | - |
| 4 | `reserveddesc` | 预留号描述 | `varchar2` | 1000 | 是 | - |
| 5 | `hasused` | 是否已使用 | `integer` | - | 是 | 1：是，0或其它：否 |
| 6 | `hasdeleted` | 是否已删除 | `integer` | - | 是 | 1：是，0或其它：否 |
| 7 | `reservedcode` | 预留code | `varchar2` | 1000 | 是 | - |
