# 泛微OA 数据表: `workflow_tridiffwfsubwffield`

- **中文名称**: 触发不同流程子流程字段设置表
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_tridiffwfsubwffield`
- **主键**: `id`
- **字段数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `tridiffwfsubwfid` | 触发不同流程子流程设置表id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `subworkflowfieldid` | 子流程字段id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `mainworkflowfieldid` | 主流程字段id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `isdetail` | 是否明细字段 | `integer` | - | 是 | 否 | 否 | - | - | 1：是，0或其它为否 |
| 6 | `iscreatedocagain` | 是否重新生成文档或附件 | `char` | 1 | 是 | 否 | 否 | - | - | 1:是，0或其他为否 |
| 7 | `ifsplitfield` | 是否字段值拆分 | `char` | 1 | 是 | 否 | 否 | - | - | 1：是，0或其他为否 |
| 8 | `iscreateattachmentagain` | 是否为重新添加附件 | `char` | 1 | 是 | 否 | 否 | - | - | - |
