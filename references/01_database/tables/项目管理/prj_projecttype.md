# 泛微OA 数据表: `prj_projecttype`

- **所属模块**: `项目管理`
- **数据库表名**: `prj_projecttype`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `isprint` | 甘特图是否打印 | `char` | 1 | 是 | - |
| 2 | `id` | 标识id | `integer` | - | 否 | 标识列 |
| 3 | `fullname` | 名称 | `varchar2` | 400 | 是 | - |
| 4 | `description` | 描述 | `varchar2` | 1000 | 是 | - |
| 5 | `wfid` | 审批流程 | `integer` | - | 是 | - |
| 6 | `protypecode` | 编号 | `varchar2` | 400 | 是 | - |
| 7 | `insertworkplan` | 是否生成日程 | `char` | 1 | 是 | - |
| 8 | `guid1` | uuid标识 | `char` | 36 | 是 | - |
| 9 | `dsporder` | 顺序 | `number` | (10,2) | 是 | - |
