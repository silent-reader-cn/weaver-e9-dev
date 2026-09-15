# 泛微OA 数据表: `hrmtraintype`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmtraintype`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `typeaim` | 目标 | `varchar2` | 4000 | 是 | 目标 |
| 2 | `typedocurl` | 文档url | `varchar2` | 1000 | 是 | 文档url |
| 3 | `typetesturl` | 考核url | `varchar2` | 1000 | 是 | 考核url |
| 4 | `typeoperator` | 负责人 | `varchar2` | 1000 | 是 | 负责人 |
| 5 | `id` | ID | `integer` | - | 否 | ID |
| 6 | `name` | 名称 | `varchar2` | 480 | 是 | 名称 |
| 7 | `description` | 描述 | `varchar2` | 480 | 是 | 描述 |
| 8 | `typecontent` | 培训内容 | `varchar2` | 4000 | 是 | 培训内容 |
