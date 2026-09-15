# 泛微OA 数据表: `hrm_protection_question`

- **所属模块**: `人力资源`
- **数据库表名**: `hrm_protection_question`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `user_id` | 用户id | `integer` | - | 否 | 用户id |
| 3 | `question` | 问题描述value值 | `varchar2` | 800 | 否 | 问题描述value值 |
| 4 | `answer` | 问题答案value值 | `varchar2` | 1000 | 否 | 问题答案value值 |
| 5 | `delflag` | 是否删除 | `integer` | - | 否 | 0是默认，1是删除 |
