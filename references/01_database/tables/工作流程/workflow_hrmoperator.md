# 泛微OA 数据表: `workflow_hrmoperator`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_hrmoperator`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `type` | 类型 | `varchar2` | 1000 | 是 | 类型3人力资源 |
| 2 | `objid` | 人员id | `varchar2` | 1000 | 是 | 人员id |
| 3 | `signorder` | 操作类型 | `varchar2` | 1000 | 是 | 逐个处理　会签 非会签 |
| 4 | `orders` | 排序 | `float` | 22 | 是 | 排序 |
| 5 | `groupid` | 操作者id | `varchar2` | 1000 | 是 | 操作者主键 |
| 6 | `groupdetailid` | 分组id | `varchar2` | 1000 | 是 | 分组id |
