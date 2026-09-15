# 泛微OA 数据表: `prj_worktype`

- **所属模块**: `项目管理`
- **数据库表名**: `prj_worktype`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 标识id | `integer` | - | 否 | 标识列 |
| 2 | `fullname` | 名称 | `varchar2` | 400 | 是 | 名称 |
| 3 | `description` | 描述 | `varchar2` | 1000 | 是 | 描述 |
| 4 | `worktypecode` | 编号 | `varchar2` | 400 | 是 | 编号 |
| 5 | `guid1` | uuid标识 | `char` | 36 | 是 | uuid标识 |
| 6 | `dsporder` | 顺序 | `number` | (10,2) | 是 | 顺序 |
