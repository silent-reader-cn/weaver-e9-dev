# 泛微OA 数据表: `workflow_dimension`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_dimension`
- **字段总数**: `16`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | id，暂时没用，此字段不是主键。 |
| 2 | `typeid` | 待办维度id | `integer` | - | 否 | 字段有唯一性约束，不能为空。 |
| 3 | `typename` | 待办维度类型名称 | `varchar2` | 20 | 是 | 待办维度类型名称，如"flowAll" |
| 4 | `typetitle` | 待办维度显示名称 | `integer` | - | 是 | 这个是用于返回给前台显示名称，存的是多语言id |
| 5 | `showcount` | 维度是否显示数量 | `char` | 1 | 是 | 1：显示，其他：不显示 |
| 6 | `groupcolor` | 维度数量颜色 | `varchar2` | 20 | 是 | 如"#000000" |
| 7 | `sqlwhere` | 维度对应的查询条件 | `varchar2` | 1000 | 是 | 用括号包裹，括号内写入查询需要加的条件，不加则查待办的全部，暂时只支持使用workflow_currentoperator表中的字段做为条件。使用时需使用t2作为别名，如：(t2.workflowid not in(1)) |
| 8 | `typesettingjstr` | 流程中心元素查看类型辅助选项设置 | `varchar2` | 2000 | 是 | 这个是json类型，存放进去的必须为json格式，否则会解析错误。 |
| 9 | `keyid` | 流程中心元素查看类型id | `integer` | - | 是 | 流程中心元素查看类型id |
| 10 | `typelabelid` | 流程中心元素查看类型显示名称 | `integer` | - | 是 | 存放的是多语言id |
| 11 | `showcountjstr` | 流程中心元素显示数量设置 | `varchar2` | 2000 | 是 | 这个是json类型，存放进去的必须为json格式，否则会解析错误。 |
| 12 | `url` | url链接 | `varchar2` | 500 | 是 | 用于存放一个url，可以根据url直接访问待办列表指定维度数据 |
| 13 | `dsporder` | 维度内tab排序 | `number` | - | 是 | 维度内tab的排序 |
| 14 | `isshow` | 是否显示 | `char` | 1 | 是 | 1表示默认显示，0表示不显示 |
| 15 | `scope` | 维度范围 | `varchar2` | 10 | 是 | 维度范围，现在有doing（待办）、done（已办）、mine（我的请求）三个范围可用 |
| 16 | `viewcondition` | 查看参数，给代码使用 | `number` | - | 是 | 查看参数，给代码使用，待办维度要大于9，已办维度要大于5，我的请求维度要大于4，同一维度不允许重复。 |
