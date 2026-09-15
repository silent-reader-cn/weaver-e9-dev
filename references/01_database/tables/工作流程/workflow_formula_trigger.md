# 泛微OA 数据表: `workflow_formula_trigger`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_formula_trigger`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `showorder` | 显示顺序 | `integer` | 100 | 是 | 显示顺序 |
| 2 | `id` | 主键编码 | `integer` | 100 | 是 | 主键 |
| 3 | `actionname` | 触发动作名称 | `varchar2` | 1000 | 是 | 触发动作名称，多语言字段 |
| 4 | `description` | 描述信息 | `varchar2` | 1000 | 是 | 描述信息，便于查看数据库数据时知道当前数据行是什么触发动作，代码执行中没有用到 |
| 5 | `event` | 动作事件 | `varchar2` | 1000 | 是 | 执行动作时，依据此字段判断所选择的动作 |
| 6 | `type` | 类型 | `varchar2` | 1000 | 是 | 触发类型，包含component：单元格、'window'：窗口事件、'process'：流程相关事件 |
