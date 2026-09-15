# 泛微OA 数据表: `carbasic`

- **所属模块**: `车辆管理`
- **数据库表名**: `carbasic`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `workflowid` | 流程id | `integer` | - | 是 | 对应workflow_base表id |
| 3 | `workflowname` | 流程名称 | `varchar2` | 800 | 是 | - |
| 4 | `typeid` | 流程类型id | `integer` | - | 是 | - |
| 5 | `wtype` | 生成类型 | `integer` | - | 是 | 0，卡片生成表单；1，自定义表单 |
| 6 | `formid` | 表单id | `integer` | - | 是 | - |
| 7 | `isuse` | 是否开启 | `integer` | - | 是 | 0：不开启；1：开启 |
| 8 | `modifydate` | 修改时间 | `varchar2` | 160 | 是 | 暂未使用 |
