# 泛微OA 数据表: `docseccategorymould`

- **中文名称**: 目录模版设置表
- **所属模块**: `知识管理`
- **数据库表名**: `docseccategorymould`
- **主键**: `id`
- **字段数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 是 | - | - | - |
| 2 | `seccategoryid` | 子目录id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `mouldtype` | 模版类型 | `integer` | - | 是 | 否 | 否 | - | - | 1：html显示模版<br>2：html编辑模版<br>3：word显示模版<br>4：word编辑模版<br>5：excel显示模版<br>6：excel编辑模版<br>7：wps显示模版<br>8：wps编辑模版<br>9：et显示模版<br>10：et编辑模版 |
| 4 | `mouldid` | 模版id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `isdefault` | 是否默认 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `mouldbind` | 模版绑定 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `docseccategorytemplateid` | 目录模板id | `integer` | - | 是 | 否 | 否 | - | - | - |
