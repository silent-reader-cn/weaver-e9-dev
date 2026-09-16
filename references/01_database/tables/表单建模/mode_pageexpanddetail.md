# 泛微OA 数据表: `mode_pageexpanddetail`

- **中文名称**: 页面扩展详细信息
- **所属模块**: `表单建模`
- **数据库表名**: `mode_pageexpanddetail`
- **主键**: `id`
- **字段数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `triggerworkflowsetid` | 自定义流程id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `javafileaddress` | java条件 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 3 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 4 | `mainid` | 页面扩展主id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `interfacetype` | 接口类型 | `integer` | - | 是 | 否 | 否 | - | - | 1：触发审批工作流<br>2：外部接口动作<br>3：自定义java接口 |
| 6 | `interfacevalue` | 接口的值 | `varchar2` | 2000 | 是 | 否 | 否 | - | - | 和接口类型结合使用 |
