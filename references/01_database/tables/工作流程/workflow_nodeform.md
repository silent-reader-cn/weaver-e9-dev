# 泛微OA 数据表: `workflow_nodeform`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_nodeform`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `isalonerow` | 独占一行 | `char` | 1 | 是 | - |
| 2 | `isorder` | 是否排序字段 | `integer` | - | 是 | - |
| 3 | `ordertype` | 排序类型 | `integer` | - | 是 | 0：升序,1：降序 |
| 4 | `orderindex` | 排序字段顺序 | `integer` | - | 是 | - |
| 5 | `nodeid` | 的 | `integer` | - | 是 | - |
| 6 | `fieldid` | 字段id | `integer` | - | 是 | - |
| 7 | `isview` | 当前节点字段是否可见 | `char` | 1 | 是 | 0：否,1：是 |
| 8 | `isedit` | 当前节点字段是否可编辑 | `char` | 1 | 是 | 0：否,1：是 |
| 9 | `ismandatory` | 当前节点字段是否必须输入 | `char` | 1 | 是 | 0：否,1：是 |
| 10 | `orderid` | 自定义页面排序id | `number` | (10,2) | 是 | - |
