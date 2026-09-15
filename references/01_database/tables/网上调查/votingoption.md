# 泛微OA 数据表: `votingoption`

- **所属模块**: `网上调查`
- **数据库表名**: `votingoption`
- **字段总数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | - |
| 2 | `votingid` | 调查id | `integer` | - | 是 | - |
| 3 | `questionid` | 问题id | `integer` | - | 是 | - |
| 4 | `optioncount` | 选项数量 | `integer` | - | 是 | - |
| 5 | `showorder` | 选项排序 | `integer` | - | 是 | - |
| 6 | `roworcolumn` | 是行or是列 | `varchar2` | 40 | 是 | - |
| 7 | `description` | 描述 | `clob` | 4000 | 是 | - |
| 8 | `innershow` | 选项内附件、图片排序 | `integer` | - | 是 | - |
| 9 | `remarkorder` | 备注排序 | `integer` | - | 是 | - |
| 10 | `remark` | 备注 | `clob` | 4000 | 是 | - |
| 11 | `copyoption` | 复制选项来源 | `integer` | - | 是 | - |
