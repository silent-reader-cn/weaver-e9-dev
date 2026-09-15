# 泛微OA 数据表: `fnalogdtl`

- **所属模块**: `财务管理`
- **数据库表名**: `fnalogdtl`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `log_uuid_td1` | 主键 | `char` | 32 | 否 | - |
| 2 | `main_uuid` | 日志主表id | `char` | 32 | 是 | - |
| 3 | `log_column` | 修改数据的列名称 | `varchar2` | 30 | 是 | - |
| 4 | `log_before_revision` | 修改前内容 | `varchar2` | 4000 | 是 | 如果有ID，保存名称及ID，格式数据对象名称【ID】 |
| 5 | `log_after_revision` | 修改后内容 | `varchar2` | 4000 | 是 | 如果有ID，保存名称及ID，格式数据对象名称【ID】 |
| 6 | `log_before_value` | 修改前表中存储的内容 | `varchar2` | 4000 | 是 | - |
| 7 | `log_after_value` | 修改后表中存储的内容 | `varchar2` | 4000 | 是 | - |
| 8 | `log_lable_id` | HtmlLabelIndex对应id | `integer` | - | 是 | 记录修改列的名称 |
| 9 | `log_description` | 描述 | `varchar2` | 4000 | 是 | - |
