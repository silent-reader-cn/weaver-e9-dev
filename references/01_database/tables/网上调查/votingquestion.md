# 泛微OA 数据表: `votingquestion`

- **所属模块**: `网上调查`
- **数据库表名**: `votingquestion`
- **字段总数**: `19`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | - |
| 2 | `description` | 描述 | `varchar2` | 1000 | 是 | - |
| 3 | `votingid` | 调查id | `integer` | - | 是 | - |
| 4 | `ismulti` | 是否是多选 | `integer` | - | 是 | - |
| 5 | `isother` | 是否是其他 | `integer` | - | 是 | - |
| 6 | `questioncount` | 问题数量 | `integer` | - | 是 | - |
| 7 | `ismultino` | 不允许多选 | `integer` | - | 是 | - |
| 8 | `showorder` | 问题排序 | `integer` | - | 是 | - |
| 9 | `pagenum` | 所在页数 | `varchar2` | 40 | 是 | - |
| 10 | `questiontype` | 问题类型 | `varchar2` | 40 | 是 | - |
| 11 | `ismustinput` | 是否必须输入 | `varchar2` | 40 | 是 | - |
| 12 | `limit` | 至少几项 | `varchar2` | 40 | 是 | - |
| 13 | `max` | 至多几项 | `varchar2` | 40 | 是 | - |
| 14 | `perrowcols` | 每行几列 | `varchar2` | 40 | 是 | - |
| 15 | `israndomsort` | 随机排序 | `varchar2` | 40 | 是 | - |
| 16 | `subject` | 问题描述 | `clob` | 4000 | 是 | - |
| 17 | `imagewidth` | 图片宽度 | `integer` | - | 是 | - |
| 18 | `imageheight` | 图片高度 | `integer` | - | 是 | - |
| 19 | `copyquestion` | 复制问题来源 | `integer` | - | 是 | - |
