# 泛微OA 数据表: `votingquestion`

- **中文名称**: 调查问题表
- **所属模块**: `网上调查`
- **数据库表名**: `votingquestion`
- **主键**: `id`
- **字段数**: `19`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | id | `integer` | - | 否 | 否 | 是 | - | - | - |
| 2 | `description` | 描述 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 3 | `votingid` | 调查id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `ismulti` | 是否是多选 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `isother` | 是否是其他 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `questioncount` | 问题数量 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `ismultino` | 不允许多选 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `showorder` | 问题排序 | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 9 | `pagenum` | 所在页数 | `varchar2` | 40 | 是 | 否 | 否 | - | - | - |
| 10 | `questiontype` | 问题类型 | `varchar2` | 40 | 是 | 否 | 否 | - | - | - |
| 11 | `ismustinput` | 是否必须输入 | `varchar2` | 40 | 是 | 否 | 否 | - | - | - |
| 12 | `limit` | 至少几项 | `varchar2` | 40 | 是 | 否 | 否 | - | - | - |
| 13 | `max` | 至多几项 | `varchar2` | 40 | 是 | 否 | 否 | - | - | - |
| 14 | `perrowcols` | 每行几列 | `varchar2` | 40 | 是 | 否 | 否 | - | - | - |
| 15 | `israndomsort` | 随机排序 | `varchar2` | 40 | 是 | 否 | 否 | - | - | - |
| 16 | `subject` | 问题描述 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 17 | `imagewidth` | 图片宽度 | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 18 | `imageheight` | 图片高度 | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 19 | `copyquestion` | 复制问题来源 | `integer` | - | 是 | 否 | 否 | - | - | - |
