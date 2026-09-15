# 泛微OA 数据表: `workflow_subwfsetdetail`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_subwfsetdetail`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `subwfsetid` | 子流程设置表id | `integer` | - | 是 | - |
| 3 | `subworkflowfieldid` | 子流程字段id | `integer` | - | 是 | - |
| 4 | `mainworkflowfieldid` | 主流程字段id | `integer` | - | 是 | - |
| 5 | `ifsplitfield` | 是否拆分字段 | `char` | 1 | 是 | 1:是，0：否 |
| 6 | `isdetail` | 是否明细字段 | `integer` | - | 是 | 1：是，0：否 |
| 7 | `iscreatedocagain` | 是否重新生成文档 | `char` | 1 | 是 | - |
| 8 | `iscreateattachmentagain` | 是否重新生成附件 | `char` | 1 | 是 | - |
| 9 | `iscreateforanyone` | 是否为每个用户生成 | `char` | 1 | 是 | - |
