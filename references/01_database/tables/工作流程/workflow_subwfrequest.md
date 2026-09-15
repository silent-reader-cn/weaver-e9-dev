# 泛微OA 数据表: `workflow_subwfrequest`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_subwfrequest`
- **字段总数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `subwfid` | 子流程id | `integer` | - | 是 | - |
| 2 | `subrequestid` | 子流程请求id | `integer` | - | 是 | - |
| 3 | `mainrequestid` | 主流程请求id | `integer` | - | 是 | - |
| 4 | `issame` | 是否相同 | `char` | 1 | 是 | - |
