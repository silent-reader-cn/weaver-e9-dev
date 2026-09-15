# 泛微OA 数据表: `prj_projectstatus`

- **所属模块**: `项目管理`
- **数据库表名**: `prj_projectstatus`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 标识id | `integer` | - | 否 | 标识列 |
| 2 | `fullname` | 状态标签 | `varchar2` | 400 | 是 | - |
| 3 | `description` | 名称 | `varchar2` | 1000 | 是 | - |
| 4 | `summary` | 描述 | `varchar2` | 2000 | 是 | - |
| 5 | `dsporder` | 顺序 | `number` | (10,2) | 是 | - |
| 6 | `issystem` | 是否系统状态 | `char` | 1 | 是 | - |
| 7 | `guid1` | uuid标识 | `char` | 36 | 是 | - |
