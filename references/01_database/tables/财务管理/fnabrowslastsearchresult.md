# 泛微OA 数据表: `fnabrowslastsearchresult`

- **所属模块**: `财务管理`
- **数据库表名**: `fnabrowslastsearchresult`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `idfk` | 科目id | `integer` | - | 是 | - |
| 2 | `charfk` | 作废 | `char` | 32 | 是 | - |
| 3 | `browsertype` | 浏览按钮类型 | `varchar2` | 100 | 否 | 仅支持科目类型 |
| 4 | `userid` | oa用户id | `integer` | - | 否 | - |
| 5 | `showorder` | 显示顺序 | `number` | (8,3) | 是 | - |
